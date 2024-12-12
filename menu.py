from family import Family
from person import Person
from datetime import datetime
import graph
import os
import json
import re

def show_initial_menu():
    """
    Display the initial menu and get user input
    """
    menu_display = """To get started, please choose one of the following options:

        1. Create a new family
        2. Continue with existing family data (demonstration family trees provided here)

        """
    print(menu_display)
    user_input = input("Please enter the number corresponding to your choice: ").strip()
    while user_input not in {"1", "2"}:
        print("Invalid choice. Please enter 1 or 2.")
        user_input = input("Please enter the number corresponding to your choice: ")
    return user_input

def get_user_family():
    choice = show_initial_menu()
    user_family = None
    if choice == "1":
        family_name = input("Enter the family name: ").strip()
        user_family = Family(family_name)
        print(f"New family '{family_name}' created.")

    elif choice == "2":
        filename = input("Enter a JSON filename to load the family tree or "
                         "'DEMO1' to load Zeynab's family tree for demonstration "
                         "or 'DEMO2' to load Kardashian's family tree for demonstration: ").strip()
        family_name = input("Enter a name for the family or the demonstration family: ").strip()

        if filename.strip() == "DEMO1":
            filename = "Zeynab_family_tree.json"
        elif filename.rstrip() == "DEMO2":
            filename = "Kardashian_family_tree.json"

        family_tree = load_family_from_json(filename)
        user_family = Family(family_name, family_tree)
        if not family_tree:
            print(f"New family '{family_name}' created.")
        else:
            print(f"The {family_name} family is loaded from {filename}.")
        input("Press Enter to continue...")

    return user_family

def show_option_menu():
    """
    Display the menu for selecting different actions
    """
    menu_display = """
    Please choose one of the following options:

    1. Add a new person to your family tree
    2. Remove a person from your family tree
    3. Add immediate relationship for a person
    4. Remove immediate relationship for a person
    5. Update a person's information
    6. Find the relationship (path) between two people
    7. Look up a person's information
    8. Visualize your family tree
    9. Save the data into a new or existing JSON file
    10. Exit the program

    Please input the number corresponding to your intended action:
    """
    print(menu_display)
    user_input = input("Your choice: ").strip()
    while user_input not in {"1", "2", "3", "4", "5", "6", "7", "8", "9", "10"}:
        print("Invalid choice. Please enter a number between 1 and 10.")
        user_input = input("Your choice: ").strip()
    return user_input

def loop_main_menu(user_family):
    user_action = show_option_menu()
    while user_action != "10":
        user_family = execute_action(user_action,user_family)
        input("Press Enter to continue")
        user_action = show_option_menu()
    print("You have exited the program.")

# Execute a specific action about user's family tree
def execute_action(action, user_family):
    if action == "1":  # Add a new person to your family tree
        user_family = menu_create_person(user_family)
    elif action == "2":  # Remove a person from your family tree
        user_family = menu_delete_person(user_family)
    elif action == "3":  # Add a relationship for a person
        user_family = menu_add_relationships_for_person(user_family)
    elif action == "4":  # Remove a relationship for a person
        user_family = menu_remove_relationships_for_person(user_family)
    elif action == "5":  # Update a person's information
        user_family = menu_update_person_info(user_family)
    elif action == "6":  # Find the relationship (path) between two people
        user_family = menu_search_for_person(user_family)
    elif action == "7":  # Look up a person's information
        menu_get_person_info(user_family)
    elif action == "8":  # Visualize your family tree
        menu_draw_family_graph(user_family)
    elif action == "9":  # Save the data into a new or existing JSON file
        menu_save_family_to_json(user_family)
    return user_family

def menu_create_person(user_family):
    print(f"\nBelow is the current family dictionary for your information: ")
    user_family.print_family_dict()
    name = input("\nEnter the name of the new person: ")
    birthdate = get_valid_birthdate()
    gender = input("Enter the gender (M/F): ").strip().upper()
    while gender not in {"F", "M"}:
        gender = input("Invalid input. Please enter 'M' for Male or 'F' for Female.")
    occupation = input("Enter the occupation (optional): ") or "Unknown"
    is_alive_input = input("Is this person alive? (Y/N): ").strip().upper()
    while is_alive_input not in {"Y", "N"}:
        print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")
        is_alive_input = input("Is this person alive? (Y/N): ").strip().upper()
    is_alive = True if is_alive_input.upper() == "Y" else False
    user_family.create_person_in_fam(name, birthdate, gender, occupation, is_alive)

    add_relation_option = input("Do you want to add relations for the person? Enter 'Yes' or 'No'： ").strip().lower()
    while add_relation_option not in "yes" or "no":
        print("Invalid input. Please enter 'Yes' or 'No'.")
        add_relation_option = input("Do you want to add relations for the person? Enter 'Yes' or 'No'： ")
    if add_relation_option == "yes":
        user_family = menu_add_relationships_for_person(user_family)
    return user_family

def menu_delete_person(user_family):
    print(f"\nBelow is the current family dictionary for your information: ")
    user_family.print_family_dict()
    person_name = input("Enter the name of the person to remove: ")
    user_family.delete_person(person_name)
    return user_family

def menu_add_relationships_for_person(user_family):
    while True:
        try:
            print("\nImmediate family relationships includes: mother, father, sibling, children, partner.")
            first_person_name = input("Enter the name of the first person ").strip()
            second_person_name = input("Enter the name of the second person ").strip()
            relation = input("Enter their relation: ")
            user_family.add_relation(first_person_name,relation,second_person_name)
            return user_family
        except Exception as err:
            print(f"An error occurred: {err}. Please try again.")

def menu_remove_relationships_for_person(user_family):
    while True:
        try:
            print("Immediate family relationships includes: mother, father, sibling, children, partner.")
            first_person_name = input("Enter the name of the first person ").strip()
            second_person_name = input("Enter the name of the second person ").strip()
            relation = input("Enter their relation: ")
            user_family.remove_relation(first_person_name,relation,second_person_name)
            return user_family
        except Exception as err:
            print(f"An error occurred: {err}. Please try again.")

def menu_update_person_info(user_family):
    while True:
        try:
            print(f"\nBelow is the current family dictionary for your information: ")
            user_family.print_family_dict()
            person_name = input("\nEnter the name of the person to update: ")
            attribute = input('Enter the attribute to update (please enter "gender", "occupation", "is_alive"): ')
            while attribute not in ["gender", "occupation", "is_alive"]:
                print("Invalid input.")
                attribute = input('Enter the attribute to update (please enter "gender", "occupation", "is_alive"): ')
            if attribute == "is_alive":
                new_attr = input("Enter the new value for is_alive ('Y' for Yes, 'N' for No): ")
                while new_attr.upper() not in {"Y", "N"}:
                    print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")
                    new_attr = input("Enter the new value for is_alive ('Y' for Yes, 'N' for No): ")
                new_attr = True if new_attr.upper() == "Y" else False
            else:
                new_attr = input(f"Enter the new value for {attribute}: ")
            user_family.update_person_info(person_name, attribute, new_attr)
            return user_family
        except Exception as err:
            print(f"An error occurred: {err}. Please try again.")

def menu_search_for_person(user_family):
    while True:
        try:
            first_name = input("Enter the first person's name: ")
            second_name = input("Enter the second person's name: ")
            user_family.search_for_person(first_name, second_name)
            return user_family
        except Exception as err:
            print(f"An error occurred: {err}. Please try again.")

def menu_get_person_info(user_family):
    while True:
        try:
            person_name = input("Enter the name of the person to look up: ")
            user_family.get_person_info(person_name)
            return
        except Exception as err:
            print(f"An error occurred: {err}. Please try again.")

def menu_draw_family_graph(user_family):
    try:
        graph.create_graph(user_family)
        return
    except Exception as err:
        print(f"An error occurred: {err}. Please try again.")

def menu_save_family_to_json(user_family):
    try:
        filename = input("Enter the filename to save (e.g., Zeynab_family_tree.json): ")
        user_family.save_family_to_json(filename)
        return
    except Exception as err:
        print(f"An error occurred: {err}. Please try again.")

def get_valid_birthdate():
    """
    Helper function to get a valid birthdate input in the format DD-MM-YYYY.
    """
    while True:
        birthdate = input("Enter the birthdate (DD-MM-YYYY): ").strip()
        if re.match(r"^\d{2}-\d{2}-\d{4}$", birthdate):
            try:
                datetime.strptime(birthdate, "%d-%m-%Y")
                return birthdate
            except ValueError:
                print("Invalid date. Please enter a valid date in the format DD-MM-YYYY.")
        else:
            print("Invalid format. Please enter the birthdate in the format DD-MM-YYYY.")

def load_family_from_json(filename="Kardashian_family_tree.json"):
    """Load the family tree data from a JSON file and reconstruct the family graph."""
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' does not exist.")
        return None

    with open(filename, "r") as file:
        json_data = json.load(file)

    # Step 1: Create Person objects without relations
    family_dict = {
        name: Person(
            name=data["name"],
            birthdate=data["birthdate"],
            gender=data["gender"],
            occupation=data["occupation"],
            is_alive=data["is_alive"]
        )
        for name, data in json_data.items()
    }

    # Step 2: Re-establish relationships using `relation_dict`
    for name, data in json_data.items():
        person = family_dict[name]
        for relation, relatives in data["relation_dict"].items():
            for relative_name in relatives:
                person.add_relation(relation, family_dict[relative_name])

    print(f"Family tree loaded from {filename}")
    return family_dict
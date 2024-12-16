from family import Family
from person import Person
from datetime import datetime
from graph import create_graph
import os
import json
import re


class Menu:
    """This is a class for processing user response and provide reactions"""
    def __init__(self):
        self.family = None

    def show_initial_menu(self):
        """
        Display the initial menu and get user input
        """
        menu_display = """To get started, please choose one of the following options:

        1. Create a new family
        2. Continue with existing family data

        """
        print(menu_display)
        user_input = input("Please enter the number corresponding to your choice: ").strip()
        while user_input not in {"1", "2"}:
            print("Invalid choice. Please enter 1 or 2.")
            user_input = input("Please enter the number corresponding to your choice: ")
        return user_input

    def show_option_menu(self):
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
        user_input = input("Your choice: ")
        while user_input not in {"1", "2", "3", "4", "5", "6", "7", "8", "9", "10"}:
            print("Invalid choice. Please enter a number between 1 and 10.")
            user_input = input("Your choice: ").strip()
        return user_input

    def load_family_from_json(self, filename="Kardashian_family_tree.json"):
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

    def execute_action(self, action, *args):
        """
        Execute a specific action based on the user's input
        """
        if action == "1":  # Add a new person to your family tree
            self.family.create_person_in_fam(*args)
            self.add_relationships_for_person(args[0])
        elif action == "2":  # Remove a person from your family tree
            self.family.delete_person(*args)
        elif action == "3":  # Add a relationship for a person
            self.add_relationships_for_person(*args)
        elif action == "4":  # Remove a relationship for a person
            self.remove_relationships_for_person(*args)
        elif action == "5":  # Update a person's information
            self.family.update_person_info(*args)
        elif action == "6":  # Find the relationship (path) between two people
            return self.family.search_for_person(*args)
        elif action == "7":  # Look up a person's information
            self.family.get_person_info(*args)
        elif action == "8":  # Visualize your family tree
            self.family.print_family_dict()  # CHANGE!!!!!
        elif action == "9":  # Save the data into a new or existing JSON file
            self.family.save_family_to_json(*args)
        elif action == "10":  # Exit the program with confirmation
            # confirm_exit = input("Are you sure you want to exit? (Y/N): ").strip().upper()
            # while confirm_exit not in {"Y", "N"}:
            #     confirm_exit = input("Invalid choice. Are you sure you want to exit? (Y/N): ").strip().upper()
            # if confirm_exit == "Y":
            #     print("Exiting the Family Tree Management System. Goodbye!")
            exit()  # Exit the program
            # else:
            #     print("Exit cancelled. Returning to the menu.")
            #     return -1
        else:
            print("Invalid action.")

        input("Press Enter to return to the menu...")

    def run(self):
        """
        Run the menu system, getting user input and executing actions
        """
        while True:
            choice = self.show_initial_menu()
            if choice == "1":
                family_name = input("Enter the family name: ").strip()
                self.family = Family(family_name)
                print(f"New family '{family_name}' created.")
                input("Press Enter to continue...")
            elif choice == "2":
                filename = input('Enter the JSON filename or "DEMO" to load: ').strip()

                if filename.rstrip() == "DEMO":
                    filename = "Kardashian_family_tree.json"

                family_tree = self.load_family_from_json(filename)
                family_name = input("Enter the family name: ").strip()
                self.family = Family(family_name, family_tree)
                if not family_tree:
                    print(f"New family '{family_name}' created.")
                else:
                    print(f"The {family_name} family is loaded from {filename}.")
                input("Press Enter to continue...")
            else:
                print("Invalid option.")
                continue

            while True:
                option = self.show_option_menu()
                if option == "1":
                    name = input("Enter the name of the new person: ")
                    birthdate = self.get_valid_birthdate()
                    gender = input("Enter the gender (M/F): ")
                    while gender not in {"F", "M"}:
                        gender = input("Invalid input. Please enter 'M' for Male or 'F' for Female.")
                    occupation = input("Enter the occupation (optional): ") or "Unknown"
                    is_alive_input = input("Is this person alive? (Y/N): ").strip().upper()
                    while is_alive_input not in {"Y", "N"}:
                        print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")
                        is_alive_input = input("Is this person alive? (Y/N): ").strip().upper()
                    is_alive = True if is_alive_input.upper() == "Y" else False
                    self.execute_action(option, name, birthdate, gender, occupation, is_alive)
                elif option == "2":
                    name = input("Enter the name of the person to remove: ")
                    self.execute_action(option, name)
                elif option == "3":
                    name = input("Enter the name of the person to add immediate relationship to: ")
                    self.execute_action(option, name)
                elif option == "4":
                    name = input("Enter the name of the person to remove immediate relationship to: ")
                    self.execute_action(option, name)
                elif option == "5":
                    name = input("Enter the name of the person to update: ")
                    attribute = input("Enter the attribute to update (gender, occupation, is_alive): ")
                    if attribute == "is_alive":
                        new_attr = input("Enter the new value for is_alive ('Y' for Yes, 'N' for No): ")
                        while new_attr.upper() not in {"Y", "N"}:
                            print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")
                            new_attr = input("Enter the new value for is_alive ('Y' for Yes, 'N' for No): ")
                        new_attr = True if new_attr.upper() == "Y" else False
                    else:
                        new_attr = input(f"Enter the new value for {attribute}: ")
                    self.execute_action(option, name, attribute, new_attr)
                elif option == "6":
                    first_name = input("Enter the first person's name: ")
                    second_name = input("Enter the second person's name: ")
                    self.execute_action(option, first_name, second_name)
                elif option == "7":
                    name = input("Enter the name of the person to look up: ")
                    self.execute_action(option, name)
                elif option == "8":
                    create_graph(self.family)
                elif option == "9":
                    filename = input("Enter the filename to save (e.g., Kardashian_family_tree.json): ")
                    self.execute_action(option, filename)
                elif option == "10":
                    if self.execute_action(option) == -1:
                        # if they did not confirm exit and came back
                        continue
                    else:
                        break
                else:
                    print("Invalid option.")

    def add_relationships_for_person(self, person_name):
        """
        Add immediate relationships for a person in the family.
        """
        if len(self.family.family_dict) == 1:
            print(f"\nThis is the current family: ")
            self.family.print_family_dict()
            print()
            return

        print(f"\nNow let's define immediate family relationships for {person_name}.")
        print("Immediate family relationships includes: mother, father, sibling, children, partner.")
        while True:
            print(f"\nThis is the current family: ")
            self.family.print_family_dict()
            print()
            second_person_name = input("Enter the name of another person in the family to define a relationship or pressed 'N' to quit: ").strip()
            if second_person_name.upper() == 'N':
                break
            if second_person_name == person_name:
                print("You cannot define a relationship with the same person. Please try again.")
                continue

            relationship = input(f"Fill in the [ ]: {person_name}'s [RELATIONSHIP] is {second_person_name}" +
                                  "(Choose [RELATIONSHIP] from mother, father, sibling, children, partner): ").strip()

            # Call the add_relation method to build the relation_dict
            self.family.add_relation(person_name, relationship, second_person_name)

            add_more = input("Do you want to add another relationship? (Y/N): ").strip().upper()
            while add_more not in {"Y", "N"}:
                add_more = input("Invalid input. Do you want to add another immediate relationship? (Y/N): ").strip().upper()

            if add_more == "N":
                break

        # Confirm all relationships are added
        confirm = input(f"Are all immediate relationships for {person_name} added? (Y/N) ").strip().upper()
        while confirm not in {"Y", "N"}:
            confirm = input("Invalid input. Are all relationships for this person added? (Y/N): ").strip().upper()

        if confirm == "Y":
            print(f"All relationships for {person_name} have been added.")
        else:
            input("Press Enter to continue...")
            self.add_relationships_for_person(person_name)
    
    def remove_relationships_for_person(self, person_name):
        """
        Remove relationships for a person in the family.
        """

        print("Immediate family relationships includes: mother, father, sibling, children, partner.")
        while True:
            print(f"\nThis is the current family: ")
            self.family.print_family_dict()
            print()
            second_person_name = input("Enter the name of another person in the family to remove a relationship or pressed 'N' to quit: ").strip()
            if second_person_name.upper() == 'N':
                break
            if second_person_name == person_name:
                print("You cannot remove a relationship with the same person. Please try again.")
                continue

            relationship = input(f"Fill in the [ ]: {person_name}'s [RELATIONSHIP] was {second_person_name}" +
                                  "(Choose [RELATIONSHIP] from mother, father, sibling, children, partner): ").strip()

            self.family.remove_relation(person_name, relationship, second_person_name)

            remove_more = input("Do you want to remove another relationship? (Y/N): ").strip().upper()
            while remove_more not in {"Y", "N"}:
                remove_more = input("Invalid input. Do you want to remove another immediate relationship? (Y/N): ").strip().upper()

            if remove_more == "N":
                break
    
    def get_valid_birthdate(self):
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

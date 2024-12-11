from person import Person
from collections import deque
import json

# This demo file is linked to the Zeynab_family_tree.json file

def main():
    family_dict = {}

    # Zeynab could change the people in the demo family, starting from this line
    me = Person("Zeynab", "09-11-1999", "F", "Student", True)
    mom = Person("Sigge", "23-10-1962", "F", "Nurse", True)
    aunt = Person("Simagne", "09-11-1958", "F", "Jeweler", True)
    cousin = Person("Mimi", "04-09-1989", "F", "Manager", True)
    grandpa = Person("Jedd", "06-08-1939", "M", "Unknown", True)
    sister = Person("Zekeya", "01-04-2002", "F", "Student", True)
    

    me.add_relation("mother", mom)
    me.add_relation("sibling", sister)

    sister.add_relation("mother", mom)
    sister.add_relation("sibling", me)

    mom.add_relation("children", me)
    mom.add_relation("children", sister)
    mom.add_relation("father", grandpa)
    mom.add_relation("sibling", aunt)

    aunt.add_relation("father", grandpa)
    aunt.add_relation("sibling", mom)
    aunt.add_relation("children", cousin)

    cousin.add_relation("mother", aunt)

    grandpa.add_relation("children", mom)
    grandpa.add_relation("children", aunt)

    print("Me:\n", me)
    print("Sister:\n", sister)
    print("Mom:\n", mom)
    print("Aunt:\n", aunt)
    print("Cousin:\n", cousin)
    print("Grandpa:\n", grandpa)

    add_person(me, family_dict)
    add_person(sister, family_dict)
    add_person(mom, family_dict)
    add_person(aunt, family_dict)
    add_person(cousin, family_dict)
    add_person(grandpa, family_dict)


    # Save to JSON
    save_family_to_json(family_dict)
    # Down to this line
    loaded_family_dict = load_family_from_json()  # Load from JSON

    # Verify loaded data
    for name, person in loaded_family_dict.items():
        print(f"{name}: {person}")

    print()
    print("------------BFS Search for Family-----------------")
    print()

    print("Search Results for Zeynab:")
    print()
    search_for_person(me, "Sigge")
    search_for_person(me, "Jedd")
    search_for_person(me, "Mimi")
    print()

    print("Search Results for Zekeya:")
    print()
    search_for_person(sister, "Zeynab")
    search_for_person(sister, "Simagne")
    search_for_person(sister, "Jedd")


# Function to create a person project to be added to the family tree
def create_person():
    name = input("Name: ")
    birthdate = input("Date of Birth (DD-MM-YYYY): ")
    gender = input("Gender(F/M): ")
    occupation = input("Occupation: ")
    new_person = Person(name, birthdate, gender, occupation)
    return new_person

# Function to add a new person object to the family tree
def add_person(person, family_dict):
    if person.name not in family_dict:
        family_dict[person.name] = person

# Function to delete a person and all of its relations with other people from family tree
def delete_person(person, family_dict):
    if person.name in family_dict:
        family_dict.pop(person.name)
        for member in family_dict.values():
            for relation, relatives in member.relation_dict.items():
                if person in relatives:
                    member.relation_dict[relation].pop(person)
                    # check if there is any other people under this relation
                    if not member.relation_dict[relation]:
                        del member.relation_dict[relation]
    return family_dict

# Function to print the current family tree
def print_family_dict(family_dict):
    print("The Family:\n")
    for key, value in family_dict.items():
        print(f'{key},{value}')

def search_for_person(first_person, second_person_name):
    """BFS searching the relations between two people in a family tree, take 1 Person object and 1 name as parameter"""
    relationship_stack = deque()
    relationship_stack.append([first_person])

    visited = set()
    visited.add(first_person)
    
    while relationship_stack:  # when the stack is not empty
        curr_path = relationship_stack.popleft()
        last_person = curr_path[-1]
        for relation, relatives in last_person.relation_dict.items():
            for relative in relatives:
                if relative not in visited:
                    visited.add(relative)
                    new_path = curr_path.copy()
                    new_path.append(relative)
                    if relative.name == second_person_name:
                        return print_list_of_person(new_path)
                    relationship_stack.append(new_path)

    print(f"{second_person_name} cannot be founded to connect to {first_person.name}")

# Function to find the relation between two immediate family members
def find_immediate_relation(first_person, second_person):
    for key, value in first_person.relation_dict.items():
        if second_person in value:
            return key
    return None

# Function to print the path from one person to another person (show their relations and the relatives involved)
def print_list_of_person(people_list):
    out_put = ""
    for i in range(len(people_list)-1):
        out_put += people_list[i].name + f"('s {find_immediate_relation(people_list[i],people_list[i+1])})" + "->"
    out_put += people_list[-1].name
    print(out_put)
    print(f"The relationship distance from {people_list[0].name} to {people_list[-1].name} is {len(people_list)-1} step(s).")

def save_family_to_json(family_dict, filename="Zeynab_family_tree.json"):
    """Save the family data to a JSON file."""
    json_data = {
        name: person.to_dict()
        for name, person in family_dict.items()
    }
    with open(filename, "w") as file:
        json.dump(json_data, file, indent=4)
    print(f"Family tree saved to {filename}")

def load_family_from_json(filename="Zeynab_family_tree.json"):
    """Load the family tree data from a JSON file and reconstruct the family graph."""
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

main()
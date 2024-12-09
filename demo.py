from person import Person
from collections import deque
import json

def main():
    family_dict = {}

    # Zeynab could change the people in the demo family, starting from this line
    me = Person("Zeynab", "09-11-1999", "F", "Student")
    mom = Person("Alice", "12-12-1950", "F", "Unknown")
    aunt = Person("Grace", "12-12-1950", "F", "Unknown")
    cousin = Person("Lucy", "12-12-2000", "F", "Student")
    grandpa = Person("Peter", "12-12-1900", "M", "Unknown")

    me.add_relation("mother", mom)
    mom.add_relation("children", me)
    mom.add_relation("father", grandpa)
    mom.add_relation("sibling", aunt)
    aunt.add_relation("father", grandpa)
    aunt.add_relation("sibling", mom)
    aunt.add_relation("children", cousin)
    cousin.add_relation("mother", aunt)
    grandpa.add_relation("children", mom)
    grandpa.add_relation("children", aunt)

    print("Me:\n", me)
    print("Mom:\n", mom)
    print("Aunt:\n", aunt)
    print("Cousin:\n", cousin)
    print("Grandpa:\n", grandpa)

    add_person(me, family_dict)
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
    search_for_person(me, "Alice")
    search_for_person(me, "Peter")
    search_for_person(me, "Lucy")


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
    for member in family_dict.keys():
        for relatives in member.relation_dict.values():
            if person in relatives:
                relatives.remove(person)
    return family_dict

# Function to print the current family tree
def print_family_dict(family_dict):
    print("The Family:\n")
    for key, value in family_dict.items():
        print(f'{key},{value}')

def search_for_person(first_person, second_person):
    """BFS searching the relations between two people in a family tree, take two Person objects as parameter"""
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
                    if relative.name == second_person:
                        return print_list_of_person(new_path)
                    relationship_stack.append(new_path)

    print(f"{second_person} cannot be founded to connect to {first_person.name}")

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
        if i == 0:
            out_put = people_list[0].name + f"('s {find_immediate_relation(people_list[0],people_list[1])})"
        else:
            out_put += "->" + people_list[i].name + f"('s {find_immediate_relation(people_list[i],people_list[i+1])})"
    out_put += "->" + people_list[-1].name
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
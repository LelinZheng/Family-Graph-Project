from person import Person
from collections import deque
import json


def main():
    family_dict = {}
    me = Person("Zeynab", "09-11-1999", "F", "Student")
    mom = Person("Alice", "12-12-1950", "F", "Unknown")
    aunt = Person("Grace", "12-12-1950", "F", "Unknown")
    cousin = Person("Lucy", "12-12-2000", "F", "Student")
    grandpa = Person("Peter", "12-12-1900", "M", "Unknown")
    
    me.add_family_member("mother", mom)
    mom.add_family_member("children", me)
    mom.add_family_member("father", grandpa)
    mom.add_family_member("sibling", aunt)
    aunt.add_family_member("father", grandpa)
    aunt.add_family_member("sibling", mom)
    aunt.add_family_member("children", cousin)
    cousin.add_family_member("mother", aunt)
    grandpa.add_family_member("children", mom)
    grandpa.add_family_member("children", aunt)

    print("Me:\n", me)
    print("Mom:\n", mom)
    print("Aunt:\n", aunt)
    print("Cousin:\n", cousin)
    print("Grandpa:\n", grandpa)
    
    add_person_to_graph(me, family_dict)
    add_person_to_graph(mom, family_dict)
    add_person_to_graph(aunt, family_dict)
    add_person_to_graph(cousin, family_dict)
    add_person_to_graph(grandpa, family_dict)

    print_family_dict(family_dict)

    # Save to JSON
    save_family_to_json(family_dict)
    loaded_family_dict = load_family_from_json()  # Load from JSON

    # Verify loaded data
    for name, person in loaded_family_dict.items():
        print(f"{name}: {person}")

    print()
    print("------------BFS Search for Family-----------------")
    search_for_person(me, family_dict, "Alice")
    search_for_person(me, family_dict, "Peter")
    search_for_person(me, family_dict, "Lucy")


def create_person():
    name = input("Name: ")
    birthdate = input("Date of Birth (DD-MM-YYYY): ")
    gender = input("Gender(F/M): ")
    occupation = input("Occupation: ")
    new_person = Person(name, birthdate, gender, occupation)
    return new_person


def add_person_to_graph(person, family_dict):
    if person.name not in family_dict:
        family_dict[person.name] = person


def print_family_dict(family_dict):
    print("The Family:\n")
    print(family_dict.items())


def search_for_person(me, family_dict, name):
    """BFS searching for certain family member with their name"""
    relationship_stack = deque()
    relationship_stack.append([me])

    visited = set()
    visited.add(me)
    
    while relationship_stack:  # when the stack is not empty
        curr_path = relationship_stack.popleft()
        last_person = curr_path[-1]
        for relation, relatives in last_person.relation_dict.items():
            for relative in relatives:
                if relative not in visited:
                    visited.add(relative)
                    new_path = curr_path.copy()
                    new_path.append(relative)
                    if relative.name == name:
                        return print_list_of_person(new_path)
                    relationship_stack.append(new_path)

    print(f"{name} cannot be founded to connect to {me.name}")


def print_list_of_person(people_list):
    out_put = ""
    for person in people_list:
        out_put += "->" + person.name
    print(out_put)
    print(f"The relationship distance from {people_list[0].name} to {people_list[-1].name} is {len(people_list)-1} steps.")


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
                person.add_family_member(relation, family_dict[relative_name])

    print(f"Family tree loaded from {filename}")
    return family_dict


main()
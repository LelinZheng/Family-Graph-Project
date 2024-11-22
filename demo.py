from person import Person
from collections import deque


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
        family_dict[person.name] = []
    for (relation, relative) in person.relation_dict.items():
        family_dict[person.name].append(relative)


def print_family_dict(family_dict):
    string = ""
    for (center, relatives_list) in family_dict.items():
        string += center + " -> "
        for relatives in relatives_list:
            for relative in relatives:
                string += relative.name + " "
        string += "; "
    print("The Family:\n")
    print(string)


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


main()
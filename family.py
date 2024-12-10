from person import Person
from collections import deque
import json


class Family:
    """A family class"""
    def __init__(self, family_name, family_dict={}):
        """User must enter a name for the family to initialize a family object"""
        self.family_name = family_name
        self.family_dict = family_dict

    def create_person_in_fam(self, name, birthdate, gender, occupation="Unknown", is_alive=True):
        new_person = Person(name, birthdate, gender, occupation, is_alive)
        self.add_person_to_fam(new_person)

    def add_person_to_fam(self, person):
        if person.name not in self.family_dict:
            self.family_dict[person.name] = person
        else:
            print(f"{person.name} already exists in the {self.family_name} family. Please try again.")
            return -1

    def delete_person(self, person_name):
        person = self.convert_name_to_person(person_name)
        if not person:
            print(f"{person_name} does not exist in the {self.family_name} family. Please try again.")
            return -1
        if person.name in self.family_dict:
            del self.family_dict[person.name]
            # remove this person from everybody else' relation_dict
            for member in self.family_dict.values():
                for relation, relatives in list(member.relation_dict.items()):  
                    # makes a copy of it to avoid error when
                    # dictionary changed size during iteration
                    if person in relatives:
                        relatives.remove(person)
                        # check if there is any other people under this relation
                        if not relatives:
                            del member.relation_dict[relation]
        else:
            print(f"{person_name} does not exist in the {self.family_name} family. Please try again.")
            return -1

    def add_relation(self, first_person_name, relationship, second_person_name):
        first_person = self.convert_name_to_person(first_person_name)
        second_person = self.convert_name_to_person(second_person_name)

        if first_person not in self.family_dict.values():
            print(f"{first_person_name} does not exist in the family. Please add them to the {self.family_name} family first.")
            return -1
        if second_person not in self.family_dict.values():
            print(f"{second_person_name} does not exist in the family. Please add them to the {self.family_name} family first.")
            return -1

        if relationship == "sibling" or relationship == "partner":
            first_person.add_relation(relationship, second_person)
            second_person.add_relation(relationship, first_person)
        elif relationship == "mom" or relationship == "dad":
            first_person.add_relation(relationship, second_person)
            second_person.add_relation("children", first_person)
        elif relationship == "children":
            first_person.add_relation(relationship, second_person)
            if first_person.gender == "M":
                second_person.add_relation("father", first_person)
            elif first_person.gender == "F":
                second_person.add_relation("mother", first_person)
            else:
                second_person.add_relation("parent", first_person)  # non-binary parent
        else:
            print(f"{relationship} does not exists as an immediate family relationship. Please try again.")

    def update_person_info(self, person_name, attribute, new_attr):
        person = self.convert_name_to_person(person_name)
        if not person:
            print(f"{person_name} does not exist in the {self.family_name} family. Please try again.")
            return -1
        if attribute == "gender":
            person.update_gender(new_attr)
        elif attribute == "occupation":
            person.update_occupation(new_attr)
        elif attribute == "is_alive":
            person.update_is_alive(new_attr)
        else:
            print(f"{attribute} of {name} does not exists. Please try again.")
            return -1

    def print_family_dict(self):
        print("The Family:\n")
        for key, value in self.family_dict.items():
            print(f'{key},{value}')

    def search_for_person(self, first_person_name, second_person_name):
        """
        BFS searching the relations between two people in a family
        Person Obj, string --> None
        """
        first_person = self.convert_name_to_person(first_person_name)
        if first_person not in self.family_dict.values():
            print(f"{first_person_name} does not exist in the {self.family_name} family. Please try again.")
            return -1
        if second_person_name not in self.family_dict:
            print(f"{second_person_name} does not exist in the {self.family_name} family. Please try again.")
            return -1

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
                            return self.print_list_of_person(new_path)
                        relationship_stack.append(new_path)

        print(f"{second_person_name} cannot be founded to connect to {first_person.name}")

    # Function to find the relation between two immediate family members
    def find_immediate_relation(self, first_person, second_person):
        for key, value in first_person.relation_dict.items():
            if second_person in value:
                return key
        return None

    # Function to print the path from one person to another person (show their relations and the relatives involved)
    def print_list_of_person(self, people_list):
        out_put = ""
        for i in range(len(people_list)-1):
            out_put += people_list[i].name + f"('s {self.find_immediate_relation(people_list[i], people_list[i+1])})" + " -> "
        out_put += people_list[-1].name
        print(out_put)
        print(f"The relationship distance from {people_list[0].name} to {people_list[-1].name} is {len(people_list)-1} step(s).")

    def save_family_to_json(self, filename="Zeynab_family_tree.json"):
        """Save the family data to a JSON file."""
        json_data = {
            name: person.to_dict()
            for name, person in self.family_dict.items()
        }
        with open(filename, "w") as file:
            json.dump(json_data, file, indent=4)
        print(f"Family tree saved to {filename}")

    def convert_name_to_person(self, name):
        for individual_name in self.family_dict:
            if individual_name == name:
                return self.family_dict[individual_name]
        return None

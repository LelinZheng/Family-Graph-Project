from person import Person
from collections import deque
import json
import os


class Family:
    """A family class"""
    def __init__(self, family_name, family_dict=None):
        """
        Initialize a Family object.
        :param family_name: Name of the family
        :param family_dict: Optional dictionary of family members,
        can be loaded from a JSON file
        """
        self.family_name = family_name
        if family_dict:
            self.family_dict = family_dict
        else:
            # Default to an empty dictionary
            self.family_dict = {}

    def create_person_in_fam(self, name, birthdate, gender,
                             occupation="Unknown", is_alive=True):
        """Create a person object in the family"""
        new_person = Person(name, birthdate, gender, occupation, is_alive)
        self.add_person_to_fam(new_person)

    def add_person_to_fam(self, person):
        """Add a person object to the family"""
        if person.name not in self.family_dict:
            self.family_dict[person.name] = person
            print(f"{person.name} is added to the {self.family_name} family.")
        else:
            print(f"{person.name} already exists in the {self.family_name}" +
                  "family. Please try again.")
            return -1

    def delete_person(self, person_name):
        """Remove a person from the family"""
        person = self._convert_name_to_person(person_name)
        if not person:
            return -1

        del self.family_dict[person.name]
        print(f"{person.name} is removed from the {self.family_name} family.")
        # remove this person from everybody else' relation_dict
        for member in self.family_dict.values():
            for relation, relatives in list(member.relation_dict.items()):
                # makes a copy of it to avoid error when
                # dictionary changed size during iteration
                if person in relatives:
                    relatives.remove(person)
                    # check if there is any other people
                    # under this relation
                    if not relatives:
                        del member.relation_dict[relation]

    def add_relation(self, first_person_name, relationship,
                     second_person_name):
        """
        Add relation between two people in the family.
        Both people's relation_dict will be updated.
        """
        first_person = self._convert_name_to_person(first_person_name)
        second_person = self._convert_name_to_person(second_person_name)

        if first_person not in self.family_dict.values():
            print(f"{first_person_name} does not exist in the family." +
                  f"Please add them to the {self.family_name} family first.")
            return -1
        if second_person not in self.family_dict.values():
            print(f"{second_person_name} does not exist in the family." +
                  f" Please add them to the {self.family_name} family first.")
            return -1

        # Adding opposite relationship to the second person
        if relationship == "sibling" or relationship == "partner":
            if first_person.add_relation(relationship, second_person) != -1\
               and\
               second_person.add_relation(relationship, first_person) != -1:
                print(f"Added relationship: {second_person.name} is" +
                      f" {relationship} of {first_person.name}.")
            else:
                return -1
        elif relationship == "mother" or relationship == "father":
            if first_person.add_relation(relationship, second_person) != -1\
               and\
               second_person.add_relation("children", first_person) != -1:
                print(f"Added relationship: {second_person.name} is" +
                      f" {relationship} of {first_person.name}.")
            else:
                return -1
        elif relationship == "children":
            res1 = first_person.add_relation(relationship, second_person)
            if first_person.gender == "M":
                res2 = second_person.add_relation("father", first_person)
            elif first_person.gender == "F":
                res2 = second_person.add_relation("mother", first_person)
            if res1 != -1 and res2 != -1:
                print(f"Added relationship: {second_person.name} is" +
                      f" {relationship} of {first_person.name}.")
            else:
                return -1
        else:
            print(f"{relationship} does not exists as an immediate family" +
                  " relationship. Please try again.")

    def remove_relation(self, first_person_name, relationship,
                        second_person_name):
        """
        Remove relation between two people in the family.
        Both people's relation_dict will be updated.
        """
        first_person = self._convert_name_to_person(first_person_name)
        second_person = self._convert_name_to_person(second_person_name)

        if first_person not in self.family_dict.values():
            print(f"{first_person_name} does not exist in the family." +
                  f"Please add them to the {self.family_name} family first.")
            return -1
        if second_person not in self.family_dict.values():
            print(f"{second_person_name} does not exist in the family." +
                  f" Please add them to the {self.family_name} family first.")
            return -1

        # Removing opposite relationship to the second person
        if relationship == "sibling" or relationship == "partner":
            if first_person.remove_relation(relationship, second_person) != -1\
               and\
               second_person.remove_relation(relationship, first_person) != -1:
                print(f"Removed relationship: {second_person.name} is" +
                      f" NO longer {relationship} of {first_person.name}.")
            else:
                return -1
        elif relationship == "mother" or relationship == "father":
            if first_person.remove_relation(relationship, second_person) != -1\
               and\
               second_person.remove_relation("children", first_person) != -1:
                print(f"Removed relationship: {second_person.name} is" +
                      f" NO longer {relationship} of {first_person.name}.")
            else:
                return -1
        elif relationship == "children":
            res1 = first_person.remove_relation(relationship, second_person)
            if first_person.gender == "M":
                res2 = second_person.remove_relation("father", first_person)
            elif first_person.gender == "F":
                res2 = second_person.remove_relation("mother", first_person)
            if res1 != -1 and res2 != -1:
                print(f"Removed relationship: {second_person.name} is" +
                      f" NO longer {relationship} of {first_person.name}.")
            else:
                return -1
        else:
            print(f"{relationship} does not exists as an immediate family" +
                  " relationship. Please try again.")

    def update_person_info(self, person_name, attribute, new_attr):
        """Update people's information"""
        person = self._convert_name_to_person(person_name)
        if not person:
            return -1
        if attribute == "gender":
            person.update_gender(new_attr)
            print(f"{person.name}'s gender is updated to {new_attr}.")
        elif attribute == "occupation":
            person.update_occupation(new_attr)
            print(f"{person.name}'s occupation is updated to {new_attr}.")
        elif attribute == "is_alive":
            if new_attr == "Y":
                person.update_is_alive(True)
                print(f"{person.name}'s status is updated to alive.")
            else:
                person.update_is_alive(False)
                print(f"{person.name}'s status is updated to deceased.")
        else:
            print(f"{attribute} of {person_name} does not exists." +
                  "Please try again.")
            return -1

    def print_family_dict(self):
        """Print the family dict in a string format"""
        print(f"The {self.family_name} Family:")
        string = ""
        for person_name in self.family_dict:
            string += person_name + ", "
        if not string:
            string = "None"
        else:
            string = string.rstrip(", ")
        print(string)

    def get_person_info(self, person_name):
        """Print person info in a string format"""
        person = self._convert_name_to_person(person_name)
        if not person:
            return -1
        print(person)

    def show_immediate_family(self, person_name):
        """Print person's immediate family in a string format"""
        person = self._convert_name_to_person(person_name)
        if not person:
            return -1
        print(f"Immediate family members for {person_name}:")
        family_str = {relation: [relative.name for relative in relatives]
                      for relation, relatives in person.relation_dict.items()}
        if not family_str:
            family_str = " None"

        for relation, relatives in family_str.items():
            relatives_list = ', '.join(relatives)
            print(f"{relation.capitalize()}: {relatives_list}")

    def search_for_person(self, first_person_name, second_person_name):
        """
        BFS searching the relations between two people in a family
        Person Obj, string --> None
        """
        first_person = self._convert_name_to_person(first_person_name)
        if first_person not in self.family_dict.values():
            print(f"{first_person_name} does not exist in the" +
                  f" {self.family_name} family. Please try again.")
            return -1
        if second_person_name not in self.family_dict:
            print(f"{second_person_name} does not exist in the" +
                  f" {self.family_name} family. Please try again.")
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
                            return self._print_list_of_person(new_path)
                        relationship_stack.append(new_path)

        print(f"{second_person_name} cannot be founded to connect to " +
              f" {first_person.name}")
        return -1

    def _find_immediate_relation(self, first_person, second_person):
        """Helper function to find the relation for two immediate members"""
        for key, value in first_person.relation_dict.items():
            if second_person in value:
                return key
        return None

    def _print_list_of_person(self, people_list):
        """
        Helper function
        Print the path from one person to another person
        And show their relations and the relatives involved
        """
        out_put = ""
        for i in range(len(people_list)-1):
            out_put += people_list[i].name +\
                       f"('s {self._find_immediate_relation(
                        people_list[i], people_list[i+1])})" + " -> "
        out_put += people_list[-1].name
        print(out_put)
        print(f"The relationship distance from {people_list[0].name} to" +
              f" {people_list[-1].name} is {len(people_list)-1} step(s).")

    def save_family_to_json(self, filename):
        """
        Save the family data to a JSON file.
        The file name must be in a format as 'Zeynab_family_tree.json'
        """
        def save_json_file(filename):
            json_data = {
                name: person.to_dict()
                for name, person in self.family_dict.items()
            }
            with open(filename, "w") as file:
                json.dump(json_data, file, indent=4)
            print(f"Family tree saved to {filename}")

        # Validate file name format
        if not filename.endswith("_family_tree.json"):
            print("Error: Filename must be in the format" +
                  " 'Name_family_tree.json'.")
            return -1

        # Check if the file already exists
        if os.path.exists(filename):
            print(f"File '{filename}' already exists." +
                  " Are you sure to overwrite it? (Y/N)")
            ans = input().strip().upper()
            while ans not in {"Y", "N"}:
                ans = input("Please enter Y/N only: ").strip().upper()
            if ans == "Y":
                self._save_json_file(filename)
                return
            else:
                print(f"The {self.family_name} family did not save." +
                      " Please use a new file name to save it.")
                return -1

        self._save_json_file(filename)

    def _save_json_file(self, filename):
        """Helper method to save family data to JSON."""
        json_data = {
            name: person.to_dict()
            for name, person in self.family_dict.items()
        }
        with open(filename, "w") as file:
            json.dump(json_data, file, indent=4)
        print(f"Family tree saved to {filename}.")

    def _convert_name_to_person(self, name):
        """Helper function to return a person object if in family"""
        for individual_name in self.family_dict:
            if individual_name == name:
                return self.family_dict[individual_name]
        print(f"{name} does not exist in the {self.family_name}" +
              " family. Please try again.")
        return

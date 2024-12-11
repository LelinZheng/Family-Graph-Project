from datetime import datetime


class Person:
    def __init__(self, name, birthdate, gender, occupation="Unknown",
                 is_alive=True):
        """
        Initialize the class Person, which stores information of a person
        in the family tree. The information includes the person's name,
        date of birth, gender, occupation (which is set as unknown by default),
        also a boolean attribute to indicate whether the person is alive.
        """
        self.name = name
        self.birthdate = birthdate  # DD-MM-YYYY
        self.gender = gender
        self.occupation = occupation
        self.relation_dict = {}
        # key is the relation like "mother", value is a list of person object
        self.is_alive = is_alive

    @property
    def age(self):
        """
        Function to set the person's age by subtracting the current year
        by the year of birth,
        so that the program updates the age by itself
        """
        birthyear = int(self.birthdate.split("-")[-1])
        current_year = datetime.now().year
        age = current_year - birthyear
        return age

    def update_gender(self, new_gender):
        self.gender = new_gender

    def update_is_alive(self, new_is_alive):
        self.is_alive = True if new_is_alive else False

    def update_occupation(self, new_occupation):
        self.occupation = new_occupation

    def add_relation(self, relation, new_person):
        """add a relation of a family member using person object"""
        for rel, person_list in self.relation_dict.items():
            if new_person in person_list:
                print(f"{new_person.name} is already related to {self.name}." +
                      f"{new_person.name} is {self.name} 's {rel}")
                return -1

        if relation not in self.relation_dict:
            self.relation_dict[relation] = [new_person]
        else:
            self.relation_dict[relation].append(new_person)

    def remove_relation(self, relation, new_person):
        """remove a relation of a family member using person object"""
        if relation not in self.relation_dict:
            print(f"{self.name} has no {relation}. Please try again.")
            return -1
        else:
            if new_person not in self.relation_dict[relation]:
                print(f"{new_person.name} is NOT {relation} of {self.name}." +
                      "Please try again.")
                return -1
            self.relation_dict[relation].remove(new_person)

            # if there is nobody else under this relation
            if not self.relation_dict[relation]:
                del self.relation_dict[relation]

    def __str__(self):
        """Store the person object's information in string for printing"""
        string = ""
        for (relation, people) in self.relation_dict.items():
            string += " " + relation.capitalize() + ":"
            for person in people:
                string += " " + person.name
            string += ";"
        if not string:
            string = " None"
        birthday = self.birthdate.split("-")[0]
        birthmonth = int(self.birthdate.split("-")[1])
        month_list = {1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr",
                      5: "May", 6: "June", 7: "July", 8: "Aug",
                      9: "Sep", 10: "Oct", 11: "Nov", 12: "Dec"}
        month = month_list[birthmonth]
        if self.is_alive:
            return "Name: " + self.name + ", Gender: " + self.gender +\
                   ", Birthday: " + month + " " + birthday + ", Age: " +\
                    str(self.age) + ", Occupation: " + self.occupation +\
                    ", Immediate Family Relations:" + string
        else:
            return "Name: " + self.name + " (Deceased)" + ", Gender: " +\
                   self.gender + ", Birthday: " + month + " " + birthday +\
                   ", Age: " + str(self.age) + ", Occupation: " +\
                   self.occupation + ", Immediate Family Relations:" +\
                   string

    def to_dict(self):
        """Convert the Person object to a dictionary for JSON serialization."""
        return {
            "name": self.name,
            "birthdate": self.birthdate,
            "gender": self.gender,
            "occupation": self.occupation,
            "is_alive": self.is_alive,
            "relation_dict": {
                relation: [relative.name for relative in relatives]
                for relation, relatives in self.relation_dict.items()
            }
        }

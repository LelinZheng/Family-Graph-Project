from datetime import datetime

class Person:
    def __init__(self, name, birthdate, gender, occupation="Unknown", is_alive=True):
        """
         Initialize the class Person, which stores information of a person in the family tree.
        The information includes the person's name, date of birth, gender, occupation (which is
        set as unknown by default), also a boolean attribute to indicate whether the person is alive.
        """
        self.name = name
        self.birthdate = birthdate  # DD-MM-YYYY
        self.gender = gender
        self.occupation = occupation
        self.relation_dict = {}  # key is the relation like "mother", values a list of person object,
        self.is_alive = is_alive

    @property
    def age(self):
        """
        Function to set the person's age by subtracting the current year by the year of birth
        so that the program updates the age by itself
        """
        birthyear = int(self.birthdate.split("-")[-1])
        current_year = datetime.now().year
        age = current_year - birthyear
        return age

    # Function to update the person's gender
    def update_gender(self, new_gender):
        self.gender = new_gender

    # Function to update the person's living status, new_is_alive should be a boolean statement
    def update_is_alive(self, new_is_alive):
        self.is_alive = True if new_is_alive else False

    # Function to update the person's occupation
    def update_occupation(self, new_occupation):
        self.occupation = new_occupation

    # Function to add a relation of a family member
    def add_relation(self, relation, new_person):
        # Using a person object to add
        if relation not in self.relation_dict:
            self.relation_dict[relation] = [new_person]
        else:
            self.relation_dict[relation].append(new_person)
    
    # def search_family_relation(self, target_person_name):
    #     """Searching for person that match this name"""
    #     for (relation, people) in self.relation_dict.items():
    #         for person in people:
    #             if target_person_name == person.name:
    #                 return person

    # Store the person object's information in string for printing
    def __str__(self):
        string = ""
        for (relation, people) in self.relation_dict.items():
            string += relation + ": "
            for person in people:
                string += person.name  + " "
            string += " ; "
        birthday = self.birthdate.split("-")[0]
        birthmonth = int(self.birthdate.split("-")[1])
        month_list = {1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr", 
                      5: "May", 6: "June", 7: "July", 8: "Aug",
                      9: "Sep", 10: "Oct", 11: "Nov", 12: "Dec"}
        month = month_list[birthmonth]
        return "Name: " + self.name + ", Gender: " + self.gender + ", Birthday: " +\
            month + " " + birthday + " , Age: " + str(self.age) + ", Occupation: " +\
            self.occupation + ", Is Alive: " + str(self.is_alive) + " , Immediate Family Relations: " +\
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

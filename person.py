from datetime import datetime

class Person:
    def __init__(self, name, birthdate, gender, occupation):
        self.name = name
        self.birthdate = birthdate #DD-MM-YYYY
        self.gender = gender
        self.occupation = occupation
        self.relation_dict = {} # key is the relation like "mother", values is a list of person object
    
    @property
    def age(self):
        birthyear = int(self.birthdate.split("-")[-1])
        current_year = datetime.now().year
        age = current_year - birthyear
        return age
    
    def update_gender(self, new_gender):
        self.gender = new_gender
    
    def update_occupation(self, new_occupation):
        self.occupation = new_occupation
    
    def add_family_member(self, relation, new_person):
        # Using a person object to add
        if relation not in self.relation_dict:
            self.relation_dict[relation] = [new_person]
        else:
            self.relation_dict[relation].append(new_person)
    
    def search_family_relation(self, target_person_name):
        """Searching for person that match this name"""
        for (relation, people) in self.relation_dict.items():
            for person in people:
                if target_person_name == person.name:
                    return person
    
    def __str__(self):
        string = ""
        for (relation, people) in self.relation_dict.items():
            string += relation + ": "
            for person in people:
                string += person.name  # + " "
            string += "; "
        
        return "Name: " + self.name + " , Age: " + str(self.age) + " , Relation: " + string
    
    def __hash__(self):
        return hash((self.name))

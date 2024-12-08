from person import Person
"""
It may become a class of a Family Graph, this will let user define their own family
"""

def main():
    family_dict = {}
    print("Create me: ")
    me = create_person()
    print("Create mom: ")
    mom = create_person()
    print("Create grandpa: ")
    grandpa = create_person()
    
    me.add_relation("mother", mom)
    mom.add_relation("children", me)
    mom.add_relation("father", grandpa)
    grandpa.add_relation("children", mom)

    print("Me: \n", me)
    print("Mom: \n", mom)
    print("Grandpa: \n", grandpa)

def create_person():
    name = input("Name: ")
    birthdate = input("Date of Birth (DD-MM-YYYY): ")
    gender = input("Gender(F/M): ")
    occupation = input("Occupation: ")
    new_person = Person(name, birthdate, gender, occupation)
    return new_person

def add_relation(relation, person):
    pass


main()
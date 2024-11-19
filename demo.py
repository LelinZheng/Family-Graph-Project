from person import Person

def main():
    family_dict = {}
    me = Person("Zeynab", "12-12-2000", "F", "Student")
    mom = Person("Alice", "12-12-1950", "F", "Unknown")
    aunt = Person("Grace", "12-12-1950", "F", "Unknown")
    grandpa = Person("Peter", "12-12-1900", "M", "Unknown")
    
    me.add_family_member("mother", mom)
    mom.add_family_member("children", me)
    mom.add_family_member("father", grandpa)
    mom.add_family_member("sibling", aunt)
    aunt.add_family_member("father", grandpa)
    aunt.add_family_member("sibling", mom)
    grandpa.add_family_member("children", mom)
    grandpa.add_family_member("children", aunt)

    print("Me:\n", me)
    print("Mom:\n", mom)
    print("Aunt:\n", aunt)
    print("Grandpa:\n", grandpa)
    
    add_person_to_graph(me, family_dict)
    add_person_to_graph(mom, family_dict)
    add_person_to_graph(aunt, family_dict)
    add_person_to_graph(grandpa, family_dict)

    print_family_dict(family_dict)


def create_person():
    name = input("Name: ")
    birthdate = input("Date of Birth (DD-MM-YYYY): ")
    gender = input("Gender(F/M): ")
    gender = input("Occupation: ")
    new_person = Person(name, birthdate, gender, occupation="Unknown")
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


main()
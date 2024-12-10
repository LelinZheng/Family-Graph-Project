"""
Create a drop-down menu:
1. Create a family
2. Read the data about a family from a json file

after the user provides a family tree
1. add a person and their relations to a family tree
2. delete a person and all their relations from a family tree
3. update a person's information
4. search the relationship (path) between two people by their names

after the user is done with all the functions
save the data into a new json file or the old json file
"""
from family import Family


def main():
    pass


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
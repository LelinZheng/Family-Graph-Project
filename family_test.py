from family import Family
from person import Person


def test_constructor():
    family = Family("British Royal")
    assert (family.family_name == "British Royal" and
            family.family_dict == {})


def test_create_person_in_fam():
    family = Family("British Royal")
    family.create_person_in_fam("King Charles III",
                                "14-11-1948", "M", "King", True)
    assert (len(family.family_dict) == 1)
    family.create_person_in_fam("Queen Elizabeth II",
                                "21-04-1926", "F", "Queen", False)
    assert (len(family.family_dict) == 2)
    family.create_person_in_fam("King Charles III",
                                "14-11-1948", "M", "King", True)
    assert (len(family.family_dict) == 2)


def test_add_person_to_fam():
    family = Family("British Royal")
    family.add_person_to_fam(Person("King Charles III",
                                    "14-11-1948", "M", "King", True))
    assert (len(family.family_dict) == 1)
    family.add_person_to_fam(Person("King Charles III",
                                    "14-11-1948", "M", "King", True))
    assert (len(family.family_dict) == 1)


def test_delete_person():
    family = Family("British Royal")
    family.create_person_in_fam("King Charles III",
                                "14-11-1948", "M", "King", True)
    family.delete_person("King Charles III")
    assert (len(family.family_dict) == 0)
    assert (family.delete_person("King Charles III") == -1)

    family.create_person_in_fam("Queen Elizabeth II",
                                "21-04-1926", "F", "Queen", False)
    family.create_person_in_fam("King Charles III",
                                "14-11-1948", "M", "King", True)
    family.add_relation("King Charles III", "mother", "Queen Elizabeth II")
    assert (len(family.family_dict["King Charles III"].relation_dict) == 1)
    family.delete_person("King Charles III")
    assert (len(family.family_dict["Queen Elizabeth II"].relation_dict) == 0)


def test_add_relation():
    family = Family("British Royal")
    family.create_person_in_fam("Queen Elizabeth II",
                                "21-04-1926", "F", "Queen", False)
    family.create_person_in_fam("King Charles III",
                                "14-11-1948", "M", "King", True)
    assert (family.add_relation("Prince Edward", "mother",
            "Queen Elizabeth II") == -1)
    assert (family.add_relation("King Charles III", "children",
            "Prince William") == -1)

    family.add_relation("King Charles III", "mother", "Queen Elizabeth II")
    assert (len(family.family_dict["King Charles III"
                                   ].relation_dict["mother"]) == 1)
    assert (len(family.family_dict["Queen Elizabeth II"
                                   ].relation_dict["children"]) == 1)

    family.create_person_in_fam("Prince William",
                                "21-06-1982", "M", "Prince")
    family.create_person_in_fam("Kate Middleton",
                                "09-01-1982", "F", "Princess")
    family.create_person_in_fam("Prince Harry", "15-09-1984", "M", "Prince")
    family.add_relation("Prince William", "partner", "Kate Middleton")
    family.add_relation("King Charles III", "children", "Prince William")
    family.add_relation("King Charles III", "children", "Prince Harry")
    family.add_relation("Prince William", "sibling", "Prince Harry")
    assert (len(family.family_dict["Kate Middleton"
                                   ].relation_dict["partner"]) == 1)
    assert (len(family.family_dict["Prince William"
                                   ].relation_dict["partner"]) == 1)
    assert (len(family.family_dict["Prince William"
                                   ].relation_dict["father"]) == 1)
    assert (len(family.family_dict["Prince William"
                                   ].relation_dict["sibling"]) == 1)
    assert (len(family.family_dict["King Charles III"
                                   ].relation_dict["children"]) == 2)
    family.add_relation("Prince William", "partner", "Prince Harry")
    assert (len(family.family_dict["Prince William"
                                   ].relation_dict["partner"]) == 1)
    family.add_relation("Prince William", "friend", "Prince Harry")
    assert (len(family.family_dict["Prince William"].relation_dict) == 3)


def test_update_person_info():
    family = Family("British Royal")
    assert (family.update_person_info("Queen Elizabeth II",
                                      "occupation", "Princess") == -1)
    family.create_person_in_fam("Queen Elizabeth II",
                                "21-04-1926", "F", "Queen")
    assert (family.family_dict["Queen Elizabeth II"].is_alive)
    family.update_person_info("Queen Elizabeth II", "is_alive", False)
    assert (not family.family_dict["Queen Elizabeth II"].is_alive)
    family.update_person_info("Queen Elizabeth II", "gender", "M")
    assert (family.family_dict["Queen Elizabeth II"].gender == "M")
    family.update_person_info("Queen Elizabeth II", "occupation", "Princess")
    assert (family.family_dict["Queen Elizabeth II"].occupation == "Princess")
    assert (family.update_person_info("Queen Elizabeth II",
                                      "birthdate", "21-04-1926") == -1)


def test_get_person_info():
    family = Family("British Royal")
    assert (family.get_person_info("Queen Elizabeth II") == -1)


def test_show_immediate_family():
    family = Family("British Royal")
    assert (family.show_immediate_family("Queen Elizabeth II") == -1)


def test_search_for_person():
    family = Family("British Royal")
    family.create_person_in_fam("Queen Elizabeth II",
                                "21-04-1926", "F", "Queen", False)
    family.create_person_in_fam("Prince William", "21-06-1982", "M", "Prince")
    family.create_person_in_fam("Kate Middleton",
                                "09-01-1982", "F", "Princess")
    family.create_person_in_fam("Prince Harry", "15-09-1984", "M", "Prince")
    family.add_relation("Prince William", "partner", "Kate Middleton")
    family.add_relation("Prince William", "mother", "Queen Elizabeth II")
    assert (family.search_for_person("Prince William", "Prince Harry") == -1)
    assert (family.search_for_person("Prince William", "Prince Mary") == -1)


def test_find_immediate_relation():
    family = Family("British Royal")
    family.create_person_in_fam("Queen Elizabeth II",
                                "21-04-1926", "F", "Queen", False)
    family.create_person_in_fam("Prince William",
                                "21-06-1982", "M", "Prince")
    family.create_person_in_fam("Kate Middleton",
                                "09-01-1982", "F", "Princess")
    family.create_person_in_fam("Prince Harry", "15-09-1984", "M", "Prince")
    family.add_relation("Prince William", "partner", "Kate Middleton")
    assert (not family._find_immediate_relation
            (family.family_dict["Prince William"],
             family.family_dict["Prince Harry"]))
    assert (family._find_immediate_relation(
            family.family_dict["Prince William"],
            family.family_dict["Kate Middleton"]) == "partner")


def test_save_family_to_json():
    family = Family("British Royal")
    assert (family.save_family_to_json("abcd") == -1)

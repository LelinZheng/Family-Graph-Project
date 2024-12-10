from person import Person


def test_constructor():
    person = Person("Amy", "02-03-1997", "M", "accountant")
    assert (person.name == "Amy" and
            person.birthdate == "02-03-1997" and
            person.gender == "M" and
            person.occupation == "accountant" and
            person.relation_dict == {} and
            person.is_alive is True)


def test_age():
    person = Person("Amy", "02-03-1997", "M", "accountant")
    assert (person.age == 27)


def test_update_gender():
    person = Person("Amy", "02-03-1997", "M", "accountant")
    person.update_gender("F")
    assert (person.gender == "F")


def test_update_is_alive():
    person = Person("Amy", "02-03-1997", "M", "accountant", False)
    person.update_is_alive(True)
    assert (person.is_alive)


def test_update_occupation():
    person = Person("Amy", "02-03-1997", "M")
    person.update_occupation("doctor")
    assert (person.occupation == "doctor")


def test_add_relation():
    amy = Person("Amy", "02-03-1997", "F")
    jack = Person("Jack", "02-03-1999", "M")
    mike = Person("Mike", "02-03-1995", "M")
    cooper = Person("Cooper", "02-03-1980", "M")
    amy.add_relation("sibling", jack)
    assert (amy.relation_dict["sibling"] == [jack])
    assert (amy.add_relation("mother", jack) == -1 and
            len(amy.relation_dict) == 1)
    amy.add_relation("sibling", mike)
    assert (amy.relation_dict["sibling"] == [jack, mike])
    amy.add_relation("father", cooper)
    assert (amy.relation_dict["father"] == [cooper])


def test_str():
    amy = Person("Amy", "02-03-1997", "F")
    jack = Person("Jack", "02-03-1999", "M")
    cooper = Person("Cooper", "02-03-1980", "M")
    amy.add_relation("sibling", jack)
    amy.add_relation("father", cooper)
    assert (str(amy) == "Name: Amy, Gender: F, Birthday: " +
                        "Mar 02, Age: 27, Occupation: Unknown, " +
                        "Immediate Family Relations: sibling: Jack; " +
                        "father: Cooper;")
    amy = Person("Amy", "02-03-1997", "F", "doctor", False)
    assert (str(amy) == "Name: Amy (Deceased), Gender: F, Birthday: " +
                        "Mar 02, Age: 27, Occupation: doctor, " +
                        "Immediate Family Relations: None")


def test_to_dict():
    amy = Person("Amy", "02-03-1997", "F")
    jack = Person("Jack", "02-03-1999", "M")
    cooper = Person("Cooper", "02-03-1980", "M")
    amy.add_relation("sibling", jack)
    amy.add_relation("father", cooper)
    assert (amy.to_dict() == {
            "name": "Amy",
            "birthdate": "02-03-1997",
            "gender": "F",
            "occupation": "Unknown",
            "is_alive": True,
            "relation_dict": {
                "sibling": ["Jack"],
                "father": ["Cooper"]
            }
            })

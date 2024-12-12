from family import Family
import graph

def build_kardashian_family():
    """
    This is a program to initialize a demo file of Kardashian family
    and make a json file
    """

    family = Family("Kardashian")
    family.create_person_in_fam("Kim Kardashian", "21-10-1980", "F", "model")
    family.create_person_in_fam("Kris Jenner", "05-11-1955", "F", "manager")
    family.create_person_in_fam("Robert Kardashian", "22-02-1944", "M", "lawyer", False)
    family.create_person_in_fam("Kourtney Kardashian", "18-04-1979", "F", "businesswoman")
    family.create_person_in_fam("Khloe Kardashian", "27-06-1984", "F", "businesswoman")
    family.create_person_in_fam("Rob Kardashian", "17-03-1987", "M", "businessman")
    family.create_person_in_fam("Kendall Jenner", "03-11-1995", "F", "model")
    family.create_person_in_fam("Kylie Jenner", "10-08-1997", "F", "businesswoman")
    family.create_person_in_fam("Caitlyn (Bruce) Jenner", "28-10-1949", "M->F", " athlete")

    family.create_person_in_fam("North West", "15-06-2013", "F")
    family.create_person_in_fam("Saint West", "05-12-2015", "M")
    family.create_person_in_fam("Chicago West", "15-01-2018", "F")
    family.create_person_in_fam("Psalm West", "09-05-2019", "M")
    family.create_person_in_fam("Mason Disick", "14-12-2009", "M")
    family.create_person_in_fam("Penelope Disick", "05-12-2015", "F")
    family.create_person_in_fam("Reign Disick", "15-01-2018", "M")
    family.create_person_in_fam("True Thompson", "12-04-2018", "F")
    family.create_person_in_fam("Dream Kardashian", "10-11-2016", "F")
    family.create_person_in_fam("Stormi Webster", "01-02-2018", "F")
    family.create_person_in_fam("Aire Webster", "02-02-2022", "M")

    family.create_person_in_fam("Kanye West", "08-06-1977", "M", "rapper")
    family.create_person_in_fam("Scott Disick", "26-05-1983", "M", "businessman")
    family.create_person_in_fam("Travis Barker ", "14-11-1975", "M", "musician")
    family.create_person_in_fam("Lamar Odom", "06-11-1979", "M", "NBA player")
    family.create_person_in_fam("Tristan Thompson", "13-03-1991", "M", "NBA player")
    family.create_person_in_fam("Blac Chyna", "11-05-1988", "F", "model")
    family.create_person_in_fam("Travis Scott", "30-04-1991", "M", "musician")

    # Parent-child relationships for the children (adding to both parents)
    # Kim Kardashian and Kanye West's children
    family.add_relation("Kim Kardashian", "children", "North West")
    family.add_relation("Kanye West", "children", "North West")
    family.add_relation("Kim Kardashian", "children", "Saint West")
    family.add_relation("Kanye West", "children", "Saint West")
    family.add_relation("Kim Kardashian", "children", "Chicago West")
    family.add_relation("Kanye West", "children", "Chicago West")
    family.add_relation("Kim Kardashian", "children", "Psalm West")
    family.add_relation("Kanye West", "children", "Psalm West")
    family.add_relation("North West", "sibling", "Saint West")
    family.add_relation("North West", "sibling", "Chicago West")
    family.add_relation("North West", "sibling", "Psalm West")
    family.add_relation("Saint West", "sibling", "Chicago West")
    family.add_relation("Saint West", "sibling", "Psalm West")
    family.add_relation("Chicago West", "sibling", "Psalm West")

    # Kourtney Kardashian and Scott Disick's children
    family.add_relation("Kourtney Kardashian", "children", "Mason Disick")
    family.add_relation("Scott Disick", "children", "Mason Disick")
    family.add_relation("Kourtney Kardashian", "children", "Penelope Disick")
    family.add_relation("Scott Disick", "children", "Penelope Disick")
    family.add_relation("Kourtney Kardashian", "children", "Reign Disick")
    family.add_relation("Scott Disick", "children", "Reign Disick")
    family.add_relation("Mason Disick", "sibling", "Penelope Disick")
    family.add_relation("Mason Disick", "sibling", "Reign Disick")
    family.add_relation("Penelope Disick", "sibling", "Reign Disick")

    # Khloé Kardashian and Tristan Thompson's child
    family.add_relation("Khloe Kardashian", "children", "True Thompson")
    family.add_relation("Tristan Thompson", "children", "True Thompson")

    # Rob Kardashian and Blac Chyna's child
    family.add_relation("Rob Kardashian", "children", "Dream Kardashian")
    family.add_relation("Blac Chyna", "children", "Dream Kardashian")

    # Kylie Jenner and Travis Scott's children
    family.add_relation("Kylie Jenner", "children", "Stormi Webster")
    family.add_relation("Travis Scott", "children", "Stormi Webster")
    family.add_relation("Kylie Jenner", "children", "Aire Webster")
    family.add_relation("Travis Scott", "children", "Aire Webster")
    family.add_relation("Stormi Webster", "sibling", "Aire Webster")
    family.add_relation("Stormi Webster", "mother", "Kylie Jenner")
    family.add_relation("Stormi Webster", "father", "Travis Scott")
    family.add_relation("Aire Webster", "mother", "Kylie Jenner")
    family.add_relation("Aire Webster", "father", "Travis Scott")

    # Partner relationships
    family.add_relation("Kris Jenner", "partner", "Robert Kardashian")
    family.add_relation("Kris Jenner", "partner", "Caitlyn (Bruce) Jenner")
    family.add_relation("Kim Kardashian", "partner", "Kanye West")
    family.add_relation("Kourtney Kardashian", "partner", "Scott Disick")
    family.add_relation("Kourtney Kardashian", "partner", "Travis Barker ")
    family.add_relation("Khloe Kardashian", "partner", "Lamar Odom")
    family.add_relation("Khloe Kardashian", "partner", "Tristan Thompson")
    family.add_relation("Rob Kardashian", "partner", "Blac Chyna")
    family.add_relation("Kylie Jenner", "partner", "Travis Scott")

    # Sibling relationships
    family.add_relation("Kim Kardashian", "sibling", "Kourtney Kardashian")
    family.add_relation("Kim Kardashian", "sibling", "Khloe Kardashian")
    family.add_relation("Kim Kardashian", "sibling", "Rob Kardashian")
    family.add_relation("Kim Kardashian", "sibling", "Kendall Jenner")
    family.add_relation("Kim Kardashian", "sibling", "Kylie Jenner")

    family.add_relation("Kourtney Kardashian", "sibling", "Khloe Kardashian")
    family.add_relation("Kourtney Kardashian", "sibling", "Rob Kardashian")
    family.add_relation("Kourtney Kardashian", "sibling", "Kendall Jenner")
    family.add_relation("Kourtney Kardashian", "sibling", "Kylie Jenner")

    family.add_relation("Khloe Kardashian", "sibling", "Rob Kardashian")
    family.add_relation("Khloe Kardashian", "sibling", "Kendall Jenner")
    family.add_relation("Khloe Kardashian", "sibling", "Kylie Jenner")

    family.add_relation("Rob Kardashian", "sibling", "Kendall Jenner")
    family.add_relation("Rob Kardashian", "sibling", "Kylie Jenner")

    family.add_relation("Kendall Jenner", "sibling", "Kylie Jenner")

    # Parent-child relationships
    family.add_relation("Kim Kardashian", "mother", "Kris Jenner")
    family.add_relation("Kourtney Kardashian", "mother", "Kris Jenner")
    family.add_relation("Khloe Kardashian", "mother", "Kris Jenner")
    family.add_relation("Rob Kardashian", "mother", "Kris Jenner")
    family.add_relation("Kendall Jenner", "mother", "Kris Jenner")
    family.add_relation("Kylie Jenner", "mother", "Kris Jenner")

    family.add_relation("Kim Kardashian", "father", "Robert Kardashian")
    family.add_relation("Kourtney Kardashian", "father", "Robert Kardashian")
    family.add_relation("Khloe Kardashian", "father", "Robert Kardashian")
    family.add_relation("Rob Kardashian", "father", "Robert Kardashian")

    family.add_relation("Kendall Jenner", "father", "Caitlyn (Bruce) Jenner")
    family.add_relation("Kylie Jenner", "father", "Caitlyn (Bruce) Jenner")

    graph.create_graph(family)

    # family.save_family_to_json("Kardashian_family_tree.json")

    family.search_for_person("North West", "Lamar Odom")
    family.print_family_dict()
    family.get_person_info("North West")
    family.show_immediate_family("North West")


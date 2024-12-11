"""
Create a drop-down menu:
1. Create a family
2. Read the data about a family from a json file

after the user provides a family tree
1. add a person and their relations to a family tree
2. delete a person and all their relations from a family tree
3. update a person's information
4. search the relationship (path) between two people by their names
5. search up a person's information
6. get a graph of the family

after the user is done with all the functions
save the data into a new json file or the old json file
"""
from menu import Menu


def main():
    # Welcome Message
    print("===================================")
    print("     Family Tree Management")
    print("===================================")
    print("Build and visualize your family tree with ease!")
    print()

    menu = Menu()
    menu.run()


main()

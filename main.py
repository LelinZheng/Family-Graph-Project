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
import menu
from menu import loop_main_menu

def main():
    try:
        user_family = menu.get_user_family()
        loop_main_menu(user_family)

    except Exception as err:
        print(f"An error occurred: {err}. Please restart the program and try again.")

if __name__ == "__main__":
    main()

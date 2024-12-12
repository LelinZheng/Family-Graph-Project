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
import demo_kardashian_family
import demo_zeynab_family


def main():
    try:
        # demo_kardashian_family.build_kardashian_family()
        # demo_zeynab_family.build_zeynab_family()
        user_family = menu.get_user_family()
        menu.loop_main_menu(user_family)

    except Exception as err:
        print(f"An error occurred: {err}. Please restart the program and try again.")


if __name__ == "__main__":
    main()

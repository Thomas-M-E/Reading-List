from reading_list import repo
from pathlib import Path
import random

"""
TODO: Make it so the book info is hashed with a password so when uploaded to
github it is not open to everyone
or for now add the file to git ignore
TODO: Add films and TV
TODO: Add the ability to add/edit/remove books

TODO: Change this back to a view class
This is the classic MVC example
Perhaps try with SQLite instead of csv and make the interface be able
to handle both

TODO: Hopefully the hashing of the list also obscures the massive list of things infront
of you
TODO: Obviously need to prioritise books that I have already purchased too

"""
class IncorrectInputError(Exception):
    ...

def main():
    condition = True
    while(condition):
        response = input(
            "Would you like to\n"
            "\t1. select a book\n"
            "\t2. edit the database\n"
            "\t3. Exit program\n"
            "Please enter the number of your selection.\n"
        )
        if response not in {"1", "2", "3"}:
            print("Please input either 1, 2 or 3")
            continue
        condition = False
        menus = {"1": select_book_menu, "2": edit_data_menu, "3": exit_program}
        menus[response]()

def select_book_menu():
    while(condition):
        response = input("Do you want a random choice or the highest priority? R or H")
        if response not in {"R", "H"}:
            print("Please input either R or H")
            continue
        condition = False
    
    reading_list_path = Path(__file__).parent / "reading_list.csv"
    book_repo = repo.BookRepo(reading_list_path)
    response_map = {"R": random_select, "H": priority_select}
    choice = response_map[response](repo)
    print(choice)

def edit_data_menu():
    raise NotImplementedError

def exit_program():
    raise NotImplementedError

def random_select(repo):
    raise NotImplementedError
    # list = repo
    # return random.choice(list)

def priority_select(repo):
    raise NotImplementedError
    # list = repo
    # return random.choice(list)
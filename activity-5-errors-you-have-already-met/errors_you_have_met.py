"""
Five errors you have already met this fortnight.

Each one is in its own function. Call them one at a time by
uncommenting the line at the bottom, and read the traceback
properly each time before moving on.
"""

grades = {"Elara": 85, "Kwame": 92}
fleet = [{"id": "B-104"}, {"id": "B-107"}]


def missing_key():

    try:
        print(grades["Aisha"])
    except Exception as e:
        print(f"Student {e} not found")

def past_the_end():
    print(fleet[5])


def text_that_is_not_a_number():
    try:
        print(int("forty"))
    except ValueError as e:
        print(f"ValueError:{e}")
        

def adding_apples_to_oranges():
    print(int("82") + 141)


def file_that_is_not_there():
    with open("nowhere.txt", "r") as f:
        print(f.read())


missing_key()
# past_the_end()
text_that_is_not_a_number()
adding_apples_to_oranges()
# file_that_is_not_there()

from us_exceptions import *
from us_file_handle import *


def id_validation():
    while True:
        user_id = find_digit_exception("id")
        if len(user_id) == 4:
            return user_id
        else:
            logging.error("Id must be 4 numbers", exc_info=True)
            print("Id must be 4 numbers")


def password_validation():
    while True:
        password = find_digit_exception("password")
        if len(password) == 8:
            return password
        if len(password) != 8:
            logging.error("password must be 8 numbers", exc_info=True)
            print("this must take 8 numbers")


def valid_lesson_id():
    """
    This function returns a unique lesson id

    """
    my_id = read_data_in_file("Responsible/9920_units.csv", "lesson_id")
    print("0000 is a keyword")
    while True:
        lesson_id = find_digit_exception("lesson id")
        if lesson_id not in my_id and lesson_id != '0000':
            if len(lesson_id) == 4:
                return lesson_id
            else:
                print("That id is not valid"
                      "this must take 4 numbers")
        else:
            print("That id is not valid"
                  "This id is available")

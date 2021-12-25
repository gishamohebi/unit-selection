import logging

logging.basicConfig(
    filename='US_logs.log',
    filemode='a',
    level=logging.INFO,
    format='%(levelname)s*%(asctime)s -%(name)s -%(message)s',
    datefmt='%d-%b-%y %H:%M:%S'
)


class OutOfRangError(Exception):
    """
    simple class method which print an alert

    """

    @classmethod
    def new(cls):
        print("that was out of range")


def find_str_exception(variable):
    """
    check string inputs to be alpha not digit
    variable : str
    return: str_input
    """
    while True:
        str_value = input(f"Add your {variable}: ")
        if str_value.isdigit() is True:
            print(f"Please enter your {variable}")
            logging.error("Wrong input format",exc_info=True)
        else:
            break

    return str_value


def find_int_exception(variable):
    """
    A simple function to handle integer value error for variable

    variable : str
        name of the variable which has an int value

    """

    while True:
        try:
            value = int(input(f"Add your {variable} : "))
        except ValueError:
            logging.error("Wrong input format", exc_info=True)
            print(" Add integer!!!! ")
        else:
            break
    return value


def find_digit_exception(variable):
    """
    check string inputs to be digit not alpha
    param variable
    return: str_value
    """
    while True:
        str_value = input(f"Add your {variable}: ")
        if str_value.isdigit() is True:
            break
        else:
            print(f"Please enter your {variable} correctly")
            logging.error("Wrong input format", exc_info=True)
    return str_value

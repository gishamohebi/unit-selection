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
        if str_value.isalpha() == True:
            break
        else:
            print(f"Please enter your {variable}")
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
        if str_value.isdigit() == True:
            break
        else:
            print(f"Please enter your {variable}")
    return str_value

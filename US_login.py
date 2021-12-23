from US_Exceptions import *
from US_file_handle import *
from Registering import user_pass


class Student:
    def __init__(self, name, student_code, term, not_passed_units, last_grade_ave, student_id):
        self.name = name
        self.student_code = student_code
        self.term = term
        self.not_passed_units = not_passed_units
        self.last_grade_ave = last_grade_ave
        self.student_id = student_id

    def unit_selection(self):
        """
        This method will check conditions of selecting and returns a file
        for each student's selection which the name would be student code

        """
        pass

    def __str__(self):
        """
        This method shows information of each student

        """
        return f"{self.__dict__}"


class Responsible:
    def __init__(self, responsible_id, responsible_pass, responsible_name):
        self.responsible_id = responsible_id
        self.responsible_pass = responsible_pass
        self.responsible_name = responsible_name

    def write_units(self):
        """
        This method will let the object  add or write to files
        return an updated or new created file
        """
        info = get_units()
        file_writing("responsible/9920_units.csv", info)
        logging.info(f"Responsible {self.responsible_name} successfully added unit", exc_info=True)
        return f"successfully added"

    def valid_selection(self, student_info):
        """
        This will check if a unit selection list of a student is valid
        due to required units for each lesson
        param student_info: file of each student which name of it would be the student code
        return valid or not
        """
        pass

    def __str__(self):
        return f"{self.__dict__}"


class LoginCheck:
    """

    objects of this class are valid available users

    """

    def __init__(self, user_id, password):
        self.user_id = user_id
        self.password = password

    def student_check(self):
        """
        Check if students log in correctly
        return result of searching students file
        if the log in information was correct this will return an object from Student class

        """
        my_id = read_data_in_file("9920/student_UP.csv", "user_name")
        my_pass = read_data_in_file("9920/student_UP.csv", "password")
        my_data = read_data_in_file("9920/9920.csv")
        self.user_id = user_pass(self.user_id, self.password)[0]  # make the str obj to hash
        if self.user_id in my_id:  # check hash file with the hashed-input
            self.password = user_pass(self.user_id, self.password)[1]
            if self.password in my_pass:
                for k in range(len(my_data)):
                    student_code = user_pass(my_data[k]["id"], my_data[k]["student_code"])[1]
                    if student_code == self.password:
                        student_code = my_data[k]["student_code"]
                        student_id = my_data[k]["id"]
                        name = my_data[k]["name"]
                        term = my_data[k]["term"]
                        not_passed_units = my_data[k]["not_passed_units"]
                        last_grade_ave = my_data[k]["last_grade_ave"]
                        logging.info(f"{name} successfully log in", exc_info=True)
                        return Student(name, student_code, term, not_passed_units, last_grade_ave,
                                       student_id)
                # line 71 : This object can select, units or display of it's information
            else:
                logging.error("Wrong pass", exc_info=True)
                return f"Wrong pass"
        else:
            logging.error("Id was not found", exc_info=True)
            return f"Id Not Found"

    def responsible_check(self):

        """
        Check if US responsible log in correctly
        Similar to student_check method
        return result of searching responsible information file
        """
        my_id = read_data_in_file("responsible/responsible_up.csv", "responsible_id")
        my_pass = read_data_in_file("responsible/responsible_up.csv", "responsible_pass")
        my_data = read_data_in_file("responsible/9920_responsible.csv")
        self.user_id = user_pass(self.user_id, self.password)[0]  # make the str obj to hash
        if self.user_id in my_id:  # check hash file with the hashed-input
            self.password = user_pass(self.user_id, self.password)[1]
            if self.password in my_pass:
                for k in range(len(my_data)):
                    responsible_pass = user_pass(my_data[k]["responsible_id"], my_data[k]["responsible_pass"])[1]
                    if responsible_pass == self.password:
                        responsible_pass = my_data[k]["responsible_pass"]
                        responsible_id = my_data[k]["responsible_id"]
                        responsible_name = my_data[k]["name"]
                        logging.info(f"{responsible_name} successfully log in", exc_info=True)
                        return Responsible(responsible_id, responsible_pass, responsible_name)
                # line 101 : This object can write units and check validation of each student's selections
            else:
                logging.error("Wrong pass", exc_info=True)
                return f"Wrong pass"
        else:
            logging.error("Id was not found", exc_info=True)
            return f"Id Not Found"

    @staticmethod
    def check_login(input_function):

        """
        Check times of wrong logging in
        return alert or object of the input_function
        """
        counter = 0
        while True:
            result = input_function()
            if result == "Wrong pass":
                print(result)
                counter += 1
                if counter == 3:
                    logging.error("The account is LOCKED", exc_info=True)
                    return "LOCKED"
                else:
                    continue
            else:
                return result


class Units:
    def __init__(self, student_code):
        self.student_code = student_code

    def unit_availability(self):
        """
        This will return available units to students of that code
        With file opening and searching unit's file

        """
        pass

    @classmethod
    def update_units_file(cls, file_name):
        """
        This will return an update list of available units
        Updates the units capacity within the file

        """
        pass


def valid_lesson_id():
    """
    This function returns a unique lesson id

    """
    my_id = read_data_in_file("responsible/9920_units.csv", "lesson_id")
    while True:
        lesson_id = find_digit_exception("lesson id")
        if lesson_id not in my_id:
            return lesson_id
        else:
            print("That id is available")


def get_units():
    """
    This function returns a dictionary with units information
    """
    lesson_id = valid_lesson_id()
    lesson_name = input("Add your lesson name: ")
    professor_name = find_str_exception("professor name")
    unit_number = find_int_exception("unit number")
    capacity = find_int_exception("capacity")
    prerequisites = find_str_exception("prerequisites")
    info = {
        'lesson_id ': lesson_id,
        'lesson_name': lesson_name,
        'professor_name': professor_name,
        'unit_number': unit_number,
        'capacity': capacity,
        'prerequisites': prerequisites
    }
    return info


def id_validation():
    user_id = find_digit_exception("id")
    while True:
        if len(user_id) == 4:
            return user_id
        else:
            logging.error("Id must be 4 numbers", exc_info=True)
            print("Id must be 4 numbers")
            user_id = find_digit_exception("id")


def password_validation():
    password = find_digit_exception("student code")
    while True:
        if len(password) == 8:
            return password
        if len(password) != 8:
            print("this must take 8 numbers")
        password = find_digit_exception("student code")


def login_student():
    """
    this function get information and creat object

    """
    student_id = id_validation()
    student_pass = password_validation()
    user = LoginCheck(student_id, student_pass)
    return user


def login_responsible():
    """
    this function get information and creat object

    """
    responsible_id = id_validation()
    responsible_pass = password_validation()
    user = LoginCheck(responsible_id, responsible_pass)
    return user

import logging
from US_Exceptions import *
from US_file_handle import *

logging.basicConfig(filename='US_logs.log', filemode='w', level=logging.INFO,
                    format='%(levelname)s*%(asctime)s -%(name)s -%(message)s', datefmt='%d-%b-%y %H:%M:%S')


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


class LoginCheck:
    """
    NOT COMPLETE
    objects of this class are valid available users

    """

    def __init__(self, user_id, password):
        self.user_id = user_id
        self.password = password

    def student_check(self):
        """
        NOT COMPLETE
        Check if students log in correctly
        return result of searching students file
        """
        my_id = read_data_in_file("9920.csv", "id")
        my_pass = read_data_in_file("9920.csv", "student_code")
        my_data = read_data_in_file("9920.csv")
        for i in my_id:
            if hash(i) == hash(self.user_id):
                for j in my_pass:
                    if hash(j) == hash(self.password):
                        for k in range(len(my_data)):
                            if my_data[k]["student_code"] == self.password:
                                name = my_data[k]["name"]
                                term = my_data[k]["term"]
                                not_passed_units = my_data[k]["not_passed_units"]
                                last_grade_ave = my_data[k]["last_grade_ave"]
                                return Student(name, self.password, term, not_passed_units, last_grade_ave,
                                               self.user_id)
                        # line 62 : This object can select, units or display of it's information
                        break
                    else:
                        print(hash(j))
                        print((hash(self.password)))
                        logging.error("Wrong pass", exc_info=True)
                        return f"Wrong pass"
                    # NOT COMPLETE
            else:
                logging.error("Id was not found", exc_info=True)
                return f"Id Not Found"
            # NOT COMPLETE
            break

    def responsible_check(self):
        """
        NOT COMPLETE
        Check if US responsible log in correctly
        Similar to student_check method
        return result of searching responsible information file
        """
        pass

    @staticmethod
    def wrong_login():
        """
        Check times of wrong logging in
        return alert
        """
        pass


class Responsible:
    def __init__(self, responsible_id, responsible_pass):
        self.responsible_id = responsible_id
        self.responsible_pass = responsible_pass

    def write_units(self):
        """
        This method will let the object  add or write to files
        return an updated or new created file
        """
        pass

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


def id_validation():
    # THIS FUNCTION IS NOT COMPLETE
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


def login_student_info():
    student_id = id_validation()
    student_pass = password_validation()
    user = LoginCheck(student_id, student_pass)
    result = user.student_check()
    return result


def login_responsible_info():
    responsible_id = id_validation()
    responsible_pass = password_validation()
    user = LoginCheck(responsible_id, responsible_pass)
    result = user.responsible_check()
    return result

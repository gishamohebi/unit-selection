from US_Exceptions import *
from US_file_handle import *
import re
import json
import logging
import hashlib

logging.basicConfig(filename='US_logs.log', filemode='a', level=logging.INFO,
                    format='%(levelname)s*%(asctime)s -%(name)s -%(message)s', datefmt='%d-%b-%y %H:%M:%S')


def user_pass(user_name, password):
    user_name = user_name.encode()
    password = password.encode()
    return [hashlib.sha256(user_name).hexdigest(), hashlib.sha256(password).hexdigest()]


class RegisterStudent:
    """
    This class return an object which is valid to add to 9920.csv file
    """

    def __init__(
            self, first_name, last_name, student_code,
            term, not_passed_units, last_grade_ave, student_id
    ):
        self.name = first_name + " " + last_name
        self.student_code = student_code
        self.term = term
        self.not_passed_units = not_passed_units
        self.last_grade_ave = last_grade_ave
        self.student_id = student_id

    def write_to_file(self):

        if re.search(r'^9920', self.student_code):
            my_passwords = read_data_in_file("9920/9920.csv", "student_code")
            my_id = read_data_in_file("9920/9920.csv", "id")
            if self.student_id not in my_id:
                if self.student_code not in my_passwords:
                    register_student_file_writing("9920/9920.csv", self)
                    self.student_id = user_pass(self.student_id, self.student_code)[0]
                    self.student_code = user_pass(self.student_id, self.student_code)[1]
                    writing_up_file(self.student_id, self.student_code, "9920/student_UP.csv")
                    print("successfully registered!")
                    logging.info("successfully registered", exc_info=True)
                else:
                    print("this student code is available")
                    logging.info("this  student code is available", exc_info=True)
            else:
                print("this id code is available")
                logging.info("this  id code is available", exc_info=True)

        else:
            print("This app is for id which starts with 9920")
            logging.warning("This is a program for id which starts with 9920", exc_info=True)
            info = self.__dict__
            with open('others.json', "a") as myfile:  # writing json file
                json.dump(info, myfile)
            print("You were added to others.json successfully")

    @classmethod
    def student_code_validation(cls):
        student_code = find_digit_exception("student code")
        while len(student_code) != 8:
            print("this must take 8 numbers")
            student_code = find_digit_exception("student code")
            if len(student_code) == 8:
                print(student_code)
        return student_code

    @classmethod
    def term_validation(cls):
        term = find_int_exception("term")
        while term > 8 or term < 1:
            print("select from 1 to 8")
            term = find_int_exception("term")
            if 1 <= term <= 8:
                break
        return term

    @classmethod
    def important_units(cls, term, student_code):
        """
        This will help the student and responsible for unit selection validation
        param term: digit
        param student_code: digit
        return  not_passed_units: string
        """
        if term == 1:
            return " "
        else:
            term = str(term)
            if re.search(r'^9920', student_code):
                file_name = "9920/9920_important.csv"
            else:
                print("This app is for id which starts with 9920")
                logging.warning("This is a program for id which starts with 9920", exc_info=True)
                not_passed_units = " "
                return not_passed_units
            important_unit_list = read_data_in_file(file_name, term)  # this is a list of important units of that term
            print(f"Select your not passed units number")
            for i in range(len(important_unit_list)):
                if important_unit_list[i] == "":
                    important_unit_list.pop(i)
            while True:
                try:
                    for i, itme in enumerate(important_unit_list):
                        print(f"{i + 1} : {itme} \n")
                    print("Select 0 if there is not any")
                    selected = find_int_exception("not passed unit")
                    if selected == 0:
                        not_passed_units = " "
                        return not_passed_units
                    if selected != 0:
                        not_passed_units = important_unit_list[selected - 1]
                        return not_passed_units
                except IndexError:

                    logging.error("selection not in range ", exc_info=True)
                    print("select from below")
                else:
                    break

    @classmethod
    def grade(cls):
        last_grade_ave = find_int_exception("last grade ave")
        while True:
            if last_grade_ave < 0 or last_grade_ave > 20:
                logging.error("grade not in range ", exc_info=True)
                print("0 <= grade <= 20")
                last_grade_ave = find_int_exception("last grade ave")
            else:
                return last_grade_ave

    @classmethod
    def id_validation(cls):
        # THIS FUNCTION IS NOT COMPLETE
        student_id = find_digit_exception("id")
        while True:
            if len(student_id) == 4:
                return student_id
            else:
                logging.error("Id must be 4 numbers", exc_info=True)
                print("Id must be 4 numbers")
                student_id = find_digit_exception("id")

    def __str__(self):
        return f"{self.__dict__}"


def register_student():
    """
    return an object from RegisterStudent

    """
    first_name = find_str_exception("first name").capitalize()
    last_name = find_str_exception("last name ").capitalize()
    term = str(RegisterStudent.term_validation())
    student_code = str(RegisterStudent.student_code_validation())
    not_passed_units = RegisterStudent.important_units(term, student_code)
    last_grade_ave = str(RegisterStudent.grade())
    student_id = str(RegisterStudent.id_validation())

    return RegisterStudent(first_name, last_name, student_code, term, not_passed_units, last_grade_ave, student_id)

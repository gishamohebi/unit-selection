from US_Exceptions import *
from US_file_handle import *
from Registering import user_pass
import re
import os
import shutil


class Student:
    def __init__(self,
                 name, student_code,
                 term, not_passed_units,
                 last_grade_ave, student_id
                 ):
        self.name = name
        self.student_code = student_code
        self.term = term
        self.not_passed_units = not_passed_units
        self.last_grade_ave = last_grade_ave
        self.student_id = student_id
        self.selected_units = []  # to check each unit was selected once
        self.units_number = 0  # to check numbers of selected units

    def unit_selection(self, selected_lesson_id):
        """
        This method will check conditions of selecting and returns
        the selected unit info

        """
        my_id = read_data_in_file("Responsible/9920_units.csv", "lesson_id")
        my_unit = read_data_in_file("Responsible/9920_units.csv")

        if len(self.selected_units) == 0:
            if selected_lesson_id in my_id:  # check if the selected unit id was correct
                self.selected_units.append(selected_lesson_id)
                for i in my_unit:
                    if i["lesson_id"] == selected_lesson_id:
                        selected_unit = i
                        self.units_number += int(selected_unit['unit_number'])
                        return selected_unit
            else:
                logging.error(f"{self.name} selection was not found lesson", exc_info=True)
                message = f"The selected id was not found"
                return message

        else:
            if selected_lesson_id in my_id:
                if selected_lesson_id not in self.selected_units:  # check each unit was selected once
                    if self.units_number < 20:  # check the valid range of selection
                        for i in my_unit:
                            if i["lesson_id"] == selected_lesson_id:
                                selected_unit = i
                                self.units_number += int(selected_unit['unit_number'])
                                return selected_unit
                    if self.units_number == 20:  # check the valid range of selection
                        message = f"You cant select more than 20 units"
                        return message

                else:
                    message = f"You selected {selected_lesson_id} once." \
                              f"You cant select it more than once"
                    return message
            else:
                logging.error(f"{self.name} selection was not found lesson", exc_info=True)
                message = f"The selected id was not found"
                return message

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

    def write_units(self, info):
        """
        This method will let the object  add or write to files
        return an updated or new created file
        """
        file_writing("Responsible/9920_units.csv", info)
        logging.info(f"Responsible {self.responsible_name} successfully added unit", exc_info=True)
        return f"successfully added"

    @classmethod
    def find_selectors_info(cls):
        """
        This function returns a list
        index 0 : selectors ' student codes
        index 1 : list of selectors ' information
        """
        selector_codes = []
        path = "selected units"
        for file in os.listdir(path):
            if file.endswith(".csv"):
                selector_codes.append(file.strip(".csv"))
        # get the selectors student codes from the created files after each selection
        information = read_data_in_file("9920/9920.csv")
        selector_info = []
        for code in selector_codes:
            for info in information:
                if code == info["student_code"]:
                    selector_info.append(info)
                # get the selectors information
        return [selector_codes, selector_info]

    @classmethod
    def display_selector_info(cls, student_code):
        """
        This function checks if the input student code is valid among selectors
        returns either dictionary of the information or a message

        """
        selectors_code = Responsible.find_selectors_info()[0]
        if student_code in selectors_code:
            selectors_info = Responsible.find_selectors_info()[1]
            for info in selectors_info:
                if info["student_code"] == student_code:
                    selector_info = info
                    return selector_info
        else:
            message = f"{student_code} >>> was not among selectors"
            return message

    def confirm_selection(self, student_info):
        """
        This will check if a unit selection list of a student is valid
        due to required units for each lesson
        param student_info: dict of each student info
        returns a file in confirmed selection directory

        """
        student_code = student_info["student_code"]
        name = student_info["name"]
        selector_path = f"selected units/{student_code}.csv"
        students_selection = read_data_in_file(selector_path)
        students_selection_pre = read_data_in_file(selector_path, "prerequisites")
        if os.path.exists(f"confirmed selections/{student_code}.csv") is False:
            for lessons in students_selection_pre:
                if lessons != student_info["not_passed_units"]:
                    shutil.copy(selector_path, "confirmed selections")

                    logging.info(f"{name} selection was valid")
                    message = f"{name} selection is valid"
                    return message
                else:
                    for unit in students_selection:
                        if unit["prerequisites"] == student_info["not_passed_units"]:
                            students_selection.remove(unit)
                    for i in range(len(students_selection)):
                        file_writing(f"confirmed selections/{student_code}.csv", students_selection[i])
                        message = f"some of {name}'s selection was not valid"
                    return message
        else:
            message = f"Selection of {name} was confirmed once"
            return message

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
        my_hash = {}
        for i in range(len(my_id)):
            my_hash[my_id[i]] = my_pass[i]
        print(my_hash)
        my_data = read_data_in_file("9920/9920.csv")
        self.user_id = user_pass(self.user_id, self.password)[0]  # make the str obj to hash
        self.password = user_pass(self.user_id, self.password)[1]
        if self.user_id in my_hash.keys():
            password = my_hash[self.user_id]
            if self.password == password:
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
                        # upper line : This object can select, units or display of it's information
            else:
                logging.error("Wrong pass", exc_info=True)
                return f"Wrong pass"

        else:
            logging.error("Id was not found", exc_info=True)
            return f"Id Not Found"

    def responsible_check(self):

        """
        Check if US Responsible log in correctly
        Similar to student_check method
        return result of searching Responsible information file
        """
        my_id = read_data_in_file("Responsible/responsible_up.csv", "responsible_id")
        my_pass = read_data_in_file("Responsible/responsible_up.csv", "responsible_pass")
        my_data = read_data_in_file("Responsible/9920_responsible.csv")
        my_hash = {}
        for i in range(len(my_id)):
            my_hash[my_id[i]] = my_pass[i]

        self.user_id = user_pass(self.user_id, self.password)[0]  # make the str obj to hash
        self.password = user_pass(self.user_id, self.password)[1]
        if self.user_id in my_hash.keys():
            password = my_hash[self.user_id]
            if self.password == password:
                for k in range(len(my_data)):
                    responsible_pass = user_pass(my_data[k]["responsible_id"], my_data[k]["responsible_pass"])[1]
                    if responsible_pass == self.password:
                        responsible_pass = my_data[k]["responsible_pass"]
                        responsible_id = my_data[k]["responsible_id"]
                        responsible_name = my_data[k]["name"]
                        logging.info(f"{responsible_name} successfully log in", exc_info=True)
                        return Responsible(responsible_id, responsible_pass, responsible_name)
                        # upper line : This object can write units and check validation of each student's selections
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
        self.data_file = None

    def unit_availability(self):
        """
        This will return available units to students of that code
        With file opening and searching unit's file

        """
        # codes_list = ['9920','9921',other first 4 numbers of a student code]
        # pattern = an item selected from codes_list
        # if re.search(r 'pattern', self.student_code)
        # these lines show the code for more than one field
        if re.search(r'^9920', self.student_code):
            self.data_file = pandas_read_data('Responsible/9920_units.csv')
            return self.data_file

    @classmethod
    def update_units_file(cls, selected_unit):
        """
        This will return an update list of available units
        Updates the units capacity within the file

        """
        my_unit = read_data_in_file("Responsible/9920_units.csv")
        for unit in my_unit:
            if unit["lesson_id"] == selected_unit:
                capacity = (int(unit["capacity"]) - 1)
                unit["capacity"] = capacity
        for i in range(len(my_unit)):
            if i == 0:
                file_writing("Responsible/9920_units.csv", my_unit[i], mode="w")
            else:
                file_writing("Responsible/9920_units.csv", my_unit[i], mode="a")

        return logging.info("9920_units.csv updated")


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


def login_student():
    """
    this function get information and creat object

    """
    student_id = id_validation()
    student_pass = password_validation()
    user = LoginCheck(student_id, student_pass)
    check_user = user.student_check()
    return check_user


def login_responsible():
    """
    this function get information and creat object

    """
    responsible_id = id_validation()
    responsible_pass = password_validation()
    user = LoginCheck(responsible_id, responsible_pass)
    check_user = user.responsible_check()
    return check_user

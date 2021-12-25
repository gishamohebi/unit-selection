from Registering import *
from US_login import *
import os

print("THIS IS A PROGRAM FOR STUDENT WHICH ID STARTS WITH 9920\n"
      "OTHERS WILL SIMPLY ADD TO JSON FILE "
      )

while True:
    print("1.Sign in\n"
          "2.Log in\n"
          "3.Break"
          )
    key = find_int_exception("menu key")
    if key == 1:
        while True:
            print("1.New Student\n2.Back to main")
            key_1 = find_int_exception("menu key")
            if key_1 == 1:
                new_student = register_student()
                message = new_student.write_to_file()
                print(message)
            if key_1 == 2:
                break
            if key_1 > 2 or key_1 < 1:
                key_1 = OutOfRangError.new()
    if key == 2:
        while True:
            print("1.US Responsible\n"
                  "2.Student\n"
                  "3.Back to main"
                  )
            key_2 = find_int_exception("menu key")
            if key_2 == 1:
                print("Try id=1111 and pass=99201111 to see log in successfully")
                result = LoginCheck.check_login(login_responsible)
                if type(result) != str:
                    responsible = result
                    print("successfully log in")
                    while True:
                        print("1.Display info\n"
                              "2.Add Units\n"
                              "3.Display Selected Units\n"
                              "4.Back to menu"
                              )
                        key_3 = find_int_exception("menu key")
                        if key_3 == 1:
                            print(responsible)
                        if key_3 == 2:
                            response = responsible.write_units()
                            print(response)
                            pass
                        if key_3 == 3:
                            print("NOT COMPLETED")
                            pass
                        if key_3 == 4:
                            break
                        if key_3 > 4 or key_3 < 1:
                            key_3 = OutOfRangError.new()
                else:
                    print(result)

            if key_2 == 2:
                print("Try id=1111 and pass=99201111 to see log in successfully")
                result = LoginCheck.check_login(login_student)
                if type(result) != str:
                    student = result
                    print("successfully log in")

                    while True:
                        print("display info works others are not complete")
                        print("1.Display info\n"
                              "2.Unit Selection\n"
                              "3.Display Selected Units\n"
                              "4.Back to menu"
                              )
                        key_4 = find_int_exception("menu key")

                        if key_4 == 1:
                            print(student)

                        if key_4 == 2:
                            if os.path.exists(f"selected units/{student.student_code}.csv"):
                                logging.error(f"{student.name} tried for another selection", exc_info=True)
                                print("You cannot select units more than once")
                            else:

                                while True:
                                    print("\n* * * Select Your Lesson Id * * *")
                                    available_units = Units(student_code=student.student_code)
                                    available_units = available_units.unit_availability()
                                    print(available_units.to_string())
                                    print("\nEnter 0000 when you are finished\n ")
                                    selected_id = id_validation()
                                    if selected_id != '0000':
                                        result = student.unit_selection(selected_id)
                                        if type(result) != str:
                                            file_writing(f"selected units/{student.student_code}.csv", result)

                                        if type(result) == str:
                                            print(result)
                                    if selected_id == "0000":
                                        if student.units_number >= 10:
                                            logging.info(f"{student.name} successfully selected units", exc_info=True)
                                            break
                                        if student.units_number < 10:
                                            print(f"you selected {student.units_number} units, at least must be 10")
                                            logging.error(f"{student.name} submitted before selecting 10 units")

                                    available_units = Units(student_code=student.student_code)
                                    available_units = available_units.update_units_file(selected_id)
                                    display = pandas_read_data(f"selected units/{student.student_code}.csv")
                                    print(f"\n{display.to_string()}")
                                    print(f"\ntotal selected units >>> {student.units_number}")

                        if key_4 == 3:
                            if os.path.exists(f"selected units/{student.student_code}.csv"):
                                display = pandas_read_data(f"selected units/{student.student_code}.csv")
                                print(display.to_string())
                            else:
                                print("You did not select any units")
                        if key_4 == 4:
                            break
                        if key_4 > 4 or key_4 < 1:
                            key_4 = OutOfRangError.new()
                else:
                    print(result)
            if key_2 == 3:
                break
            if key_2 > 4 or key_2 < 1:
                key_2 = OutOfRangError.new()

    if key == 3:
        break
    if key < 1 or key > 3:
        key = OutOfRangError.new()

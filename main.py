from Registering import *
from US_login import *

print("THIS IS A PROGRAM FOR STUDENT WHICH ID STARTS WITH 9920\nOTHERS WILL SIMPLY ADD TO JSON FILE ")

while True:
    print("1.Sign in\n2.Log in\n3.Break")
    key = find_int_exception("menu key")
    if key == 1:
        while True:
            print("1.New Student\n2.Back to main")
            key_1 = find_int_exception("menu key")
            if key_1 == 1:
                new_student = register_student()
                new_student.write_to_file()
            if key_1 == 2:
                break
            if key_1 > 2 or key_1 < 1:
                key_1 = OutOfRangError.new()
    if key == 2:
        while True:
            print("NOT COMPLETED BUT STUDENT OPTION WORKS")
            print("1.US responsible\n2.Student\n3.Back to main")
            key_2 = find_int_exception("menu key")
            if key_2 == 1:
                result = LoginCheck.wrong_login(login_responsible)
                if type(result) != str:
                    responsible = result
                    print("successfully log in")
                    print("1.Display info\n2.Add Units\n3.Display Selected Units\n4.Back to menu")
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
                        pass
                    if key_3 > 4 or key_3 < 1:
                        key_3 = OutOfRangError.new()
                else:
                    print(result)
            if key_2 == 2:
                print("Try id=2222 and pass=99201345 to see log in successfully")
                result = LoginCheck.wrong_login(login_student)
                if type(result) != str:
                    student = result
                    print("successfully log in")
                    print("display info works others are not complete")
                    print("1.Display info\n2.Unit Selection\n3.Display Units\n4.Back to menu")
                    key_4 = find_int_exception("menu key")
                    if key_4 == 1:
                        print(student)
                    if key_4 == 2:
                        print("NOT COMPLETED")
                        pass
                    if key_4 == 3:
                        print(" ")
                        pass
                    if key_4 == 4:
                        pass
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

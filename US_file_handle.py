import csv


def read_data_in_file(file_name, header=None):
    with open(file_name, "r") as f:
        data_in_file = []
        my_file = csv.DictReader(f)
        if header != None:
            for row in my_file:
                data_in_file.append(row[header])
        else:
            for row in my_file:
                data_in_file.append(row)

    return data_in_file


def register_student_file_writing(file_name, self):
    """
    this is a function only for RegisterStudents write_to_file method
    param : file_name
    param : self : object of the Class

    """
    with open(file_name, "a") as f:
        fieldnames = ["name", "student_code", "term", "not_passed_units", "last_grade_ave", "id"]
        my_file = csv.DictWriter(f, fieldnames)
        my_file.writerow({
            fieldnames[0]: self.name,
            fieldnames[1]: self.student_code,
            fieldnames[2]: self.term,
            fieldnames[3]: self.not_passed_units,
            fieldnames[4]: self.last_grade_ave,
            fieldnames[5]: self.student_id

        })


def writing_up_file(user_name, password, name_of_file):
    with open(name_of_file, "a") as my_file:
        writer = csv.DictWriter(my_file, fieldnames=["user_name", "password"])
        if my_file.tell() == 0:
            writer.writeheader()
        writer.writerow({
            "user_name": user_name,
            "password": password
        })

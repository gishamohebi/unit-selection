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
            fieldnames[5]: self.id

        })

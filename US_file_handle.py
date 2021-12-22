import csv


def read_data_in_file(file_name, header=None):
    with open(file_name, "r") as f:
        data_in_file = []
        my_file = csv.DictReader(f)
        if header is not None:
            for row in my_file:
                data_in_file.append(row[header])
        else:
            for row in my_file:
                data_in_file.append(row)

    return data_in_file


def file_writing(name_of_file, info, mode="a"):
    with open(name_of_file, mode) as my_file:
        fields = info.keys()
        info = [info]
        writer = csv.DictWriter(my_file, fieldnames=fields)
        if my_file.tell() == 0:
            writer.writeheader()
        writer.writerows(info)


def writing_up_file(user_name, password, name_of_file):
    """
    this function writes the hashed user name password to the related file
    param user_name
    param password
    param name_of_file
    """
    with open(name_of_file, "a") as my_file:
        writer = csv.DictWriter(my_file, fieldnames=["user_name", "password"])
        if my_file.tell() == 0:
            writer.writeheader()
        writer.writerow({
            "user_name": user_name,
            "password": password
        })

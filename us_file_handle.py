import csv
import pandas as pd
import os
import re


def pandas_read_data(name_of_file):
    df = pd.read_csv(name_of_file)
    return df


def read_data_in_file(file_name, header=None):
    if os.path.exists(file_name):
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
    else:
        pass


def file_writing(name_of_file, info, mode=None):
    if mode is None:
        if os.path.exists(name_of_file):
            mode = "a"
        else:
            mode = "w"
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


def find_file_name(code):
    """
    This function help us to handle different students from different fields
    returns related student's information file or directory
    if the field was not found returns None
    """
    fields = ['9920', '9921']
    file_name = None
    for filed in fields:
        valid = re.compile(f"^{filed}")
        if valid.search(code):
            file_name = filed
            return file_name
        else:
            pass
    if file_name is None:
        return None

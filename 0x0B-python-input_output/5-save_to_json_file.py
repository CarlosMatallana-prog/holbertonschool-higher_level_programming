#!/usr/bin/python3
""" save_to_json_file """
import json


def save_to_json_file(my_obj, filename):
    """ save_to_json_file function """
    with open(filename, "w") as json_txt_file:
        json_txt_file.write(json.dumps(my_obj))

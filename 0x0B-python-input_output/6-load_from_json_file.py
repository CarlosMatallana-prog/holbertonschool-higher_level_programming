#!/usr/bin/python3
""" 6-load_from_json_file """
import json


def load_from_json_file(filename):
    """ load_from_json_file function """
    with open(filename) as json_txt:
        return json.loads(json_txt.read())

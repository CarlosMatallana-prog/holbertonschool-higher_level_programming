#!/usr/bin/python3
""" 5-text_indentation """


def text_indentation(text):
    """  prints a text with 2 new lines  """

    if type(text) is not str:
        raise TypeError("text must be a string")
    character = 0
    text = text.strip(' ')
    while character < len(text):
        print(text[character], end='')
        if text[character] in (".", "?", ":"):
            if (character + 1) < len(text):
                while text[character + 1] == ' ':
                    character += 1
            print("\n")
        character += 1

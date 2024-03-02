#!/usr/bin/python3
"""defining write_file function"""


def write_file(filename="", text=""):
    """reads filename with utf-8"""
    with open(filename, "w", encoding="utf-8" as file:
            return file.write(text)

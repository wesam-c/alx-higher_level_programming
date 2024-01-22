#!/usr/bin/python3
'''
I want to know which integar and which not by using :d and return either true or false
type error means if it is string
'''
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False

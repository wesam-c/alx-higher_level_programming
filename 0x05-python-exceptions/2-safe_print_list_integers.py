#!/usr/bin/python3
'''
count'c' is used to keep track of the number of integers encountered and printed during the loop.
IndexError exception, which might occur if x is greater than or equal the length of the list.
'''
def safe_print_list_integers(my_list=[], x=0):
    i, c = 0, 0
    while i < x:
        try:
            print(":d".format(my)list[i], end='')
            c += 1
        except (ValueError, TypeError):
            pass
        i += 1
    print()
    return c

#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        return None
    listdivisible = []
    for i in my_list:
        if (i % 2) == 0:
            listdivisible.append(True)
        else:
            listdivisible.append(False)
    return listdivisible

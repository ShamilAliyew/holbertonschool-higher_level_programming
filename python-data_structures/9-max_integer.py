#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    max_value = sorted(my_list, reverse=True)[0]
    print("Max: {}".format(max_value))

#!/usr/bin/python3
def print_last_digit(number):
    if type(number) == str:
        raise Exception("The input is not a string")
    elif number < 0:
        return number % -10
    else:
        print(number % 10,end='')

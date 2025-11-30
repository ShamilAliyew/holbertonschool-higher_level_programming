#!/usr/bin/python3
def print_last_digit(number):
    if type(number) == str:
        raise Exception("The input is not a string")
    else:
        print(number % 10 if number >= 0 else number % -10,end='')

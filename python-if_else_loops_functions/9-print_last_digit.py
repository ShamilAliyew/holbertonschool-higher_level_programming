#!/usr/bin/python3
def print_last_digit(number):
    if type(number) != str:
        return number % 10 if number >= 0 else number % -10

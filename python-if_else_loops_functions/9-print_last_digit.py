#!/usr/bin/python3
def print_last_digit(number):
    last_digit = abs(number) % 10  # son rəqəmi tapmaq
    print(last_digit, end='')       # çap et
    return last_digit               # return et

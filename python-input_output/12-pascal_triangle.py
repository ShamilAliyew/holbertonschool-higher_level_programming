#!/usr/bin/python3
"""a function that returns a list of lists of integers
 representing the Pascal’s triangle of n"""


def pascal_triangle(n):
    """a function that returns a list of lists of integers
     representing the Pascal’s triangle of n"""
    if n<= 0:
        return []
    for i in range(n):
        print("{:<{}d}".format(i, n))

print(pascal_triangle(10))

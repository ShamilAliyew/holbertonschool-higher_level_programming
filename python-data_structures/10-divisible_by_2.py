#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_result = [True if i % 2 == 0 else False for i in my_list]
    for i in range(len(my_list)):
        print("{:d} {:s} divisible by 2"
              .format(my_list[i], "is" if list_result[i] else "is not"))

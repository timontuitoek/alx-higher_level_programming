#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count_list = 0
    for element in range(x):
        try:
            print("{:d}".format(my_list[element]), end="")
            count_list += 1
        except IndexError:
            break
    print("")
    return count_list

#!/usr/bin/python3

def weight_average(my_list=[]):
    if not isinstance(my_list, list) or len(my_list) == 0:
        return 0

    total_weight = 0
    total_value = 0

    for tup in my_list:
        value, weight = tup
        total_weight += weight
        total_value += value * weight

    if total_weight == 0:
        return 0

    average = total_value / total_weight
    return average

#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0

    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    num = 0
    i = 0

    while i < len(roman_string):
        if i < len(roman_string) - 1 and roman_string[i:i+2] in roman_map:
            num += roman_map[roman_string[i:i+2]]
            i += 2
        else:
            num += roman_map[roman_string[i]]
            i += 1

    return num

#!/usr/bin/python3
def roman_to_int(roman_string):
    last = roman_string[0]
    result = 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for num in roman_string:
        if roman[last] >= roman[num]:
            result += roman[num]
        else:
            result += roman[num] - 2 * roman[last]
        last = num
    return result

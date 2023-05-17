#!/usr/bin/python3

def weight_average(my_list=[]):
    if my_list == []:
        return 0
    value1 = 0
    value2 = 0
    for score, weight in my_list:
        value1 += score * weight
        value2 += weight
    if value2 == 0:
        return 0
    average = value1 / value2
    return average

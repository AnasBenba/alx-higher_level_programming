#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        for elm in my_list:
            if i < x:
                print(elm, end = "")
                i += 1
        print("\n")
    except:
        print("Error")
    return i

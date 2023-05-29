def list_division(my_list_1, my_list_2, list_length):
    try:
        my_list = [None] * list_length
        for i in range(list_length):
            try:
                my_list[i] = my_list_1[i] / my_list_2[i]
            except TypeError:
                print("wrong type")
                my_list[i] = 0
            except ZeroDivisionError:
                print("division by 0")
                my_list[i] = 0
            except IndexError:
                print("out of range")
                my_list[i] = 0
    finally:
        return my_list

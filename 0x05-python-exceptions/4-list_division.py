#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_lenght):
    new_list = []
    for i in range(0, list_lenght):
        try:
            div = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by zero")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            new_list.append(div)
    return (new_list)

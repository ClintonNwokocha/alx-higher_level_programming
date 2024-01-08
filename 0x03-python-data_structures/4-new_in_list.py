#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    modified_list = my_list[:]
    if idx < 0:
        return modified_list
    if idx >= len(my_list):
        return modified_list
    modified_list[idx] = element
    return modified_list
    

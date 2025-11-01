#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if (idx < 0 or len(my_list) <= idx):
        return ([x for x in my_list])
    new_list = []
    for e in range(len(my_list)):
        if (idx == e):
            new_list.append(element)
            continue
        new_list.append(my_list[e])
    return (new_list)

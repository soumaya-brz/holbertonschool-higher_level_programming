#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    unique_numbers = []

    for number in my_list:
        if number not in unique_numbers:
            unique_numbers.append(number)
            result += number

    return result

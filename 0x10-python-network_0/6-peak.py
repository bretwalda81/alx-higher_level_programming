#!/usr/bin/python3
"""
This function finds a high point in the passed in array
Note that this function only finds A high point, not THE high point
As such, depending on how the code is written, it is possible to have
more than 1 possible result. Ex. given a list [4, 2, 1, 2, 3, 1],
4 and 3 are valid answers
"""


def find_peak(list_of_integers):
    """ Find dat peak """
    cpy = list_of_integers
    begin = 0
    end = len(cpy) - 1

    if begin >= end:
        return None

    while begin < end:
        mid = int(((end - begin) / 2) + begin)
        if cpy[mid] > cpy[mid - 1] and cpy[mid] > cpy[mid + 1]:
            return cpy[mid]
        else:
            # This is where valid answers can deviate. We can choose
            # whether to check and search the left side first, or
            # the right side first. Both are correct, and therefore
            # the result can differ. However, what is important is that
            # we correctly move the beginning or ending pointer depending on
            # the if statement
            # We will check the right side first. Editing the code to check
            # the left side first is a trivial matter
            if cpy[mid] <= cpy[mid + 1]:
                begin = mid + 1
            elif cpy[mid] <= cpy[mid - 1]:
                end = mid - 1

    return cpy[begin]

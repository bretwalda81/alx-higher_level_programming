#!/usr/bin/python3
def remove_char_at(str, n):
    str_2 = ''
    i = 0
    for c in str:
        if i != n:
            str_2 += str[i]
        i += 1
    return str_2

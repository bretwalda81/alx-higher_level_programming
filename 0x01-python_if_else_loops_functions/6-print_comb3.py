#!/usr/bin/python3
for i in range(0, 9):
    for x in range(1, 10):
        if x > i:
            if x != 9 or i != 9:
                print(f"{i}{x}", end=", ")
            else:
                print(f"{i}{x}")

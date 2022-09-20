#!/usr/bin/python3
for i in range(ord('z'), ord('a'), -2):
    print(f"{i:c}{chr(i - 33):s}", end="")

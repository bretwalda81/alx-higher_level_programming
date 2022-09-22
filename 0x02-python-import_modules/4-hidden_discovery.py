#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4

    list = dir(hidden_4)
    num = len(dir(hidden_4))
    for i in range(num):
        if list[i][:2] != "__":
            print(list[i])

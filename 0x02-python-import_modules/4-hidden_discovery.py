#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    all_func = dir(hidden_4)
    for i in all_func:
        if i[:2] != "__":
            print("{:s}".format(i))

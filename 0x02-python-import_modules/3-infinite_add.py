#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    addition = 0
    for i in range(len(sys.argv) - 1):
        addition +=  int(sys.argv[i + 1])
    print(addition)

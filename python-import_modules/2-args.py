#!/usr/bin/python3

if __name__ == "__main__":
    import sys

num = len(sys.argv -1)
if num == 0:
    print("{0} arguments.". format(num))
elif num == 1:
    print("{0} argument:". format(num))
else:
    print("{0} arguments:". format(num))

for i in range (1, sys.argv + 1):
    print("{0}: {1}". format(i, sys.argv[i]))

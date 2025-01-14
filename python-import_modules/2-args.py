#!/usr/bin/python3

if __name__ == "__main__":
    import args

num = len(args.argv)
if num == 0:
    print("{num} arguments.". format(num))
elif num == 1:
    print("{num} argument:". format(num))
else:
    print("{num} arguments:". format(num))

for i in range (1, args.argv + 1):
    print("{0}: {1}". format(i, args.arg[i]))
#!/usr/bin/python3
for i in range(ord('a'), ord('z') + 1):
    if i is ord('q') or i is ord('e'):
        continue
    print("{}".format(chr(i)), end="")

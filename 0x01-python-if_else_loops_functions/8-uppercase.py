#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) == ord(' '):
            i = chr(ord(i))
        elif ord(i) >= ord('a') and ord(i) <= ord('z'):
            i = chr(ord(i) - 32)
        elif ord(i) >= ord('A') and ord(i) <= ord('Z'):
            i = chr(ord(i))
        else:
            i = chr(ord(i))
        print("{:s}".format(chr(ord(i))), end="")
    print()

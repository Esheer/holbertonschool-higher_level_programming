#!/usr/bin/python3
for x in range(ord('a'), ord('z')):
    if chr(x) == 'e' or chr(x) == 'q':
        continue
    print("{:s}".format(chr(x)), end = "")

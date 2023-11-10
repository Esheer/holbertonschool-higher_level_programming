#!/usr/bin/python3
for x in range(ord('a'), ord('z')):
    if chr (x) == 'q' or chr (x) == 'e':
        continue
    print("{:s}".format (chr(x)), end = "")


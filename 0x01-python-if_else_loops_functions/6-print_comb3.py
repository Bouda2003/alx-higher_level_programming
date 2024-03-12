#!/usr/bin/python3
for i in range(1, 10):
    for j in range(i):
        print("{:02d}".format(j) + ", {:02d}".format(i), end=", " if i < 9 or j < 8 else "\n")

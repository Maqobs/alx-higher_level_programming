#!/usr/bin/python3
for letter in range(96, 123):
    if chr(letter) != 'q' and chr(letter) != 'e':
        print("{}".format(chr(letter)), end='')

#!/usr/bin/python3
import random
number = random.randit(-10000, 10000)
digit = abs(number) % 10
    print("last digit of {} is {} and ".format(number, digit), end='')

    if number < 0:
        digit = -digit

if digit > 5:
    print('is greater than 5')
elif digit == 0:
    print('is 0')
else:
    print('is less than 6 and not 0')

#!/usr/bin/env python3
number = float(input("Give me a number: "))
if number.is_integer():
    print("This number is an integer")
    print(number.is_integer)
else:
    print("This number is a decimal.")

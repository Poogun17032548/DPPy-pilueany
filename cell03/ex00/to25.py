#!/usr/bin/env python3
num = 25
number = int(input("Enter a number less than 25\n"))
if (number > num):
    print("Error")
else:
    while number <= num :
            print(f"Inside the loop, my variable is {number}")
            number += 1
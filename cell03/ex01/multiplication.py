#!/usr/bin/env python3

g = 0
number = int(input("Enter a number\n"))
sol = g * number
while g < 9:
    sol = g * number
    print(f"{g} x {number} = {sol}")
    g +=1
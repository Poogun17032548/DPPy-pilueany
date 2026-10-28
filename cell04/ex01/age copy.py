#!/usr/bin/env python3
import sys

inage = int(sys.argv[1])
age = 10
print(f"You are currently {inage} years old")
for i in range(3):
    print(f"In {age} years, you'll be {inage + age} years old.")
    age += 10


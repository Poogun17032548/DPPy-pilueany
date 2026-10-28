#!/usr/bin/env python3
import sys
# vertical = v
# horizontal = h
if (len(sys.argv) > 1):
    print("none")
else :
    v = 0
    h = 0
    while v < 11 :
        table = f"Table de {v}:"
        print(table,end="")
        while h < 11:
            test = f"{h*v}"
            print(test,end= " ")
            h += 1
        print("")
        h = 0
        v += 1
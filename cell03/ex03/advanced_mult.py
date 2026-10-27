#!/usr/bin/env python3
import sys
# vertical = v
# horizontal = h
if (sys.argv[1] == "yolo"):
    print("none")
elif(sys.argv[0] == "./advanced_mult.py" ) :
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


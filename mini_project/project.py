#!/usr/bin/env python3
import time
import random



def b(docu):
    while True:
        time.sleep(0.5)
        print("\nHello\n\n")
        time.sleep(0.5)
        name = input("Insert your name:\nExit for Exit: \n".upper())
        time.sleep(0.5)
        if name.upper() == "EXIT":
            time.sleep(0.5)
            print("\n\n")
            return docu
        elif not name.strip():
            time.sleep(0.5)
            print("\nName cannot be empty\n")
        else :
            time.sleep(0.5)
            print(f"\nYour inserted name: {name}")
            time.sleep(0.5)
            print("You have successfully signed up")
            return name
    #play game no document = no access
def a(test):
    if not test:
        time.sleep(0.5)
        print("\nError\nDocumentation required")
        return
    while True:
        time.sleep(0.5)
        print(f"Hello\n{test}\n\n")
        time.sleep(0.5)
        rr = int(input("0 for Exit: "))
        if rr == 0:
            return
def c():
    while True:
        print("Option")
        rr = int(input("0 for Exit: "))
        # match rr:
        #     case :
        
        if rr == 0:
            break
    # def d():
    #         while True:
    #             rr = int(input("0 for Exit: "))
    #             print("Hello")
    #             if rr == 0:
    #                 break
doc = ""
beer = "" #skip current shell
glass =     "" #check current shell type
cigar =    "" #heal 1 life 
Handsaw =  "" #double next shotgun damage 
Handcuffs = "" #cuffed side, skip 1 turn 
phone = "" #Tells you random loaded shell = 3rd shell is LIVE beer = skip current shell
pills = "" #50% chance to heal 2 life, 50% chance to lose 1 life
Invertor = ""   #change current shell type to opposite (LIVE to BLANK, BLANK to LIVE)
adrenaline = "" #allows to steal dealer item 
while True:
        time.sleep(0.5)
        print("\nMenu Game")
        time.sleep(0.5)
        print("Play game: 1")
        time.sleep(0.5)
        print("Document: 2")
        time.sleep(0.5)
        print("Option :3")
        time.sleep(0.5)
        print("Cheat sheet: 4")
        time.sleep(0.5)
        print("Exit: 5")
        ex = int(input("\n"))
        if ex == 5 :
            time.sleep(0.5)
            print("Good luck")
            break
        elif ex == 1 :
            a(doc)
        elif ex == 2 :
            doc= b(doc)
        elif ex == 3 :
            c()
        # elif ex == 4 :
        #     d()

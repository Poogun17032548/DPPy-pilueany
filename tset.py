none = "exit"
beer =  "beer" #skip current shell
glass =     "glass" #check current shell type
cigar =    "cigarette" #heal 1 life 
Handsaw =  "handsaw" #double next shotgun damage 
Handcuffs = "handcuffs" #cuffed side, skip 1 turn 
phone = "phone" #Tells you random loaded shell = 3rd shell is LIVE 
pills = "pills" #50% chance to heal 2 life, 50% chance to lose 1 life
Invertor = "Invertor"   #change current shell type to opposite (LIVE to BLANK, BLANK to LIVE)

item = [none,beer,glass,cigar,Handcuffs,Handsaw,phone,pills,Invertor]
status = [1] * len(item)


def test(item_list):
    while True:
        match item_list:
            case 1:
                sys1 = int(input(f"{item[item_list]}\n1: ON, 0: OFF\n"))
                return sys1
            case 2:
                sys2 = int(input(f"{item[item_list]}\n1: ON, 0: OFF\n"))
                return sys2
            case 3:
                sys3 = int(input(f"{item[item_list]}\n1: ON, 0: OFF\n"))
                return sys3
            case 4:
                sys4 = int(input(f"{item[item_list]}\n1: ON, 0: OFF\n"))
                return sys4
            case 5:
                sys5 = int(input(f"{item[item_list]}\n1: ON, 0: OFF\n"))
                return sys5
            case 6:
                sys6 = int(input(f"{item[item_list]}\n1: ON, 0: OFF\n"))
                return sys6
            case 7:
                sys7 = int(input(f"{item[item_list]}\n1: ON, 0: OFF\n"))
                return sys7
            case 8:
                sys8 = int(input(f"{item[item_list]}\n1: ON, 0: OFF\n"))
                return sys8
            case 0:
                break
print(status[3])
# choose = int(input("item : "))
# sys1 = 1
# sys1 = test(choose)
# sys2 = 1

# if item_list == 1 :
#     print(f"{item[choose]} ON")
# else :
#     print(f"{item[choose]} OFF")

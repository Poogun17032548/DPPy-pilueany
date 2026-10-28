num1 = int(input("Give me the first number: "))
num2 = int(input("Give me the second number: "))
print("Thank you!")
operator = ["+","-","/","*"]
for i in operator:
    print(f"{num1} {i} {num2} = {eval(f'{num1} {i} {num2}')}")
try:
    number = int(input("INSERT:    "))
    result = 100 / number
    print(result)
# except TypeError:
#     print("not int")
except ValueError:
    print("wrong value")
except ZeroDivisionError:
    print("you cannot divide with zero")
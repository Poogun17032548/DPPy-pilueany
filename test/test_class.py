#

class car:
    def __init__(self,color,brand,price):
        self.color = color
        self.brand = brand
        self.price = price
    def sales(self,amount):
        self.price -= amount
        print(self.brand, "has",self.price,"price left")


ow1 = car("green","toyota",1000000)
ow2 = car("pink","honda",200000)
print(ow1.price)
print(ow2.price)

car.sales(10000)
ow2.sales(100)

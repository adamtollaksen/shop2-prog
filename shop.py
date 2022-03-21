from ast import And
from tracemalloc import stop
from typing import List


class Item: 
    def __init__(self, name, price): 
        self.name = name 
        self.price = price         

items = [] 
items.append(Item('banan', 1))
items.append(Item('äpple', 2))
items.append(Item('godisbit', 5))
items.append(Item('monster', 20))
items.append(Item('köttbullar', 45))
items.append(Item('oxfile', 60))
items.append(Item('öl', 70))
items.append(Item('strumpor', 100))
items.append(Item('kallingar', 120))
items.append(Item('huvtröja', 400))
items.append(Item('jacka', 1000))
items.append(Item('bilmotor', 100000))
items.append(Item('båtmotor', 200000))
items.append(Item('dörr', 1500))
items.append(Item('allhjul',800))
items.append(Item('skärm', 3500))
items.append(Item('dator', 25000))
items.append(Item('jet', 350000000))

choice = ""
money = int(input("How much money do you have on you right now?(number only) "))
print("Welcome to the shop!")
choice = input("Do you want to buy anything? (yes/no)")
while choice == "yes":
    if choice == "yes":
        print("Here are our current items")
        for Item in items:
            print(Item.name, " ", Item.price)
        print("Your current balance is: ", money)
        buy = str(input("What do you want to buy? (Say 'exit' if you want to leave) "))
        if "exit":
            print("bye!")
            quit()

        for Item in items:
            if(Item.name == buy):
                if(Item.price < money):
                    print("You bought", buy, "!")
                    money -= Item.price
                    print("you now have", money)
                else:
                    print("You either said something that we don't have or you don't have enough money.")
                    quit()
            elif "exit":
                print("You either said something that we don't have or you don't have enough money.")
                quit()

print("Bye! Have a good day!")



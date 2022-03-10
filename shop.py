def Main():
    input("Welcome to the shop, would you like to enter?(yes/no) ")
    if "yes":
        print("Welcome!")
        money = input("How much money do you have on you right now?(number only) ")
        print("Your current balance is: ", money)
    
    print("Here are our current items in the shop. Is there anything you're looking to buy?(answer with the name of the item you want to buy): ")

    elif "no":
        print("Have a good day!")

"""
class items: 
    def __init__(self, name, price): 
        self.name = name 
        self.roll = price
          
list = [] 
  
list.append( items('banan', 1) )
list.append( items('äpple', 2) )
list.append( items('godisbit', 5) )
list.append( items('monster', 20) )
list.append( items('köttbullar', 45) )
list.append( items('oxfile', 60) )
list.append( items('bilmotor', 100 000) )
list.append( items('båtmotor', 200 000) )
list.append( items('dörr', 1 500) )
list.append( items('allhjul', 800) )
list.append( items('skärm', 3500) )
list.append( items('dator', 25 000) )
list.append( items('jet', 350 000 000) )

items=[] 



"""
Main()
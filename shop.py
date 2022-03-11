from tracemalloc import stop



class items: 
    def __init__(self, name, price): 
        self.name = name 
        self.price = price
          
list = [] 
  
list.append( items('banan', 1))
list.append( items('äpple', 2))
list.append( items('godisbit', 5))
list.append( items('monster', 20))
list.append( items('köttbullar', 45))
list.append( items('oxfile', 60))
list.append( items('öl', 70))
list.append( items('strumpor', 100))
list.append( items('kallingar', 120))
list.append( items('huvtröja', 400))
list.append( items('jacka', 1000))
list.append( items('bilmotor', 100000))
list.append( items('båtmotor', 200000))
list.append( items('dörr', 1500))
list.append( items('allhjul',800))
list.append( items('skärm', 3500))
list.append( items('dator', 25000))
list.append( items('jet', 350000000))



input("Welcome to the shop, would you like to enter?(yes/no) ")
if "yes":
    print("Welcome!")
    money = input("How much money do you have on you right now?(number only) ")
    print("Your current balance is: ", money)
else:
    print("Have a good day!")

input("Here are the things you can afford. Is there anything you're looking to buy?(answer with the name of the item you want to buy): ")

for i in range(0,len(l)):
    if(list[i]<money):
        print(list[i],end=" ")
print(items) 



        




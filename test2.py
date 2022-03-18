
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


for Item in items:
    print(Item.name)


"""
print('\n'.join(map(str, items.price)))
"""


        




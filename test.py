# Python3 code here creating class
class items: 
    def __init__(self, name, price): 
        self.name = name 
        self.roll = price
   
# creating list       
list = [] 
  
# appending instances to list 
list.append( items('banan', 0) )
list.append( items('äpple', 0) )
list.append( items('godisbit', 0) )
list.append( items('monster energy', 0) )
list.append( items('köttbullar', 0) )
list.append( items('vegetarisk blodig nymördad oxfile', 0) )
list.append( items('x', 0) )
list.append( items('x', 0) )
list.append( items('x', 0) )
list.append( items('skärm', 0) )
list.append( items('dator', 0) )
list.append( items('jet', 0) )
  
for obj in list:
    print( obj.name, obj.price, sep =' ' )
  
# We can also access instances attributes
# as list[0].name, list[0].roll and so on.
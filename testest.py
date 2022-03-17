from unicodedata import name


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1=[]
p1.append(Person("John", 36))



print(p1.name)
print(p1.age)

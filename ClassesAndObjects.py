#Class MyClass
class MyClass: #Class
    x =5 
p1 = MyClass() #Object
print(p1.x)

###########################################
#Class Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Ibrahim", 35)
p2 = Person("Sarinat", 30)

print(p1.name)
print(p2)
print(p1.age)
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

###########################################
#Object Method: A function in an object.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myFunction(self):
        print("Hello my name is " + self.name)

p1 = Person("Salau", 35)
p1.myFunction()

###########################################
#self parameter can be named any name. eg;
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1.age = 39 #Update object property
del p1.age #Delet object property
del p1 #Delete object

print(p1.age) #This will throw AttributeError for missig 'age' attribute
print(p1) #This will throw NameError after deleting p1 object
p1 = Person("Ibrahim", 36)
p1.myfunc()


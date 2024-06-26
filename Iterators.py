"""Iterator is a countable object(s), consisting of
 __iter__() and __next__() methods"""
#Example
def iterFunction():
    mytuple = ("appple", "mango")
    myiter = iter(mytuple)

    #String is iterable too
    myString = "Air"
    myAirIt = iter(myString)

    #Looping through an Iterator
    loopThis = ("Adam", "Eve")

    for x in loopThis:
        print(x)


    #Loop through String aswell
    thisString = "salau"
    
    for i in thisString:
        print(i)

    #Printing interFunction    
    print(next(myiter))
    print(next(myiter))

    #Print Air string
    print(next(myAirIt))
    print(next(myAirIt))
    print(next(myAirIt))

iterFunction()


#Create amd stop iterator
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for i in myiter:
    print(i)


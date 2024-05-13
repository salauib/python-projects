"""A for loop is used for iterating over a sequence 
(that is either a list, a tuple, a dictionary, a set, or a string). 
"""
#Print each fruit in a list of fruits
def fruitList():
    fruits = ["mango", "guava", "cashew"]
    for x in fruits:
        print(x)
fruitList()

#Strings are also iterable
def main():
    for x in "Banana":
        print(x)
main()

#Break out of loop before it loops to the end
def breakLoop1():
    fruits = ["mango", "banana", "cherry"]
    for i in fruits:
        print(i)
        if i == "banana":
            break#break after print statement
breakLoop1()

#Break out of loop before it loops to the end
def breakLoop2():
    fruits = ["cherry", "banana", "mango"]
    for i in fruits:
        if i == "banana":
            break#break before print statement
        print(i)
breakLoop2()
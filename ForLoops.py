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
            break #break after print statement
breakLoop1()

#Break out of loop before it loops to the end
def breakLoop2():
    fruits = ["cherry", "banana", "mango"]
    for i in fruits:
        if i == "banana":
            break #break before print statement
        print(i)
breakLoop2()

#Continue statement stops at a point, then continues till end
def continueLoop():
    fruits = ["pineapple", "banana", "mango"]
    for i in fruits:
        if i == "pineapple":
            continue #breaks, then continues
        print(i)
continueLoop()

#range() function prints from 0, ends, skips the last number.
def rangeFunction1():
    x = 6
    for i in range(x):
        print(i)
rangeFunction1()

#range() function prints from a given number, ends, skips the last number.
def rangeFunction2():
    x = 6
    y = 10
    for i in range(x, y):
        print(i)
z = rangeFunction2()

#range() function can also have third parameter that increaments the range
def rangeFunction3():
    w = 1
    x = 10
    y = 3
    for i in range(w, x, y):
        print(i)
z = rangeFunction3()

#Else in For Loop will not execute if the loop is stopped by break statement
def elseInForLoop():
    for x in range(1):
        print(x)
    else:
        print("Ends!")
elseInForLoop()

#Break the loop when x is 3, and see what happens with the else block
def breakInForLoop():
    for i in range(5):
        if i == 3: break
        print(i)
    else:
        print("Finnally!")
breakInForLoop()

#Nested loops
def nestedLops():
    adj = ["red", "big", "tasty"]
    fruits = ["apple", "banana", "cherry"]

    for x in adj:
        for y in fruits:
            print(x, y)

nestedLops()

#Pass Statement
def passStatement():
    for x in [0, 4, 2, 7]:
        pass
passStatement()
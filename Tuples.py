####################################################
#A tuple is a collection of data which is ordered and unchangeable
#Create a Tuple
def main():
    aTuple = ("apple", "mango", "orange")

    print(aTuple)
    print(len(aTuple))
results = main()

#####################################
#One item Tuple, don't miss the last comma (,)
def main():
    aTuple = ("apple",)

    print(type(aTuple))
    print(len(aTuple))
results = main()

#####################################
#String, int and boolean data type
def main():
    thisTuple1 = ("apple", "mango", "cherry")
    thisTuple2 = (1, 2, 3, 4, 5)
    thisTuple3 = (True, False, False)
    thisTuple4 =("abc", 34, 4, True, False, 'good')#Tuple with different data types

    print(type(thisTuple1))
    print(type(thisTuple2))
    print(type(thisTuple3))
    print(type(thisTuple4))
    print(thisTuple4[3]) #Access tuple items
    print(thisTuple4[-4:-1]) #Access tuple items with negative index

finalAnswer = main()

################################
#Using tuple() methond to construct a tuple
def main():
    thisTuple = tuple(("man", "woman", "he", "she"))
    print(thisTuple)

finalAnswer = main()

#############################
#Check if an item is present inside a tuple
def main():
    thisTuple = ("one","two","three", "four", "five")
    if "three" in thisTuple:
        print("Yes!")
    else:
        print("No!")
finalAnswer = main()

#############################
#Manipulate tuple by converting it to List and change back to tuple
def main():
    x = ("a", "b", "c", "d", "e", "g")
    y = list(x)
    y[5] = "f"
    y.append("h")#Add an itel into the converted tuple
    x = tuple(y)

    print(x)#print original tuple
    print(y)#print the manipulated tuple version (list)

    print(type(x))#print type
    print(type(y))#print type

finalAnswer = main()

################################
#Add a tuple to a tuple
def main():
    thisTuple = ("apple", "mango", "guava")
    y = ("cashew",)
    thisTuple += y

    print(thisTuple)

main()

#######################
#Remove item from tuple
#Convert the tuple to list, remove the item, convert back to tuple
def main():
    thisTuple = ("aa", "bb", "cc", "dd", "ee")
    x = list(thisTuple)
    x.remove("bb")
    thisTuple = tuple(x)

    print(thisTuple)

main()

# #Delete tuple completely
# def main():
#     thisTuple10 = ("A", "C", "D", "E")
#     del thisTuple10

#     print(thisTuple10)
# main()

#############################
#Unpacking a tuple means assigning it to variable(s)
def main():
    numberedTuple = (1, 2, 3, 4, 5)
    (a, b, c, d, e) = numberedTuple

    print(a, b, c, d, e)
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)

main()

#################################
#Loop Tutle
def main():
    myTutle = ('apple', 'mango', 'guava')
    for u in myTutle:
        print(u)
main()

#################################
#Loop through index number using for Loop
def main():
    myTuple = ('pineapple', 'mango', 'guava')
    for u in range(len(myTuple)):
        print(u, myTuple[u])
main()

#################################
#Loop through index number using while Loop
def main():
    myTuple = ('pineapple', 'mango', 'guava')
    
    i = 0
    while i < len(myTuple):
        print(i, myTuple[i])
        i += 1
main()

#################################
#Join Tuple using + operator
def main():
    myTuple = ('pineapple', 'mango', 'guava')
    yourTuple = ('AA', 'BB', 'CC')
    ourTuple = myTuple + yourTuple
    y = yourTuple * int(3.56)#Multiply tuple by a given number
    x = y.count("AA")

    print(ourTuple)
    print(y)
    print(x)

main()
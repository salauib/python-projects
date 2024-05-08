#Creat a LIST
def main():
    myList = ["Apple", "Mango", "Guava", "mango"]
    myList2 = [1, 2, 3, 4, 8, 26, 5]
    myList22 =[6, 7, 22, 33, 4, 00, 0, 10]
    myTuple = ("Kiwi", "Orange")
    myList3 = [True, False, False]
    myList4 = ["abc", 34, True, 40, "male"]
    myList5 = list(("Guava", "Berry", "Broccoli", "Cashew", "Orange", "Melon", "Banana"))

    #Add a list to anothe list using extend method
    myList2.extend(myList22)

    #You can add an iterable data type to list eg Tuple
    myList2.extend(myTuple)

    #Change a specific item value in a list
    myList3[2] = "True"
    myList4[1:3] = [35, False]

    #Insert an item into a list
    myList4.insert(4, "she")
    myList4.append("them")

    #Remove an item from a list using remove() method
    myList2.remove("Orange")
    myList2.remove(22)

    #Remove a specific item from a list using pop() method
    myList2.pop(12)
    myList2.pop()

    #Delete a specific item from a list using del keyword
    del myList5[0]
    myList5.clear()

    #Check if an item is in a list
    if True in myList3:
        print("Yes!")
    else:
        print("No!")

    print(len(myList)) #List length
    print(len(myList[1])) #Length of list's item number 2
    print(myList[3]) #Last item in the list
    print(myList)
    print(myList2)
    print(myList3)
    print(myList4)
    print(myList4[-3:-1])
    print(myList5[2:5])
    print(myList5)
main()


#Looping through List using for loop
def main():
    myList = ["Apple", "Mango", "Guava", "mango"]

    for i in myList:
        print(i)
main()

#Looping through List using while loop
def main():
    myList2 = [1, 2, 3, 4, 8, 26, 5]

    i = 0
    while i < len(myList2):
        print(myList2[i], end=", ")
        i += 1
main()

#Looping using List comprehension
def main():
    myList22 =[6, 7, 22, 33, 4, 00, 0, 10]
    [print(k) for k in myList22]
main()


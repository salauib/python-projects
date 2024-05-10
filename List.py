######################################
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

######################################
#Looping through List using for loop
def main():
    myList = ["Apple", "Mango", "Guava", "mango"]

    for i in myList:
        print(i)
main()

############################################
#Looping through List using while loop
def main():
    myList2 = [1, 2, 3, 4, 8, 26, 5]

    i = 0
    while i < len(myList2):
        print(myList2[i], end=", ")
        i += 1
main()

###################################################
#Looping using List comprehension
def main():
    myList22 =[6, 7, 22, 33, 4, 00, 0, 10]
    [print(k) for k in myList22]
main()

###################################################
#List Comprehension
#Get items from a list into a new list
def main():
    fruits = ["apple", "banana", "cherry", "kiwi", "mango", "Cashew"]
    newList = []

    for x in fruits:
        if "e" in x:
            newList.append(x)
    print(fruits)       
    print(newList)
theResult = main()

############################
#Using range() function to create an iterable list, with condition
def main():
    newList = [x for x in range(10) if x < 7]
    print(newList)
    print(len(newList), end=".\n")
main()

#########################################
#Sorting List using sort() method
def main():
    numbered_list = [ 100, 30, 33, 82, 23]
    this_list = ["orange", "mango", "kiwi", "pineapple", "banana"]
    reverse_list = ["kemi", "adam", "bello", "oye", "salau"]

    numbered_list.sort() #ALphabetically
    this_list.sort() #Numerically
    reverse_list.sort(reverse= True)

    print(numbered_list)
    print(this_list)
    print(reverse_list)
main()

########################################
#Customized sort Function (key = function)
def main():
    def myFunc(n):
        return abs(n - 50)

    thisList = [100, 50, 65, 82, 23]
    thisList.sort(key = myFunc)

    print(thisList)
main()

#########################################
#Case sensitive sorting, sorts capital befor ascending small letters
def main():
    thislist = ["banana", "Orange", "Kiwi", "cherry"]
    thislist.sort()

    print(thislist)
main()

#################################
#Case-insensitive, sorts in ascending other with or without 
#...words starting with capital letter
def main():
    thislist = ["banana", "Orange", "Kiwi", "cherry"]
    thislist.sort(key = str.lower)
    
    print(thislist)

main()

#################################
#Reverses the list regardless of th alphabet using reverse() method
def main():
    thislist = ["banana", "Orange", "Kiwi", "cherry"]
    thislist.reverse()
    
    print(thislist)

main()

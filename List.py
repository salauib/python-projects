#Creat a LIST
def main():
    myList = ["Apple", "Mango", "Guava", "mango"]
    myList2 = [1, 2, 3, 4, 8, 26, 5]
    myList3 = [True, False, False]
    myList4 = ["abc", 34, True, 40, "male"]
    myList5 = list(("Guava", "Berry", "Broccoli", "Cashew"))

    print(len(myList)) #List length
    print(len(myList[1])) #Length of list's item number 2
    print(myList[3]) #Last item in the list
    print(myList)
    print(myList2)
    print(myList3)
    print(myList4)
    print(myList4[:2])
    print(myList5[-3])
main()
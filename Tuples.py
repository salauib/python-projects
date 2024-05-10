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
    thisTuple4 =("abc", 34, 4, True, False, 'good')

    print(type(thisTuple1))
    print(type(thisTuple2))
    print(type(thisTuple3))
    print(type(thisTuple4))
    print(thisTuple4[3])

answer = main()


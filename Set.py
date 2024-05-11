######################
#Set
def main():
    myset = {'apple', 'banana', 'berry'}
    yourset = {'man', 'woman', 'human'}

    x = list(yourset)
    x.append('male')
    
    print(myset)
    print(x)
    print(type(myset))
    print(type(yourset))
    print(type(x))
main()

######################
#Note: True and 1 is considered the same value in set
#False and 0 are also the same
def main():
    thisset = {"apple", False, "banana", "cherry", True, 1, 2, 1, 0}
    
    print(thisset)
    print(len(thisset))
    print(type(thisset))
main()

##################
#Using set() constructor to create set
def main():
    thisset = set(('apple', 'mango', 'pineapple'))

    print(thisset)
    print(type(thisset))
main()
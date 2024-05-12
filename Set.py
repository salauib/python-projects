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

##################
#Accessing set items usinf for in methods
def main():
    thisset = set(('apple', 'mango', 'pineapple'))
    thisset2 = set(('man', 'woman'))

    thisset.add('tomatoes')#Added item to set using add() method
    thisset.update(thisset2)#Added to a set from another set using update() method. Dict, list, tuple can also be added
    
    thisset.remove('man')#Remove item from set with remove() method
    thisset.discard('woman')#Remove item from set with discard() method
    thisset.pop()#Remove a random item from set with pop() method
    #thisset.clear()#Empties set completely
    #del thisset #Deletes set completely
    
    for x in thisset:
        print(x)

    print(thisset)
    print(type(x))
    print("mango" in thisset)#Checked if an item is presnt in set
    print("apple" not in thisset)#Checked if an item is not presnt in set
main()

#########################
#Loop through a set
def main():
    thisset = {'one', 'two', 'three'}

    for v in thisset:
        print(v)

main()

##############################
#Join two or more set(s) with different methods
def main():
    #Join two sets with union() method
    set1 = {'a', 'b', 'c'}
    set2 = {1, 2, 3}

    set3 = set1.union(set2)

    #Join multiple sets using union() method
    set111 = {'aaa', 'bbb', 'ccc'}
    set222 = {111, 222, 333}
    set333 = {'John', 'Sam', 'Ali'}
    set444 = {'yam', 'beans', 'cassava'}

    multSets = set111.union(set222, set333, set444)

    #Another way to join set using |
    set11 = {'aa', 'bb', 'cc'}
    set22 = {11, 22, 33}

    set33 = set11 | set22

    #Can also join sets using multiple | on a single line
    set11 = {'aa', 'bb', 'cc'}
    set22 = {11, 22, 33}
    set33 = {'he', 'she'}

    set44 = set11 | set22 | set33

    #Join set and tuple
    x = {'a', 'b', 'c', 'd'}
    y = (1, 2, 3, 4, 5)

    z = x.union(y)

    #update() method also inserts from one set to the other
    d = {'a', 'b', 'c', 'd'}
    e = (1, 2, 3, 4, 5)

    d.update(e)

    #intersection() mothod returns only the item that is present in both sets
    x = {'a', 'b', 'c', 7, 'd'}
    y = (1, 2, 3, 'a', 4, 5, 7)

    zz = x.intersection(y)

    # & operator can be used instead of intersection method
    x1 = {'a', 8, 'b', 'c', 'd'}
    y1 = {1, 2, 'b', 3, 4, 5, 8}

    z1 = x1 & y1

    print(set3)
    print(multSets)
    print(set33)
    print(set44)
    print(z), print(type(z))
    print(d)
    print(zz)
    print(z1)
main()

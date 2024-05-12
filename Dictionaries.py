#Dictionary
def main():
    dict1 = {"brand": "Toyota",
             "model": "Sienna",
             "year": 1996,
             "year": 2004} #Duplicate values overwrites existing values
    

    #dict() method is a constructor
    mydict = dict(name = "salau",
                  age = 35,
                  country = 'Poland')
    
    #Accesing dictionary
    x = dict1.get("brand")
    y = dict1["model"]
    z = dict1.keys() #Returns all keys in dict
    v = dict1.values() #Returns all values in dict

    #Add new item(s) to dictionary
    dict1["color"] = "black"

    #Get a list of key:value pairs
    xx = dict1.items()

    print(dict1)
    print(len(dict1))
    print(type(dict1))
    print(mydict)
    print(type(mydict))
    print(x)
    print(y)
    print(z)
    print(v)
    print(xx)
main()

#################################
#Check if a key exists in a dict
def main():
    dict1 = {"brand": "Toyota",
             "model": "Sienna",
             "year": 2004}

    dict1["model"] = "Corolla" #Change model item's value
    dict1["country"] = "Japan" #Add item to dict
    dict1.update({"color": "Blue"}) #Add item to dict
    dict1.pop("country") #Remove item from dict
    dict1.popitem() #Remove item from dict
    del dict1["year"] #Remove item from dict, also can delete dict completely
    dict1.clear() #Empties the dict

    if "brandt" in dict1:
        print("YES!")
    else:
        print("NO!")

    print(dict1.items())
    print(len(dict1))
main()

################################
#Loop through dictionary
def main():
    firstDict = {"brand": "Mercedeze",
                 "model": "AMG",
                 "year": 2024}
    
    for i in firstDict:
        print(i)
        print(firstDict[i], end=", \n")

    for j in firstDict.values():
        print(j)
    
    print(firstDict)
main()

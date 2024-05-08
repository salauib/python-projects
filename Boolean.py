def myBoolean():
    x = "Name"
    y = 55
    print(10 >= 9)
    print(bool(5))
    print(bool("Yes"))
    print(bool(x == "Age"))
    print(bool(y >= 56))
    print(bool(0))
    print(bool(""))
    print(bool([]))
    print(bool({}))
    print(bool(()))
    print(bool(None))
    print(bool(False))
    print(bool(True))
myBoolean()

#A function that returns a boolean value
def main():
    return True

if main():
    print("YES!")
else:
    print("NO!")
print(main())

#Check if an object is an integer or not using isinstance() function
def isAnInteger():
    x = "Letter"
    print(isinstance(x, int))
isAnInteger()
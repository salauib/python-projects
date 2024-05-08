# #CREATED GLOBAL AND LOCAL VARIABLES
# #Global variale
# globalvariable = input("Enter your name please?\n ").capitalize()

# def main():
#     #Local variable
#     localVariable = "python programmer"

#     #Making a local variable glocal with keyword "global"
#     global x
#     x = "That's right!"

#     print(globalvariable + " is a  " + localVariable)
# main()

# print(globalvariable)
# print(x)





#Data Types
#Setting and getting data types

def main():
    a = "Salau"
    b = 35
    c = 20.3
    d = 2j
    e = ["mango", "orange"]
    f = ("mango", "orange")
    g = range(3)
    h = {"name": "Salau", "age": 35,}
    i = {"man", "woman"}
    j = frozenset({"apple", "berry"})
    k = True
    l = b"Hello"
    m = bytearray(7)
    n = memoryview(bytes(7))
    o = None

    print(type(a))
    print(type(b))
    print(type(c))
    print(type(d))
    print(type(e))
    print(type(f))
    print(type(g))
    print(type(h))
    print(type(i))
    print(type(j))
    print(type(k))
    print(type(l))
    print(type(m))
    print(type(n))
    print(type(o))
main()
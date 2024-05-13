#Creating and calling functions
def myFunction(): #Creating function

    print("I just created self function")

myFunction() #Calling function

##########################
#Passing parameter(s) and argument(s) into a function
def myFunction(fname):#Parameter passed to function
    print(fname + " is a python programmer!")

myFunction("Salau")#Argument passed into a function call
myFunction("Sarinat")#Argument passed into a function call

#############################
#Pass and * into a function if you do not know how many parmeters would come in
def myFunction(*sons):
    print(sons[2] + " is my first son.")

myFunction("Ali", "Abubakry", "Ibrahim")

#############################
#Keyword arguments
def myFunction(child1, child2, child3):
    print( child3 + " is my first son.")

myFunction(child2 ="Ali", child3 = "Abubakry", child1 = "Ibrahim")

#############################
#Default keyword
def myFunction(country = "Nigeria"):
    print("I am from Lagos, " + country)

myFunction()
myFunction("Sweden")
myFunction("Poland")
myFunction("Switzerland")

#############################
#Passing a list as an argument
def myFunction(food):
    for x in food:
        print(x)

fruits = ["apple", "mango", "berry"]

myFunction(fruits)

############################
#Return a value from a function
def returnFunction(x):
    return 5 * x

print(returnFunction(5))
print(returnFunction(1))
print(returnFunction(25))


########################
#Pass statement
def passStatement():
    pass 
""" having an empty function definition like this,
 would raise an error without the pass statement
    """
 
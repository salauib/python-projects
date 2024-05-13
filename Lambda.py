#A lambda is a function, takes any amount of arguments,
#... but with only one expression
#Syntax => [lambda arguments: expression]
def lambdaFunction():
    x = lambda a: a + 10
    print(x(5))
lambdaFunction()

###################################
#Lambda can take multiple arguments
def lambdaFunction():
    x = lambda a, b : a * b
    print(x(5,6))
lambdaFunction()
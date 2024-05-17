"""When you create a variable inside or 
outside of a function, that is a SCOPE"""

#Local Scope: Accessible only withing a function
def localScope():
    x = 2
    print(x)
localScope()

#Another Local Scope
#Function inside Function
#x scope is avaible to innerFun() inside firstFun() only
def firstFunc():
    x = 3
    def innerFun():
        print(x)
    innerFun()
firstFunc()

#Global Scope
xx = 4
def globalFunc():
    x = 1
    print(x)
    print(xx)

globalFunc()
print(xx)

#global kewyword
#Use global keyword to make local variable become global
def globalVariable():
    global x
    x = 300
globalVariable()
print(x)

#nonlocale kewyword
"""If you use the nonlocal keyword, 
the variable will belong to the outer function"""
def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello" #x becomes global to myfunc1(), overrides "Jane"
  myfunc2()
  return x

print(myfunc1())
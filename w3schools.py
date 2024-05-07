#Global variale
globalvariable = input("Enter your name please?\n ").capitalize()

def main():
    #Local variable
    localVariable = "python programmer"

    #Making a local variable glocal with keyword "global"
    global x
    x = "That's right!"

    print(globalvariable + " is a  " + localVariable)
main()

print(globalvariable)
print(x)
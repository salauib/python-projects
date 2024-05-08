#String operations
def main():
    #looping through a String
    for x in "salau":
        print(x.capitalize())
main()

#Strings are Arrays 
def main():
    a = "ibrahim"
    print("Letter in position 1 is: " + a[1].upper())
main()

#String length using len() function
def main():
    a = "Life's Good"
    print("The length of a is: " + str(len(a)))
main()

#Checking if a character is present in a Str
def main():
    textMessage = "My wife makes me happy!"
    print("makes" in textMessage.lower())
main()

#Checking if a character is present in a Str using If statement
#Using keywords "in" or "not in"
def main():
    myMessage = "Python is fun!"
    if "Python!" not in myMessage:
        print("Yes")
    else:
        print("No")
main()

#Slicing Strings using slice syntax
def main():
    txt = "Programmer"
    print(txt[1:7])
main()

#Remove whitespace from program
def main():
    a = " Prome queen is here! "
    print(a.upper().strip())
main()

#Replace string
def main():
    a = "Mallam, Audu!"
    print(a)
    print(a.replace("M", "S"))
    print(a.split(",")) #Split string output
main()


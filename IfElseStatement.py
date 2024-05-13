######################################
#If ... Else Statements
def main():
    a = 30
    b = 5
    c = a + b

    if a < b:
        print(True)
    elif b > a:
        print(True)
    elif c == a + b:
        print("That's right!")
    else:
        print("Over!")

main()

##########################
#A line code of if statement
def oneLineCode():
            aa = 2
            bb = 3
            if aa < bb: print("Yes!")
oneLineCode()

##########################
#A line code of if ... else statement
def ifElseStatement():
            aa = 2
            bb = 333
            print("A") if aa > bb else print("BB")
ifElseStatement()

################################
#Logical operator (and)
def logicalOperator():
            aa = 2
            bb = 333
            cc = aa * bb
            
            if aa < bb and aa * bb == cc:
                   print("Confirm!")
logicalOperator()

################################
#Logical operator (or)
def logicalOperator():
            aaa = 2
            bbb = 333
            ccc = aaa * bbb
            
            if aaa > bbb or ccc < 100:
                   print("Confirm!")
            else:
                   print("Oops!")
logicalOperator()

################################
#Logical operator (not)
def logicalNot():
            aaa = 2
            bbb = 333
            ccc = aaa * bbb
            
            if not aaa < bbb:
                   print("Yes!")
            else:
                   print("No!")
logicalNot()

################################
#Nested if statements
def nestedIf():
        x = 31
        if x > 10:
                print("Above ten,")
                if x > 20:
                        print("and also above 20!")
                else:
                        print("but not above 20.")
nestedIf()

################################
#pass statement, when if statement has no code to run yet.
def passStatement():
        x = 31
        if x > 50:
                pass
passStatement()
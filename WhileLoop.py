##################################
#while loop, as long as a condition is true
def main():
    i = 1
    while i < 5:
        print(i)
        i += 1
main()

##################################
#break statement stops the loop even if the while is true
def main():
    i = 1
    while i < 5:
        print(i)
        if i == 3:
            break
        i += 1
main()

##################################
#continue statement omits a line or more, then continue to execute the rest of the program
def main():
    i = 1
    while i < 8:
        i += 1
        if i == 3:
            continue
        print(i)
main()

##################################
#else statement executes whe the conditon is false
def main():
    i = 1
    while i < 5:
        print(i)
        i += 1
    else:
        print("i is no longer less than 5")
main()
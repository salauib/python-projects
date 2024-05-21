# def house():
#     name = input("What's your name? ").capitalize()

#     #Using if statement
#     if name == "Salau" or name == "Sarinat":
#         print("Married")
#     elif name == "Balogun":
#         print("In Lagos")
#     else:
#         print("Who?")

# house()

def house():
    name = input("What's your name? ").capitalize()
    #Using match statement
    match name:
        case "Salau" | "Sarinat" | "Ibrahim":
            print("Married")
        case "Balogun":
            print("In Lagos")
        case _:
            print("Who?")
house()
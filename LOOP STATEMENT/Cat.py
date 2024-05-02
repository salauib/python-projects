# def cat():
#     i = 0

#     while i < 5: #Loop using WHILE statement
#         print(i)
#         i += 1

# cat()

# def cat():
#     for i in range(3): #Loop using WHILE statement
#         print("Hello")

# cat()

# def cat():
#     print("Hello\n" * 5, end="")

# cat()

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n    

def meow(n):
    for _ in range(n):
        print("meow")

main()
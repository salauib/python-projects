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

def cat():
    while True:
        n = int(input("What's n? \n"))
        if n > 0:
            break

    for _ in range(n):
        print("meow")

cat()
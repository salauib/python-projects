def main():
    name = input("What is your name? ")
    hello(name)


def hello(to = "Somebody"):
    print("Hello,", to)

hello()
main()
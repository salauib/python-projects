"""NOTE: Python has not built-in support for Arrays, 
Lists can be used instead"""
#Arrays
def carsArray():
    cars = ["Toyota", "Ford", "Benz"]

    cars[1] = "Volvo" #Update an array
    w = len(cars)#print the length of an array

    #Loop through an array
    for x in cars:
        print(x)

    print(cars)
    print(w)
carsArray()
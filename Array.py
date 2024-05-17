"""NOTE: Python has not built-in support for Arrays, 
Lists can be used instead"""
#Arrays
def carsArray():
    cars = ["Toyota", "Ford", "Benz"]

    cars[1] = "Volvo" #Update an array
    cars.append("Honda") #Added to array
    
    #Remove from array, use remove() or pop() methods
    cars.remove("Benz")
    
    w = len(cars)#print the length of an array

    #Loop through an array
    for x in cars:
        print(x)

    print(cars)
    print(w)
carsArray()
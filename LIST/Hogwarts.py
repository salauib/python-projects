#Working with LIST using for loop
#Print out the students one after the other
# def main():
#     students = ["Salau", "Sarinat", "Oye"]
#     for student in range(len(students)):
#         print(student + 1, students[student])

# main()


#DICTIONARY
def main():
    students = {"Salau": "Lagos",
                "Sarinat": "Lagos",
                "Oye": "Lagos",
                "Balogun": "Others"}
    
    for student in students:
        print(student, students[student], sep=", ")

main()

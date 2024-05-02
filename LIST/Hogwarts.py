#Working with LIST using for loop
#Print out the students one after the other
def main():
    students = ["Salau", "Sarinat", "Oye"]
    for student in range(len(students)):
        print(student + 1, students[student])

main()
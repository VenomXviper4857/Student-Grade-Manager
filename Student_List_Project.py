Students = {}

def action_1():
    Student = input("Add a student: ").title()

    while True:
        Grade = input("Enter their grade (0-100): ")

        if Grade.isdigit():
            Grade = int(Grade)

            if 0 <= Grade <= 100:
                Students[Student] = Grade
                break
            else:
                print("Please enter a grade between 0 and 100.")
        else:
            print("Please enter a valid number.")

while True:

    Action = input("What would you like to do (select a number): \n 1. Add Student \n 2. View Students \n 3. Delete Student \n 4. Exit \n ---")

    # What happens when you exit
    if Action == "4":
        print("See you later!")
        break

    # What happens when you add a student
    elif Action == "1":

        action_1()

        while True:
            Continue = input("Would you like to add another student (Y/N): ").upper()

            if Continue == "Y":
                action_1()
            elif Continue == "N":
                break
            else:
                print("Please enter either Y or N.")

    # What happens when you want to view students
    elif Action == "2":
        if len(Students) == 0:
            print("There are no students in the list.")
        else:
            print("\nStudents:")
            for student, grade in Students.items():
                print(f"{student}: {grade}")

    # What happens when you want to delete a student
    elif Action == "3":

        while True:
            Del = input("Which student would you like to delete (enter their name): ").title()

            if Del in Students:
                del Students[Del]
            else:
                print("Student not found.")

            while True:
                Ask = input("Would you like to delete another student? (Y/N): ").upper()

                if Ask == "Y":
                    break
                elif Ask == "N":
                    break
                else:
                    print("Please enter either Y or N.")

            if Ask == "N":
                break

    else:
        print("Please pick one of the actions listed")
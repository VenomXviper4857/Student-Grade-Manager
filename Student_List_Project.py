import json

try:
    with open("students.json", "r") as file:
        Students = json.load(file)
except FileNotFoundError:
    Students = {}

def action_1():
    Student = input("Add a student: ").title()

    if Student in Students:
        print(f"{Student} already exists. Their grade will be updated.")

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

    Action = input(
        "\nWhat would you like to do (select a number):"
        "\n1. Add Student"
        "\n2. View Students"
        "\n3. Delete Student"
        "\n4. Check the average of everyone's grades"
        "\n5. Edit a student's grade"
        "\n6. Exit"
        "\n--- "
    )

    # Exit
    if Action == "6":

        with open("students.json", "w") as file:
            json.dump(Students, file)

        print("See you later!")
        break

    # Add Student
    elif Action == "1":

        action_1()

        while True:
            Continue = input("Would you like to add another student? (Y/N): ").upper()

            if Continue == "Y":
                action_1()

            elif Continue == "N":
                break

            else:
                print("Please enter either Y or N.")

    # View Students
    elif Action == "2":

        if len(Students) == 0:
            print("There are no students in the list.")

        else:
            print("\nStudents:")
            for student, grade in Students.items():
                print(f"{student}: {grade}")

    # Delete Student
    elif Action == "3":

        while True:

            student_to_delete = input(
                "Enter the name of the student you want to delete: "
            ).title()

            if student_to_delete in Students:
                del Students[student_to_delete]
                print(f"{student_to_delete} has been removed.")

            else:
                print("Student not found.")

            Ask = input("Would you like to delete another student? (Y/N): ").upper()

            if Ask == "Y":
                continue

            elif Ask == "N":
                break

            else:
                print("Please enter either Y or N.")
                break

    # Average Grade
    elif Action == "4":

        if len(Students) == 0:
            print("There are no students in the list.")

        else:
            average = sum(Students.values()) / len(Students)
            print(f"The average grade is: {average:.2f}")

    # Edit Grade
    elif Action == "5":

        while True:

            student_to_edit = input(
                "Enter the name of the student whose grade you want to edit: "
            ).title()

            if student_to_edit in Students:

                while True:
                    new_grade = input(
                        f"Enter the new grade for {student_to_edit} (0-100): "
                    )

                    if new_grade.isdigit():
                        new_grade = int(new_grade)

                        if 0 <= new_grade <= 100:
                            Students[student_to_edit] = new_grade
                            print(
                                f"{student_to_edit}'s grade has been updated to {new_grade}."
                            )
                            break

                        else:
                            print("Please enter a grade between 0 and 100.")

                    else:
                        print("Please enter a valid number.")

            else:
                print(f"{student_to_edit} is not in the student list.")

            while True:
                Continue = input(
                    "Would you like to edit another student's grade? (Y/N): "
                ).upper()

                if Continue == "Y":
                    break

                elif Continue == "N":
                    break

                else:
                    print("Please enter either Y or N.")

            if Continue == "N":
                break
    # Invalid Menu Option
    else:
        print("Please pick one of the actions listed.")

students = []

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        students.append(name)
        print("Student Added!")

    elif choice == "2":
        print("\nStudent List:")
        for s in students:
            print(s)

    elif choice == "3":
        break

    else:
        print("Invalid Choice")

students: list[dict[str, any]] = [
    {"id": 1, "name": "Dara", "age": 20, "gender": "Male", "score": 85},
    {"id": 2, "name": "Sokha", "age": 21, "gender": "Female", "score": 90},
    {"id": 3, "name": "Vanna", "age": 19, "gender": "Male", "score": 75},
    {"id": 4, "name": "Sreymom", "age": 22, "gender": "Female", "score": 95},
    {"id": 5, "name": "Bopha", "age": 20, "gender": "Female", "score": 80},
    {"id": 6, "name": "Rith", "age": 23, "gender": "Male", "score": 65},
    {"id": 7, "name": "Sokun", "age": 21, "gender": "Male", "score": 88},
    {"id": 8, "name": "Chantha", "age": 19, "gender": "Female", "score": 92},
    {"id": 9, "name": "Pisey", "age": 20, "gender": "Female", "score": 78},
    {"id": 10, "name": "Vicheka", "age": 22, "gender": "Male", "score": 84},
    {"id": 11, "name": "Malis", "age": 18, "gender": "Female", "score": 96},
    {"id": 12, "name": "Sovann", "age": 24, "gender": "Male", "score": 70},
    {"id": 13, "name": "Kanha", "age": 21, "gender": "Female", "score": 89},
    {"id": 14, "name": "Borey", "age": 20, "gender": "Male", "score": 76},
    {"id": 15, "name": "Dalin", "age": 19, "gender": "Female", "score": 93}
]

while True:
    print("\n1 : show all student")
    print("2 : show only student Female")
    print("0 : Exit")

    user_input: str = input("pls chose option : ")

    # Option 1: Show all students
    if user_input == "1":
        print("\n===== ALL STUDENTS =====")

        for student in students:
            print(student)

    # Option 2: Show only Female students
    elif user_input == "2":
        print("\n===== FEMALE STUDENTS =====")

        for student in students:
            if student["gender"] == "Female":
                print(student)

    # Option 0: Exit
    elif user_input == "0":
        print("Goodbye!")
        break

    else:
        print("Invalid option! Please try again.")

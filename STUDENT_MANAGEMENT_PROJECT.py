class Student:

    all_students = []

    def __init__(self, name, rollno, marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks

    @classmethod
    def add_student(cls):
        name = input("Enter student name: ")
        rollno = input("Enter student roll number: ")
        marks = int(input("Enter student marks: "))

        student = cls(name, rollno, marks)

        cls.all_students.append(student)

        print(f"Student {name} added successfully!")

    @classmethod
    def find_student_by_roll(cls, roll):
        for student in cls.all_students:
            if student.rollno == roll:
                return student

        return None
    
    def update_marks(self,marks):
        self.marks = new_marks

        print(f"the name was added {name} succesfully!!!!")
    @classmethod
    def display_students(cls):
        if not cls.all_students:
            print("No students found!")
            return

        print("\n----- All Students -----")

        for student in cls.all_students:
            print(
                f"Name: {student.name}, "
                f"Roll No: {student.rollno}, "
                f"Marks: {student.marks}"
            )




    @classmethod
    def update_student_marks(cls):
        roll = int(input("enter your roll number to update marks: "))

        student = cls.find_student_by_roll(roll)

        if student:
            new_marks = int(input("enter your new marks here: "))
            student.update(new_marks)
        else:
            print("this student is not found!")



while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Update Student Marks")
    print("3. Display All Students")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        Student.add_student()

    elif choice == "2":
        Student.update_student_marks()

    elif choice == "3":
        Student.display_students()

    elif choice == "4":
        print("Program exited successfully!")
        break

    else:
        print("Invalid choice! Please try again.")


class University:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.teachers = []

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def show_students(self):
        print(f"Students enrolled in {self.name}:")
        for student in self.students:
            print(f"ID: {student.student_id}, Name: {student.name}, Year: {student.year}")

    def show_teachers(self):
        print(f"Teachers in {self.name}:")
        for teacher in self.teachers:
            print(f"Name: {teacher.name}, Subject: {teacher.subject}")

class Student(University):
    def __init__(self, university, student_id, name, year):
        super().__init__(university.name)
        self.student_id = student_id
        self.name = name
        self.year = year
        university.add_student(self)

class Teacher:
    def __init__(self, name, subject, timetable):
        self.name = name
        self.subject = subject
        self.timetable = timetable

    def show_timetable(self):
        print(f"Timetable for {self.name} ({self.subject}):")
        for day, time in self.timetable.items():
            print(f"{day}: {time}")

# Creating University instance
punjab_university = University("Tech University")

# Adding Students
student1 = Student(punjab_university, 101, "Saad", "First")
student2 = Student(punjab_university, 102, "Babar", "First")
student3 = Student(punjab_university, 103, "Shahid", "Third")

# Adding Teachers
teacher1 = Teacher("Prof. Imran", "Mathematics", {
    "Monday": "9 AM - 11 AM",
    "Wednesday": "10 AM - 12 PM",
    "Friday": "2 PM - 4 PM"
})
teacher2 = Teacher("Prof. Asim", "Computer Science", {
    "Tuesday": "11 AM - 1 PM",
    "Thursday": "1 PM - 3 PM"
})

# Adding teachers to the university
punjab_university.add_teacher(teacher1)
punjab_university.add_teacher(teacher2)

# Display students and teachers in the university
punjab_university.show_students()
punjab_university.show_teachers()

# Display teacher's timetable
teacher1.show_timetable()
teacher2.show_timetable()

class Person:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

class Student(Person):
    def __init__(self, student_id, name, email, major):
        super().__init__(student_id, name, email)
        self.major = major
        self.courses_enrolled = []
    
    def enroll_course(self, course):
        self.courses_enrolled.append(course)
        print(f"{self.name} enrolled in {course.name}")
    
    def display_info(self):
        print(f"\nStudent ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Major: {self.major}")
        print("Enrolled Courses:")
        for course in self.courses_enrolled:
            print(f"- {course.name}")

class Lecturer(Person):
    def __init__(self, lecturer_id, name, email, department):
        super().__init__(lecturer_id, name, email)
        self.department = department
        self.courses_teaching = []
    
    def assign_course(self, course):
        self.courses_teaching.append(course)
        course.instructor = self
        print(f"{self.name} assigned to teach {course.name}")
    
    def display_info(self):
        print(f"\nLecturer ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Department: {self.department}")
        print("Courses Teaching:")
        for course in self.courses_teaching:
            print(f"- {course.name}")

class Course:
    def __init__(self, course_code, name):
        self.course_code = course_code
        self.name = name
        self.instructor = None
        self.students_enrolled = []
    
    def add_student(self, student):
        self.students_enrolled.append(student)
    
    def display_info(self):
        print(f"\nCourse Code: {self.course_code}")
        print(f"Course Name: {self.name}")
        if self.instructor:
            print(f"Instructor: {self.instructor.name}")
        else:
            print("Instructor: Not assigned")
        print(f"Students Enrolled: {len(self.students_enrolled)}")

class University:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.lecturers = []
        self.courses = []
    
    def add_student(self, student):
        self.students.append(student)
    
    def add_lecturer(self, lecturer):
        self.lecturers.append(lecturer)
    
    def add_course(self, course):
        self.courses.append(course)
    
    def display_students(self):
        print(f"\nStudents at {self.name}:")
        for student in self.students:
            print(f"- {student.name} (ID: {student.id})")
    
    def display_lecturers(self):
        print(f"\nLecturers at {self.name}:")
        for lecturer in self.lecturers:
            print(f"- {lecturer.name} (Department: {lecturer.department})")
    
    def display_courses(self):
        print(f"\nCourses offered at {self.name}:")
        for course in self.courses:
            print(f"- {course.name} (Code: {course.course_code})")

# Create a university
my_university = University("Pauline's University")

# Create some courses
math101 = Course("MATH101", "Introduction to Mathematics")
cs101 = Course("CS101", "Introduction to Computer Science")

# Create some lecturers
lecturer1 = Lecturer("L001", "Dr. Ruth", "ruth@university.edu", "Mathematics")
lecturer2 = Lecturer("L002", "Prof. Pauline", "pauline@university.edu", "Computer Science")

# Assign lecturers to courses
lecturer1.assign_course(math101)
lecturer2.assign_course(cs101)

# Create some students
student1 = Student("S001", "Mable Tusiime", "mable@student.edu", "Computer Science")
student2 = Student("S002", "Innocent Enock Othieno", "innocent@student.edu", "Mathematics")

# Add entities to university
my_university.add_student(student1)
my_university.add_student(student2)
my_university.add_lecturer(lecturer1)
my_university.add_lecturer(lecturer2)
my_university.add_course(math101)
my_university.add_course(cs101)

# Students enroll in courses
student1.enroll_course(cs101)
student1.enroll_course(math101)
student2.enroll_course(math101)

# Update course enrollment lists
for course in [math101, cs101]:
    for student in course.students_enrolled:
        course.add_student(student)

# Display information
print("\n=== University System ===")
print(f"Welcome to {my_university.name}\n")

print("\n--- Students ---")
student1.display_info()
student2.display_info()

print("\n--- Lecturers ---")
lecturer1.display_info()
lecturer2.display_info()

print("\n--- Courses ---")
math101.display_info()
cs101.display_info()

print("\n--- University Overview ---")
my_university.display_students()
my_university.display_lecturers()
my_university.display_courses()
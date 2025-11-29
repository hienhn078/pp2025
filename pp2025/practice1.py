class Student:
    def __init__(self, student_id, student_name, dob):
        self.student_id = student_id
        self.student_name = student_name
        self.dob = dob
        
    def __str__(self):
        return f"{self.student_id} - {self.student_name} - {self.dob}"


class Course:
    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name
        
    def __str__(self):
        return f"{self.course_id} - {self.course_name}"


class MarkManager:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}  
    
    def input_students(self):
        n = int(input("Enter the number of students: "))
        for i in range(n):
            print(f"Enter information for student {i+1}:")
            student_id = input("Student ID: ")
            student_name = input("Student Name: ")
            dob = input("Date of Birth: ")
            student = Student(student_id, student_name, dob)
            self.students.append(student)
    
    def input_courses(self):
        n = int(input("Enter the number of courses: "))
        for i in range(n):
            print(f"__Enter the information for course {i+2}")
            course_id = input("Course ID: ")
            course_name = input("Course Name: ")
            course = Course(course_id, course_name)
            self.courses.append(course)
    
    def input_marks(self):
        course_id = input("Enter the course ID to input marks: ")
        if course_id not in [course.course_id for course in self.courses]:
            print("Course not found!")
            return
        
        if course_id not in self.marks:
            self.marks[course_id] = {}
        
        print(f"Enter marks for course {course_id}:")
        for student in self.students:
            mark = float(input(f"Enter marks for {student.student_name}: "))
            self.marks[course_id][student.student_id] = mark
    
    def list_students(self):
        print("\n__Students List__")
        for student in self.students:
            print(student)
    
    def list_courses(self):
        print("\n__Courses List__")
        for course in self.courses:
            print(course)
    
    def show_marks(self):
        course_id = input("Enter the course ID to show marks: ")
        if course_id not in self.marks:
            print("No marks for this course!")
            return
        
        print(f"\nMarks for course {course_id}:")
        for student in self.students:
            mark = self.marks[course_id].get(student.student_id, "Not Available")
            print(f"{student.student_name}: {mark}")


def main():
    manager = MarkManager()
    
    while True:
        print("""
Student mark management:
1. Input students
2. Input courses
3. Input marks for course
4. List students
5. List courses
6. Show marks for course
7. Exit
""")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            manager.input_students()
        elif choice == "2":
            manager.input_courses()
        elif choice == "3":
            manager.input_marks()
        elif choice == "4":
            manager.list_students()
        elif choice == "5":
            manager.list_courses()
        elif choice == "6":
            manager.show_marks()
        elif choice == "7":
            print("Exiting program...")
            break
        else:
            print("Invalid option! Try again.")


if __name__ == "__main__":
    main()

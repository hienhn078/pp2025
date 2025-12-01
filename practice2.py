class Student:
    def __init__(self, student_id, student_name, dob):
        self.__student_id = student_id
        self.__student_name = student_name
        self.__dob = dob

    @property
    def info(self):
        return {
            "id": self.__student_id,
            "name": self.__student_name,
            "dob": self.__dob
        }

    def __str__(self):
        return f"{self.__student_id} - {self.__student_name} - {self.__dob}"


class Course:
    def __init__(self, course_id, course_name):
        self.__course_id = course_id
        self.__course_name = course_name

    @property
    def info(self):
        return {
            "id": self.__course_id,
            "name": self.__course_name
        }

    def __str__(self):
        return f"{self.__course_id} - {self.__course_name}"


class Mark:
    def __init__(self, student, course, value):
        self.student = student   
        self.course = course      
        self.value = value

    def __str__(self):
        return f"{self.student.info['name']} ({self.student.info['id']}) - {self.course.info['id']}: {self.value}"


class MarkManager:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = []

    def input_student(self):
        n = int(input("Enter the number of students: "))
        for i in range(n):
            print(f"Enter the information of student {i+1}:")
            student_id = input("  Student ID: ")
            student_name = input("  Student name: ")
            dob = input("  Date of Birth: ")
            student = Student(student_id, student_name, dob)
            self.students.append(student)

    def find_student(self, student_id):
        result = [student for student in self.students if student.info["id"] == student_id]
        return result[0] if result else None


    def input_course(self):
        n = int(input("Enter the number of courses: "))
        for i in range(n):
            print(f"Enter the information of course {i+1}:")
            course_id = input("  Course ID: ")
            course_name = input("  Course name: ")
            course = Course(course_id, course_name)
            self.courses.append(course)

    def find_course(self, course_id):
        result = [course for course in self.courses if course.info["id"] == course_id]
        return result[0] if result else None
    
    def input_marks(self):
        course_id = input("Enter course ID to input marks: ")
        course = self.find_course(course_id)
        if not course:
            print("Course not found")
            return

        if not self.students:
            print("No students available. Please add students first.")
            return

        print(f"Enter marks for course {course.info['name']} ({course.info['id']}):")
        for student in self.students:
            while True:
                try:
                    mark_value = float(input(f"  Enter the mark for {student.info['name']} ({student.info['id']}): "))
                    break
                except ValueError:
                    print("  Invalid input. Please enter a number.")
            mark = Mark(student, course, mark_value)
            self.marks.append(mark)

    def get_marks_by_course(self, course_id):
        return [mark for mark in self.marks if mark.course.info["id"] == course_id]

    def list_students(self):
        if not self.students:
            return "Student List\n<no students>\n"
        student_text = "\n".join(str(student) for student in self.students)
        return f"Student List\n{student_text}\n"

    def list_course(self):
        if not self.courses:
            return "Course List\nNo courses\n"
        course_text = "\n".join(str(course) for course in self.courses)
        return f"Course List\n{course_text}\n"

    def show_marks(self):
        course_id = input("Enter course ID to show marks: ")
        course = self.find_course(course_id)
        if not course:
            print("Course not found")
            return

        marks = self.get_marks_by_course(course_id)
        if not marks:
            print("No marks for this course")
            return

        print(f"Marks for course {course.info['name']} ({course.info['id']}):")
        for mark in marks:
            print(" ", mark)


def main():
    manager = MarkManager()
    while True:
        print("""
Student mark management:
1. Input student
2. Input course
3. Input marks
4. List students
5. List courses
6. Show marks
7. Exit
""")
        choice = input("Your choice: ").strip()

        if choice == "1":
            manager.input_student()
        elif choice == "2":
            manager.input_course()
        elif choice == "3":
            manager.input_marks()
        elif choice == "4":
            print(manager.list_students(), end="")  
        elif choice == "5":
            print(manager.list_course(), end="")     
        elif choice == "6":
            manager.show_marks()
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")
            

if __name__ == "__main__":
    main()

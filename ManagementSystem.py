import pickle
from Student import Student
from Course import Course

class StudentManagementSystem:
    def __init__(self):
        self.students = self.load_data("students.pkl")
        self.courses = self.load_data("courses.pkl")

        # ---------- Default Courses ----------
        if not self.courses:
            self.courses = [
                Course(1, "Introduction to Programming", "Dr. Zeeshan Bhatti"),
                Course(2, "Data Structures and Algorithms", "Dr. Ali Nizamani"),
                Course(3, "Database Management Systems", "Prof. Ahsan Ahmed"),
                Course(4, "Operating Systems", "Dr. Sana Malik"),
                Course(5, "Web Application Development", "Dr. Javeria Shah"),
                Course(6, "Artificial Intelligence", "Dr. Muhammad Ali Nizamani"),
                Course(7, "Computer Networks", "Dr. Kashif Shaikh"),
                Course(8, "Software Engineering", "Prof. Imran Memon"),
                Course(9, "Object-Oriented Programming", "Dr. Bilal Khoso"),
                Course(10, "Machine Learning", "Dr. Farah Siddiqui")
            ]
            self.save_data("courses.pkl", self.courses)
            print("✅ Default courses loaded into pickle!")

        # ---------- Default Students ----------
        if not self.students:
            self.students = [
                Student(1, "Saroop Singh"),
                Student(2, "Ayesha Khan"),
                Student(3, "Ali Raza"),
                Student(4, "Mehak Sheikh"),
                Student(5, "Bilal Ahmed"),
                Student(6, "Hina Qureshi"),
                Student(7, "Zainab Memon")
            ]
            self.save_data("students.pkl", self.students)
            print("✅ Default students loaded into pickle!")

    # ---------- Add Student ----------
    def add_student(self, student):
        if any(s.student_id == student.student_id for s in self.students):
            print("⚠️ Student ID already exists!")
        else:
            self.students.append(student)
            self.save_data("students.pkl", self.students)
            print(f"✅ Student {student.name} added successfully!")

    # ---------- View All Courses ----------
    def list_courses(self):
        if not self.courses:
            print("No courses available.")
        else:
            for course in self.courses:
                course.display_course_info()

    # ---------- Enroll Student ----------
    def enroll_student(self, student_id, course_id):
        student = next((s for s in self.students if s.student_id == student_id), None)
        course = next((c for c in self.courses if c.course_id == course_id), None)

        if student and course:
            student.enroll_course(course)
            self.save_data("students.pkl", self.students)
        else:
            print("⚠️ Invalid Student or Course ID!")

    # ---------- View Student Courses ----------
    def view_student_courses(self, student_id):
        student = next((s for s in self.students if s.student_id == student_id), None)
        if student:
            student.view_courses()
        else:
            print("⚠️ Student not found!")

    # ---------- Assign Grade ----------
    def assign_grade(self, student_id, course_id, grade):
        student = next((s for s in self.students if s.student_id == student_id), None)
        course = next((c for c in self.courses if c.course_id == course_id), None)

        if student and course:
            student.assign_grade(course, grade)
            self.save_data("students.pkl", self.students)
        else:
            print("⚠️ Invalid Student or Course ID!")

    # ---------- Pickle Save & Load ----------
    def save_data(self, filename, data):
        with open(filename, "wb") as f:
            pickle.dump(data, f)

    def load_data(self, filename):
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except FileNotFoundError:
            return []


# ---------- Main Program ----------
def main():
    sms = StudentManagementSystem()

    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View All Courses")
        print("3. Enroll Student in Course")
        print("4. View Student Courses")
        print("5. Assign Grade")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            student_id = int(input("Enter Student ID: "))
            name = input("Enter Student Name: ")
            sms.add_student(Student(student_id, name))

        elif choice == '2':
            sms.list_courses()

        elif choice == '3':
            student_id = int(input("Enter Student ID: "))
            course_id = int(input("Enter Course ID: "))
            sms.enroll_student(student_id, course_id)

        elif choice == '4':
            student_id = int(input("Enter Student ID: "))
            sms.view_student_courses(student_id)

        elif choice == '5':
            student_id = int(input("Enter Student ID: "))
            course_id = int(input("Enter Course ID: "))
            grade = input("Enter Grade (A/B/C/D/F): ")
            sms.assign_grade(student_id, course_id, grade)

        elif choice == '6':
            print("Exiting... All data saved in pickle.")
            break

        else:
            print("⚠️ Invalid choice! Try again.")


if __name__ == "__main__":
    main()

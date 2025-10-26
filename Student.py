class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.courses = {}  # {course_id: {"course": course_object, "grade": grade}}

    def enroll_course(self, course):
        if course.course_id in self.courses:
            print(f"⚠️ {self.name} is already enrolled in {course.name}")
        else:
            self.courses[course.course_id] = {"course": course, "grade": None}
            print(f"✅ {self.name} enrolled in {course.name}")

    def assign_grade(self, course, grade):
        if course.course_id in self.courses:
            self.courses[course.course_id]["grade"] = grade
            print(f"🎓 Grade {grade} assigned to {self.name} for {course.name}")
        else:
            print(f"⚠️ {self.name} is not enrolled in {course.name}")

    def view_courses(self):
        if not self.courses:
            print(f"{self.name} is not enrolled in any course.")
        else:
            print(f"\n📘 Courses for {self.name}:")
            for data in self.courses.values():
                course = data["course"]
                grade = data["grade"]
                print(f"- {course.name} (Instructor: {course.instructor}) | Grade: {grade if grade else 'N/A'}")

    def __repr__(self):
        return f"Student(ID: {self.student_id}, Name: {self.name})"

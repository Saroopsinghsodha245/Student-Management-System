class Course:
    def __init__(self, course_id, name, instructor):
        self.course_id = course_id
        self.name = name              # ✅ Correct attribute name
        self.instructor = instructor

    def display_course_info(self):
        print(f"ID: {self.course_id}, Course: {self.name}, Instructor: {self.instructor}")

    def __repr__(self):
        return f"Course(ID: {self.course_id}, Name: {self.name}, Instructor: {self.instructor})"

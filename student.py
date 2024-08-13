class Student:
    def __init__(self, name, age, average_score):
        self.name = name
        self.age = age
        self.average_score = average_score

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_average_score(self):
        return self.average_score

    def set_average_score(self, average_score):
        self.average_score = average_score

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Average Score: {self.average_score}")

    def grade(self):
        if self.average_score > 8:
            return "Excellent"
        elif 6 <= self.average_score <= 8:
            return "Good"
        elif 4 <= self.average_score < 6:
            return "Satisfactory"
        else:
            return "Poor"

student1 = Student("Alice", 20, 9.2)
student2 = Student("Bob", 22, 7.5)
student3 = Student("Charlie", 19, 5.3)

students = [student1, student2, student3]

for student in students:
    student.display_info()
    print(f"Grade: {student.grade()}\n")

def is_honors(self):
    return self.average_score > 8

Student.is_honors = is_honors

for student in students:
    print(f"{student.get_name()} Honors: {student.is_honors()}")

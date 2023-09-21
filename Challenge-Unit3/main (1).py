def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students

class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

# Example usage:
student1 = Student("Lingakumar", "11", 3.9)
student2 = Student("Joseph", "12", 3.7)
student3 = Student("Siva", "13", 3.5)

students = [student1, student2, student3]

sorted_students = sort_students(students)

for student in sorted_students:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")

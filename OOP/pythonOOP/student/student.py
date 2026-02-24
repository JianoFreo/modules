class Student:
    academic_year = 2024
    num_students = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1
        
student1 = Student("Jiano", 19)
student2 = Student("Freo", 20)

print(student1.name)
print(student2.age)
print(Student.academic_year) # better to access the class variable by the class name itself rather than the instance
print(Student.num_students)

print(f"The grad students of {Student.academic_year} has {Student.num_students} students")
print(f"they are {student1.name} and {student2.name}")
print(f"The grad of {Student.academic_year} are {student1.name} and {student2.name}")
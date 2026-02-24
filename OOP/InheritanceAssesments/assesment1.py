# Create a Person class with:

# __init__ that takes name and age
# A method introduce() that prints "Hi, I'm [name] and I'm [age] years old"
# Create a Teacher class that inherits from Person:

# Add subject parameter to __init__
# Add a method teach() that prints "[name] is teaching [subject]"
# Create a Student class that inherits from Person:

# Add grade parameter to __init__
# Add a class variable total_students = 0 that counts all students
# Add a method study() that prints "[name] is studying hard"
# Create instances:

# 2 teachers (with different subjects)
# 3 students (with different grades)
# Call all methods to test them
# Print the total number of students
# Bonus Challenge:

# Override the introduce() method in Teacher to say "Hello, I'm [name] and I teach [subject]"
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def introduce(self):
        print(f"hi, Im {self.name} and I'm {self.age} years old")
        
class Student(Person):
    total_students = 0
    
    def __init__(self, name, age, grade):
        super().__init__(name, age)  # Calls Person's __init__ (you have to specify which self to grab(self.name, self.age))
        # thats why you only need to make 1 self.grade in this __init__
        # When Student has its own __init__, 
        # it overrides Person's __init__. But you still need Person's __init__ to run to set name 
        # and age. That's where super() comes in.
        # Python calls Student.__init__("Alice", 16, "10th")
        # Student's __init__ needs to accept these values: def __init__(self, name, age, grade)
        # Then Student passes name and age to Person: super().__init__(name, age)
        self.grade = grade
        Student.total_students += 1
    
    def study(self):
        print(f"{self.name} is studying hard")
        
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
    
    def teach(self):
        print(f"{self.name} is teaching {self.subject}")

# Test instances
teacher1 = Teacher("Mr. Smith", 35, "Math")
teacher2 = Teacher("Ms. Johnson", 42, "English")

student1 = Student("Alice", 16, "10th")
student2 = Student("Bob", 15, "9th")
student3 = Student("Charlie", 17, "11th")

# Test methods
teacher1.introduce()
teacher1.teach()

student1.introduce()
student1.study()

print(f"Total students: {Student.total_students}")
        
        
        
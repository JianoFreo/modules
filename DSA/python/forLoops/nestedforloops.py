for i in range(1, 4):
    for x in range(1, 10):
        print(x)
    print()
#----------------------------------------------------------------------
  
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
Symbol = input("Enter a symbol to use: ")
for i in range(rows):
    for j in range(cols):
        print(Symbol, end=' ')
    print()
#----------------------------------------------------------------------
    
for i in range(5):
    for x in range(7):
        print("x", end="")
    print(" inew line")
#----------------------------------------------------------------------

students = ["Jiano", "Freo", "Magtangob"]
nameClass = ["first name: ", "second name: ", "last name: "]
for student in students:
    for name in nameClass:
            print(nameClass[name], students[student])
    print()
#----------------------------------------------------------------------

students = ["Jiano", "Freo", "Magtangob"]
nameClass = ["first name: ", "second name: ", "last name: "]
for student in range(len(students)):
    for name in range(len(nameClass)):
        if student == name:
            print(nameClass[name] + students[student])
            
#----------------------------------------------------------------------
courseAndStudents = [
    ["BSIS", "David"],
    ["BSIT", "Jiano"],
    ["BSCS", "Freo"],
    ["BSCpE", "Emman"]
]

for listStudents in courseAndStudents:
    for listInList in listStudents:
        print(listInList)
    print()
#----------------------------------------------------------------------
names = ["jiano", "Freo"]
nameClasses = ["first", "second"]

for name in names:
    for nameClass in nameClasses:
        print(nameClass, name)
#----------------------------------------------------------------------

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] == target - nums[i]:
                return [i, j]
    return []

# Example usage:
nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))  # Output: [0, 1]


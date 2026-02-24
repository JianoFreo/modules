# For Loop Training Examples

# 1. Basic for loop with range()
print("=== 1. Basic For Loop ===")
for i in range(1, 6):
    print(f"Number: {i}")

# 2. For loop with list
print("\n=== 2. Loop Through List ===")
fruits = ["apple", "banana", "cherry"]
fruit = input("what do you want: ")
fruits.append(fruit)
for i in fruits:
    print(f"I like {i}")

# 3. For loop with enumerate (get index and value)
print("\n=== 3. Loop with Index ===")
colors = ["red", "green", "blue"]
for index, color in enumerate(colors):
    print(f"{index}: {color}")

# 4. For loop with range step
print("\n=== 4. Loop with Step ===")
for i in range(0, 10, 2):  # 0, 2, 4, 6, 8
    print(i)

# 5. Nested for loops
print("\n=== 5. Nested Loop (Multiplication Table) ===")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")

# 6. For loop with break
print("\n=== 6. Loop with Break ===")
for i in range(1, 10):
    if i == 5:
        print("Found 5, breaking!")
        break
    print(i)

# 7. For loop with continue
print("\n=== 7. Loop with Continue ===")
for i in range(1, 6):
    if i == 3:
        print("Skipping 3")
        continue
    print(i)

# 8. For loop with string
print("\n=== 8. Loop Through String ===")
for letter in "HELLO":
    print(letter)

# 9. For loop with sum/count
print("\n=== 9. Sum Numbers ===")
total = 0
for i in range(1, 6):
    total += i
print(f"Sum of 1-5: {total}")

# 10. For loop with condition
print("\n=== 10. Even Numbers Only ===")
for i in range(1, 11):
    if i % 2 == 0:
        print(i)

# PRACTICE CHALLENGES:
# Try to write loops for these:

# Challenge 1: Print numbers from 10 down to 1
print("\n=== Challenge 1: Count Down ===")
# Your code here


# Challenge 2: Print only vowels from a word
print("\n=== Challenge 2: Find Vowels ===")
# word = "python"
# Your code here


# Challenge 3: Find the largest number in a list
print("\n=== Challenge 3: Find Max ===")
# numbers = [5, 2, 8, 1, 9, 3]
# Your code here


# Challenge 4: Create a pyramid pattern
print("\n=== Challenge 4: Pyramid ===")
# for i in range(1, 6):
#     Your code here
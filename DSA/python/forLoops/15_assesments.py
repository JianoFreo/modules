# Level 1: Basics
# 1. Print numbers 1–5  
# Output:
# ```
# 1
# 2
# 3
# 4
# 5
# ```

for i in range(1, 6):
    print(i)
    
# 2. Print characters of `"hello"`  
# Output:
# ```
# h
# e
# l
# l
# o
# ```
for letters in ("hello"):
    print(letters)
    
# 3. Print even numbers between 2 and 10  
# Output:
# ```
# 2
# 4
# 6
# 8
# 10
# ```
for i in range(2, 11, 2):
    print(i)
    
# Level 2: Lists & Collections
# 4. Print `"I like <fruit>"` for each fruit in `["apple","banana","cherry"]`  
# Output:
# ```
# I like apple
# I like banana
# I like cherry

fruits =["apple", "banana", "cherry"]

for fruit in fruits:
    print(f"I like {fruit}")

# 5. Print coordinates from `[(1,2),(3,4),(5,6)]`  
# Output:
# ```
# x= 1 y= 2
# x= 3 y= 4
# x= 5 y= 6

cords = [(1,2),(3,4),(5,6)]

for x, y in cords:
    print(f"x= {x} y= {y}")

# 6. Print items with value > 100 from `{"pen":10,"book":120,"bag":900}`  
# Output:
# ```
# book 120
# bag 900

itemPrices = {"pen":10,"book":120,"bag":900}

for item, price in itemPrices.items():
# person.keys()      # Only keys: name, age, city
# person.values()    # Only values: Jiano, 20, Manila
# person.items()     # Both: (name, Jiano), (age, 20), (city, Manila)
    if price > 100:
        print(f"{item} {price}")
        
# Level 3: Loop Control
# 7. Print numbers 1–10 but skip multiples of 3  
# Output:
# ```
# 1
# 2
# 4
# 5
# 7
# 8
# 10

for i in range(1, 11):
    if (i % 3 == 0):
        continue
    print(i)
    
# 8. Stop summing 1–100 when total exceeds 50, print where stopped  
# Output:
# ```
# Stopped at 10
stopped = int(input("what number of total shouold it stop: "))
total = 0
for i in range(1, 101):
    total += i
    if total > stopped:
        print(f"Stopped at {i}")
        break
# 9. Search for 7 in `[1,2,3,8,9]`, print `"not found"`  
# Output:
# ```
# not found
# ```
nums = [1,2,3,7,8,7,9]# if there are more than one 7, it prints more "found"
found = False
for i in nums:
    if i == 7:
        print("found")
        found = True
if not found:
    print("not found")
###OR
for i in [1,2,3,7,7,8,9]: #this one only prints it once
    if i == 7:
        print("found")
        break
else: 
    print("not found")







for i in range(10, 0, -1):
    print(i)
print("Happy birthday")

num = int(input("Enter a number: "))
if (num % 2 == 0):
    print("even")
else:
    print("odd")

# Example: Dynamic ascending/descending based on variable values
start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

# If start is less than end, count up (step=1), otherwise count down (step=-1)
#step = 1 if start < end else -1
if (start <= end):
    step = 1
else:
    step = -1

for i in range(start, end, step):
    print(i)

# Stack Example - LIFO (Last In, First Out)
print("\n--- Stack Example ---")
stack = []

# Get user input and push to stack
while True:
    user_input = input("Enter a value to push (or 'quit' to stop): ")
    if user_input.lower() == 'quit':
        break
    stack.append(user_input)
    print(f"Stack: {stack}")

# Pop elements
print("\nPopping elements:")
while stack:
    popped = stack.pop()
    print(f"Popped: {popped}, Remaining stack: {stack}")

if not stack:
    print("Stack is now empty")

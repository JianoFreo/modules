# Stack Example - LIFO (Last In, First Out)
# Print a header to show the start of stack example
print("\n--- Stack Example ---")
# Initialize an empty list to use as a stack
stack = []

# Get user input and push to stack
# Create an infinite loop to keep accepting user input
while True:
    # Prompt user to enter a value and store it
    user_input = input("Enter a value to push (or 'quit' to stop): ")
    # Check if user typed 'quit' (case-insensitive) to exit the loop
    if user_input.lower() == 'quit':
        # Break out of the loop
        break
    # Add the user input to the end of the stack (push operation)
    stack.append(user_input)
    # Display the current stack after adding the element
    print(f"Stack: {stack}")

# Pop elements
# Print a header for the popping section
print("\nPopping elements:")
# Loop while the stack is not empty
while stack:
    # Remove and return the last element from the stack (pop operation)
    popped = stack.pop()
    # Display the popped element and what remains in the stack
    print(f"Popped: {popped}, Remaining stack: {stack}")

# Check if stack is empty
if not stack:
    # Print message if stack is empty (all elements have been popped)
    print("Stack is now empty")
    
    
    list = []
stack = []
def push(num):
    stack.append(num)
def pop(num):
    stack.pop(num)
def peek():
    return stack[-1]
def isEmpty():
    return len(stack) == 0

# Menu system
while True:
    print("\n=== Stack Menu ===")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Is Empty")
    print("5. print all stack")
    print("6. Exit")
    
    choice = input("Choose an option (1-6): ")
    
    match choice:
        case "1":
            num = int(input("Enter number to push: "))
            push(num)
            print(f"Pushed {num}")
        case "2":
            pop(-1)
            print("Popped element")
        case "3":
            print(f"Top element: {peek()}")
        case "4":
            print(f"Is empty: {isEmpty()}")
        case "5":
            print(stack)
        case "6":
            print("Exiting...")
            break
        case _:
            print("Invalid choice") 
    
    

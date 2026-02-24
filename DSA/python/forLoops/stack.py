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


    

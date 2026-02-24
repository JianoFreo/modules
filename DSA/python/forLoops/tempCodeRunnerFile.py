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
    
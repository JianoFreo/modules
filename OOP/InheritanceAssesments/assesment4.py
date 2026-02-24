# # Restaurant Management System
# Different types of menu items (appetizers, main courses, desserts, drinks)
# Each item has a name, price, and preparation time
# Some items can be customized (like pizzas with toppings, or drinks with size options)
# They need to track how many times each item is ordered
# They want to see which items are most popular
# They need to calculate bills for customers
# Some items have special dietary tags (vegetarian, vegan, gluten-free)
# Main courses need to show calories, but appetizers and desserts don't require this
# What they need:

# Track all items on the menu
# Be able to add new items
# Calculate the total cost when a customer orders multiple items
# Show the most popular items (ordered more than 10 times)
# Apply a 10% discount for orders over $50
# Display the full menu organized by type
# For each order, calculate estimated wait time (sum of all preparation times)
# Mark items as "out of stock" and prevent ordering them
# Your Task:

# Design and build this system using OOP principles. Think about:

# What classes do you need?
# What should inherit from what?
# What data needs to be stored?
# What methods are needed?
class MenuItem:
    all_items = []
    
    def __init__(self, name, price, prep_time):
        self.name = name
        self.price = price
        self.prep_time = prep_time
        self.times_ordered = 0
        self.in_stock = True
        MenuItem.all_items.append(self)
    
    def order(self):
        if self.in_stock:
            self.times_ordered += 1
            return True
        else:
            print(f"{self.name} is out of stock")
            return False
    
    def mark_out_of_stock(self):
        self.in_stock = False
        print(f"{self.name} marked as out of stock")
    
    def is_popular(self):
        return self.times_ordered > 10
    
    def display(self):
        status = "Available" if self.in_stock else "OUT OF STOCK"
        print(f"{self.name} - ${self.price} ({self.prep_time} min) - {status}")

class Appetizer(MenuItem):
    def __init__(self, name, price, prep_time, dietary_tags=None):
        super().__init__(name, price, prep_time)
        self.dietary_tags = dietary_tags if dietary_tags else []
        self.category = "Appetizer"
    
    def display(self):
        status = "Available" if self.in_stock else "OUT OF STOCK"
        tags = ", ".join(self.dietary_tags) if self.dietary_tags else "None"
        print(f"[APPETIZER] {self.name} - ${self.price} ({self.prep_time} min) - Tags: {tags} - {status}")

class MainCourse(MenuItem):
    def __init__(self, name, price, prep_time, calories, dietary_tags=None):
        super().__init__(name, price, prep_time)
        self.calories = calories
        self.dietary_tags = dietary_tags if dietary_tags else []
        self.category = "Main Course"
    
    def display(self):
        status = "Available" if self.in_stock else "OUT OF STOCK"
        tags = ", ".join(self.dietary_tags) if self.dietary_tags else "None"
        print(f"[MAIN COURSE] {self.name} - ${self.price} ({self.calories} cal, {self.prep_time} min) - Tags: {tags} - {status}")

class Dessert(MenuItem):
    def __init__(self, name, price, prep_time, dietary_tags=None):
        super().__init__(name, price, prep_time)
        self.dietary_tags = dietary_tags if dietary_tags else []
        self.category = "Dessert"
    
    def display(self):
        status = "Available" if self.in_stock else "OUT OF STOCK"
        tags = ", ".join(self.dietary_tags) if self.dietary_tags else "None"
        print(f"[DESSERT] {self.name} - ${self.price} ({self.prep_time} min) - Tags: {tags} - {status}")

class Drink(MenuItem):
    def __init__(self, name, price, prep_time, size="Medium"):
        super().__init__(name, price, prep_time)
        self.size = size
        self.category = "Drink"
    
    def display(self):
        status = "Available" if self.in_stock else "OUT OF STOCK"
        print(f"[DRINK] {self.name} ({self.size}) - ${self.price} ({self.prep_time} min) - {status}")

class Order:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = []
    
    def add_item(self, item):
        if item.order():
            self.items.append(item)
            print(f"Added {item.name} to order")
        
    def calculate_total(self):
        total = sum(item.price for item in self.items)
        if total > 50:
            discount = total * 0.10
            total -= discount
            print(f"10% discount applied: -${discount:.2f}")
        return total
    
    def calculate_wait_time(self):
        return sum(item.prep_time for item in self.items)
    
    def show_receipt(self):
        print(f"\n{'='*50}")
        print(f"ORDER FOR: {self.customer_name}")
        print(f"{'='*50}")
        for item in self.items:
            print(f"  {item.name} - ${item.price}")
        print(f"{'-'*50}")
        total = self.calculate_total()
        wait_time = self.calculate_wait_time()
        print(f"TOTAL: ${total:.2f}")
        print(f"Estimated wait time: {wait_time} minutes")
        print(f"{'='*50}\n")

class Restaurant:
    def __init__(self, name):
        self.name = name
    
    def display_menu(self):
        print(f"\n{'='*50}")
        print(f"{self.name.upper()} - MENU")
        print(f"{'='*50}\n")
        
        categories = ["Appetizer", "Main Course", "Dessert", "Drink"]
        for category in categories:
            print(f"\n--- {category}s ---")
            for item in MenuItem.all_items:
                if hasattr(item, 'category') and item.category == category:
                    item.display()
    
    def show_popular_items(self):
        print(f"\n{'='*50}")
        print("POPULAR ITEMS (Ordered more than 10 times)")
        print(f"{'='*50}")
        popular = [item for item in MenuItem.all_items if item.is_popular()]
        if popular:
            for item in popular:
                print(f"{item.name} - Ordered {item.times_ordered} times")
        else:
            print("No popular items yet")
        print()

# Create Restaurant
restaurant = Restaurant("The Daily Plate")

# Create Menu Items
# Appetizers
wings = Appetizer("Buffalo Wings", 8.99, 15)
salad = Appetizer("Caesar Salad", 7.50, 10, ["vegetarian"])
nachos = Appetizer("Loaded Nachos", 9.99, 12, ["vegetarian"])

# Main Courses
steak = MainCourse("Grilled Steak", 24.99, 25, 650)
pasta = MainCourse("Fettuccine Alfredo", 16.99, 20, 580, ["vegetarian"])
burger = MainCourse("Classic Burger", 12.99, 18, 720)
salmon = MainCourse("Grilled Salmon", 22.99, 22, 520)

# Desserts
cake = Dessert("Chocolate Cake", 6.99, 8)
icecream = Dessert("Ice Cream Sundae", 5.99, 5, ["gluten-free"])

# Drinks
soda = Drink("Coca Cola", 2.99, 2, "Large")
juice = Drink("Orange Juice", 3.99, 3, "Medium")
coffee = Drink("Coffee", 2.50, 5, "Small")

# Display Menu
restaurant.display_menu()

# Simulate some orders to make items popular
print("\n--- Simulating previous orders to create popularity data ---")
for i in range(15):
    burger.order()
    pasta.order()
for i in range(12):
    wings.order()

# Show popular items
restaurant.show_popular_items()

# Create customer orders
print("\n--- CUSTOMER ORDERS ---\n")

# Order 1
order1 = Order("John Smith")
order1.add_item(wings)
order1.add_item(steak)
order1.add_item(soda)
order1.show_receipt()

# Order 2 (over $50 for discount)
order2 = Order("Sarah Johnson")
order2.add_item(salad)
order2.add_item(steak)
order2.add_item(salmon)
order2.add_item(cake)
order2.add_item(coffee)
order2.show_receipt()

# Mark item as out of stock
print("--- STOCK MANAGEMENT ---")
icecream.mark_out_of_stock()

# Try to order out of stock item
print()
order3 = Order("Mike Davis")
order3.add_item(burger)
order3.add_item(icecream)  # This will fail
order3.add_item(soda)
order3.show_receipt()

# Show updated popular items
restaurant.show_popular_items()

        
        
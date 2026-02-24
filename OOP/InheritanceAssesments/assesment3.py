# Create a Product class with:

# __init__ that takes name, price, and stock (quantity available)
# Class variable total_products = 0 to track all products
# Method display_info() that prints "[name] - $[price] ([stock] in stock)"
# Method purchase(quantity) that reduces stock by quantity and prints "Purchased [quantity] name" (only if enough stock available, otherwise print "Not enough stock")
# Create an Electronics class that inherits from Product:

# Add warranty parameter to __init__ (in years, use super())
# Override display_info() to also show warranty: "[name] - $[price] ([stock] in stock) - [warranty] year warranty"
# Add method extend_warranty(years) that adds years to warranty and prints "Warranty extended to [warranty] years"
# Create a Clothing class that inherits from Product:

# Add size parameter to __init__ (use super())
# Override display_info() to also show size: "[name] - $[price] (Size: [size], [stock] in stock)"
# Add method restock(quantity) that adds quantity to stock and prints "Restocked [quantity] items. New stock: [stock]"
# Test your code:

# Create 2 electronics items with different warranties
# Create 2 clothing items with different sizes
# Display info for all items
# Purchase some items (test both success and failure cases)
# Extend warranty for one electronic item
# Restock one clothing item
# Print total products created
class Product:
    total_products = 0
    all_products = []
    
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
        Product.total_products += 1
        Product.all_products.append(self)
        
    def display_info(self):
        print(f"{self.name} - ${self.price} ({self.stock} in stock)")
    
    def purchase(self, quantity):
        if self.stock >= quantity:
            self.stock -= quantity
            print(f"Purchased {quantity} {self.name}(s)")
        else:
            print("Not enough stock")

class Electronics(Product):
    def __init__(self, name, price, stock, warranty):
        super().__init__(name, price, stock)
        self.warranty = warranty
        
    def display_info(self):
        print(f"{self.name} - ${self.price} ({self.stock} in stock) - {self.warranty} year warranty")
    
    def extend_warranty(self, years):
        self.warranty += years
        print(f"Warranty extended to {self.warranty} years")
        
class Clothing(Product):
    def __init__(self, name, price, stock, size):
        super().__init__(name, price, stock)
        self.size = size
        
    def display_info(self):
        print(f"{self.name} - ${self.price} (Size: {self.size}, {self.stock} in stock)")
        
    def restock(self, quantity):
        self.stock += quantity
        print(f"Restocked {quantity} items. New stock: {self.stock}")

electronics1 = Electronics("phone", 1000, 10, 3)
electronics2 = Electronics("laptop", 2000, 20, 5)

clothing1 = Clothing("pants", 200, 30, "L")
clothing2 = Clothing("shirt", 300, 10, "M")

# Display all items
for product in Product.all_products:
    product.display_info()

print()

# Test purchases
electronics1.purchase(5)  # Success
electronics2.purchase(25)  # Not enough stock
clothing1.purchase(10)  # Success

print()

# Extend warranty
electronics1.extend_warranty(2)

print()

# Restock
clothing2.restock(15)

print()

# Print total products
print(f"Total products created: {Product.total_products}")


        
    
        
        
        
        
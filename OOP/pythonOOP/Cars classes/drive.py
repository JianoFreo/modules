from car import Car
# class Car:
#     def __init__(self, model, year, color, for_sale):
#         self.model = model
#         self.year = year
#         self.color = color
#         self.for_sale = for_sale
    
#     def drive(self):
#         print(f"you drive the car {self.color} {self.model}")
        
#     def stop(self):
#         print(f"You stop the car {self.color} {self.model}")

car1 = Car("Mustang", 2024, "red", False)
car2 = Car("Corvette", 2025, "blue", True)

car1.drive()
car2.stop()
car1.describe()
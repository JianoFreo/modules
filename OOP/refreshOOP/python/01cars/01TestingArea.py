from MainClass import Car

car1 = Car("Mustang", 2024, "red", False)
car2 = Car("Corvette", 2025, "blue", True)
##-------------------new method--------------------
print(car1.model)
print(car2.year)
##-------------------new method--------------------
car1.drive()
car2.stop()

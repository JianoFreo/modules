# from animalClass import *
### It is temporarily duplicated so i dont have to switch tabs, delete the parent class after
class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True
        
    def eat(self):
        print(f"{self.name} is eating.")
    
    def sleep(self):
        print(f"{self.name} is sleeping.")    
        
class Dog(Animal): #This is a child class of Animal, that means that all of the attributes of Animal would be under here
    def speak(self):
        print("arf")
    # def __init__(self, name): THESE ARE THE METHODS THAT WERE INHERITED FROM THE PARENT CLASS ANIMAL
    #     self.name = name
    #     self.is_alive = True
        
    # def eat(self):
    #     print(f"{self.name} is eating.")
    
    # def sleep(self):
    #     print(f"{self.name} is sleeping.")
class Cat(Animal): #This is a child class of Animal, that means that all of the attributes of Animal would be under here
    pass
class Mouse(Animal): #This is a child class of Animal, that means that all of the attributes of Animal would be under here
    pass

dog1 = Dog("Scooby")# Creates Dog object, __init__ runs automatically. because there is function that follows dog1, though it would run anyway
dog2 = Dog("Shaggy")#This replaces the name parameter not the self
cat1 = Cat("Whiskers")
cat2 = Cat("Mingming")
mouse1 = Mouse("Jerry")
mouse2 = Mouse("Mickey")

dog1.speak()
print(dog1.name) # even thoough the dog class is empty it still inherited the name attribute because of the parent class Animal
print(dog1.is_alive) # is_alive is in not in the parameter because the value is fixed in (self.is_alive = True)

#----------------------------------------------------------------------------------------------------------------------------------------
class Bag:
    def __init__(self, name):
        self.name = name
class Wallet(Bag):
    def Brand(self, name):
        self.name = name

item1 = Wallet("dior")
print(item1.name)

# The Brand method in Wallet is not 
# running at all - it's just sitting 
# there unused. You'd have to call it
# manually like:

item1 = Wallet("dior")  # Uses Bag's __init__
item1.Brand("gucci")    # Now Brand runs and changes name to "gucci"
print(item1.name)       # "gucci"
    
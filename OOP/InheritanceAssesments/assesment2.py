# Create a Character class with:

# __init__ that takes name, health, and level
# Class variable total_characters = 0 to track all characters created
# Method attack() that prints "[name] attacks for [level * 10] damage"
# Method is_alive() that returns True if health > 0, otherwise False
# Create a Warrior class that inherits from Character:

# Add weapon parameter to __init__ (use super())
# Override attack() to print "[name] swings their [weapon] for [level * 15] damage"
# Add method defend() that prints "[name] blocks with their shield"
# Create a Mage class that inherits from Character:

# Add spell parameter to __init__ (use super())
# Override attack() to print "[name] casts [spell] for [level * 12] damage"
# Add method heal() that adds 20 to health and prints "[name] heals for 20. Health is now [health]"
# Test your code:

# Create 2 warriors with different weapons
# Create 2 mages with different spells
# Have each character attack
# Have warriors defend and mages heal
# Print total characters created
class Character:
    total_characters = 0
    def __init__(self, name, health, level):
        self.name = name
        self.health = health
        self.level = level
        Character.total_characters += 1
        
    def attack(self):
        print(f"{self.name} attacks for {self.level * 10} damage")
        
    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False
        
class Warrior(Character):
    def __init__(self, name, health, level, weapon):
        super().__init__(name, health, level)
        self.weapon = weapon
    def attack(self): #overrides the Character's attack()
        print(f"{self.name} swings their {self.weapon} for {self.level * 15} damage")
    
    def defend(self):
        print(f"{self.name} blocks with their sheild")
        
class Mage(Character):
    def __init__(self, name, health, level, spell):
        super().__init__(name, health, level)
        self.spell = spell
    
    def attack(self):
        print(f"{self.name} casts {self.spell} for {self.level * 12} damage")
    
    def heal(self):
        self.health += 20
        print(f"{self.name} heals for 20. Health is now {self.health}")
    
warrior1 = Warrior("kaka", 20, 15, "sword")
warrior2 = Warrior("juan", 10, 15, "bow")

mage1 = Mage("nana", 30, 10, "blast")
mage2 = Mage("JJ", 25, 5, "fireball")

# Test all methods
warrior1.attack()
warrior1.defend()

warrior2.attack()
warrior2.defend()

mage1.attack()
mage1.heal()

mage2.attack()
mage2.heal()

print(f"\nTotal characters created: {Character.total_characters}")


        
        
        
class Bag:
    def __init__(self, name):
        self.name = name
class Wallet(Bag):
    def Brand(self, name):
        self.name = name

item1 = Wallet("dior")
print(item1.name)
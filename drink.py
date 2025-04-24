class Drink:
    def __init__(self,price):
        self.price = price
    def drink(self):
        print("je ne sais pas ce que c'est, mais je le bois.")
class coffee(Drink):
    price = {"simple":1,"serre":1,"allonge":1.5}
    def __init__(self,type):
        self.type = type
        super().__init__(price = self.price.get(type, 1))
    def drink(self):
        print(f"un bon cafe de {self.type} qui coute {self.price}$ pour me reveiller !")
coffee = coffee("simple")
boire = coffee.drink()
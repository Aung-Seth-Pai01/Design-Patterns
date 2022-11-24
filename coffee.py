from abc import ABC, abstractmethod

class Beverage(ABC):
    def __init__(self, description) -> None:
        self.description = description

    @abstractmethod
    def cost(self):
        pass

class Expresso(Beverage):
    def show_desc(self):
        return self.description

    def cost(self):
        return 100

class AddonDecorator(Beverage):
    def __init__(self, beverage: Beverage):
        self._beverage = beverage
    
    def Beverage(self):
        return self._beverage

class SoyDecorator(AddonDecorator):
    def show_desc(self):
        return self.Beverage().show_desc() + " Soy"

    def cost(self):
        return self.Beverage().cost() + 50

class ChocolateDecorator(AddonDecorator):
    def show_desc(self):
        return self.Beverage().show_desc() + " Choco"
    
    def cost(self):
        return self.Beverage().cost() + 100

mycoffee = Expresso("Expresso")
mycoffee = ChocolateDecorator(SoyDecorator(mycoffee))
print(mycoffee.cost(), mycoffee.show_desc())
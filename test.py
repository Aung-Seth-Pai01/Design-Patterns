from abc import ABC, abstractmethod

class Beverage(ABC):
    @abstractmethod
    def show_cost(self):
        pass

class Expresso(Beverage):
    name = "Expresso"
    cost = 100
    def __str__(self):
        return f"{self.name} is {self.cost}"

    def show_cost(self):
        return self.cost

class AddonDecorator(Beverage):
    def __init__(self, beverage: Beverage):
        self.beverage = beverage
    
    def Beverage(self):
        return self.beverage

class SoyDecorator(AddonDecorator):
    beverage: Beverage;
    def __init__(self, b):
        self.beverage = b
        self.beverage.name = "Soy " + self.Beverage().name
        self.beverage.cost =  self.Beverage().cost + 50

    def __str__(self):
        return f"{self.beverage.name} is {self.beverage.cost}"

    def show_cost(self):
        return self.Beverage().cost + 50

class ChocoDecorator(AddonDecorator):
    beverage: Beverage;
    def __init__(self, b):
        self.beverage = b
        self.beverage.name = "Choco " + self.Beverage().name
        self.beverage.cost =  self.Beverage().cost + 200

    def __str__(self):
        return f"{self.beverage.name} is {self.beverage.cost}"

    def show_cost(self):
        return self.Beverage().cost + 50

def client_code(coffee: Beverage) -> str:
    print(f"{coffee.show_desc()}, {coffee.cost()}")

if __name__ == "__main__":
    mycoffee = Expresso()
    print(mycoffee)
    
    mycoffee = SoyDecorator(mycoffee)
    print(mycoffee)

    # mycoffee = ChocoDecorator(mycoffee)
    # print(mycoffee)

    # mycoffee = ChocolateDecorator(SoyDecorator(mycoffee))
    # client_code(mycoffee)
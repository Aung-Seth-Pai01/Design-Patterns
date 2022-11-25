'''Decorator Pattern Practice
'''

from abc import ABC, abstractmethod

# abstract class (component) enforces required class methods
class Beverage(ABC):
    def __init__(self, description):
        self.description = description

    @abstractmethod
    def cost(self):
        pass

    @abstractmethod
    def show_desc(self):
        pass

# concrete component (base class)
class Coffee(Beverage):
    '''base coffee with default cost'''
    def show_desc(self):
        return self.description

    def cost(self):
        return 100

# base decorator (provide interface for other decorators)
class AddonDecorator(Beverage):
    def __init__(self, beverage: Beverage):
        self._beverage = beverage
    
    def Beverage(self):
        return self._beverage

# concrete decorator
class SoyDecorator(AddonDecorator):
    '''Soy Milk topping for base coffee'''
    def show_desc(self):
        return "Soy " + self.Beverage().show_desc()

    def cost(self):
        return self.Beverage().cost() + 50

# concrete decorator
class ChocolateDecorator(AddonDecorator):
    '''Chocolate topping for base coffee'''
    def show_desc(self):
        return "Choco " + self.Beverage().show_desc()
    
    def cost(self):
        return self.Beverage().cost() + 100

# concrete decorator
class DiscountDecorator(AddonDecorator):
    '''Apply discount on provided Beverage
        args: input: discount_percent -> int 0~100
    '''
    def __init__(self, beverage: Beverage, discount_percent):
        super().__init__(beverage)
        self.discount_percent = discount_percent
        
    def show_desc(self):
        if isinstance(self.discount_percent, int) and (self.discount_percent in range(0,101)):
            print(f"Applied {self.discount_percent}% Discount on " + self.Beverage().show_desc())
            return self.Beverage().show_desc()
        else:
            print("Discount not available")
            return self.Beverage().show_desc()

    def cost(self):
        if isinstance(self.discount_percent, int) and (self.discount_percent in range(0,101)):
            _discount_deduction = (self.discount_percent/100) * self.Beverage().cost()
            return self.Beverage().cost() - _discount_deduction
        else:
            return self.Beverage().cost()

def client_code(coffee: Beverage) -> str:
    print(f"{coffee.show_desc()}, {coffee.cost()}")

if __name__ == "__main__":
    mycoffee = Coffee("Expresso")
    client_code(mycoffee)

    mycoffee = ChocolateDecorator(DiscountDecorator(SoyDecorator(mycoffee), 10))
    client_code(mycoffee)
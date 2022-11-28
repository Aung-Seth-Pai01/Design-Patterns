'''Decorator Pattern Practice
'''
from base_coffee import Coffee
from addons_decorator import SoyDecorator, ChocolateDecorator
from discount import DiscountDecorator

def client_code(coffee) -> str:
    print(f"{coffee.show_desc()}, {coffee.cost()}")

if __name__ == "__main__":
    mycoffee = Coffee("Expresso")
    client_code(mycoffee)

    mycoffee = ChocolateDecorator(DiscountDecorator(SoyDecorator(mycoffee), 10))
    client_code(mycoffee)
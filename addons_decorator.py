from decorator import AddonDecorator

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
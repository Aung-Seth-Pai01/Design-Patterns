from decorator import AddonDecorator
from abstract_drink import Beverage

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
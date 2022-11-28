from abstract_drink import Beverage

# base decorator (provide interface for other decorators)
class AddonDecorator(Beverage):
    def __init__(self, beverage: Beverage):
        self._beverage = beverage
    
    def Beverage(self):
        return self._beverage

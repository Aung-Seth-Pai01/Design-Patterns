from abstract_drink import Beverage

# concrete component (base class)
class Coffee(Beverage):
    '''base coffee with default cost'''
    def show_desc(self):
        return self.description

    def cost(self):
        return 100
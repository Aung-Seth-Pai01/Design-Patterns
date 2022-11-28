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
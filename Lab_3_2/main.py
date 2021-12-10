from abc import ABC

from customization import Customization
from manufacture import CocaColaFactory


class ProductStore(ABC):

    def __init__(self):
        pass

    def makeProduct(self):
        for factory in [CocaColaFactory()]:
            self.factory = factory
            self.CocaCola = self.factory.getProduct(customization=Customization)
            self.CocaCola.make()
            self.CocaCola.setWater()
            self.CocaCola.setCoke()


product = ProductStore()
product.makeProduct()

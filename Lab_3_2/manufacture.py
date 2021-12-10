from abc import ABC, abstractmethod

from customization import Customization
from preparation import Preparation


class ProductFactory(ABC):

    @abstractmethod
    def getProduct(self, customization):
        pass

    @staticmethod
    def getProduct_factory():
        pass


class CappuccinoFactory(ProductFactory):

    def getProduct(self, customization):
        return Cappuccino()


class BlackCoffeeFactory(ProductFactory):

    def getProduct(self, customization):
        return BlackCoffee()


class LemonadeFactory(ProductFactory):
    def getProduct(self, customization):
        return Lemonade()


class HotMilkFactory(ProductFactory):

    def getProduct(self, customization):
        return HotMilk()


class CocaColaFactory(ProductFactory):

    def getProduct(self, customization):
        return CocaCola()


class Cappuccino(CappuccinoFactory):

    def preparation(self, preparation: Preparation):
        pass

    def customization(self, customization: Customization):
        pass

    def make(self):
        print(type(self).__name__, 'was made!')

    def milk(self):
        print('Steamed milk foam was set ', type(self).__name__)

    def sugar(self):
        print('Some sugar was set ', type(self).__name__)

    def coffee(self):
        print('Some coffee was added ', type(self).__name__)


class BlackCoffee(BlackCoffeeFactory):


    def preparation(self, preparation: Preparation):
        pass

    def customization(self, customization: Customization):
        pass

    def make(self):
        print(type(self).__name__, 'was made!')

    def water(self):
        print('Water was set ', type(self).__name__)

    def coffee(self):
        print('Coffee was added ', type(self).__name__)


class Lemonade(LemonadeFactory):

    def preparation(self, preparation: Preparation):
        pass

    def customization(self, customization: Customization):
        pass

    def make(self):
        print(type(self).__name__, 'was made!')

    def water(self):
        print('Water in ', type(self).__name__, 'set')

    def sugar(self):
        print('Sugar was set', type(self).__name__)

    def lemonJuice(self):
        print('You have lemons you could make', type(self).__name__)


class HotMilk(HotMilkFactory):

    def preparation(self, preparation: Preparation):
        pass

    def customization(self, customization: Customization):
        pass

    def make(self):
        print(type(self).__name__, 'was made!')

    def milk(self):
        print('Milk', type(self).__name__)


class CocaCola(CocaColaFactory):
    def preparation(self, preparation: Preparation):
        pass

    def customization(self, customization: Customization):
        pass

    def make(self):
        print(type(self).__name__, 'was made!')

    def water(self):
        print('Water was set', type(self).__name__)

    def coke(self):
        print('ingredient was added', type(self).__name__)

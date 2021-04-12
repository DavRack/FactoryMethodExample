from __future__ import annotations
from abc import ABC, abstractmethod
from random import randint
import time

class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self) -> str:

        product = self.factory_method()

        result = f"Creator: The same creator's code has just worked with {product.operation()}"

        return result

class ConcreteCreatorTime(Creator):
    def factory_method(self) -> Product:
        if time.time_ns() % 2 == 0:
            return ConcreteProduct1()
        return ConcreteProduct2()

class ConcreteCreatorRandom(Creator):
    def factory_method(self) -> Product:

        if randint(1,2) == 1:
            return ConcreteProduct1()
        
        return ConcreteProduct2()

class Product(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass

class ConcreteProduct1(Product):
    def operation(self) -> str:
        return "ConcreteProduct1"

class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "ConcreteProduct2"

if __name__ == "__main__":
    print("Probando los diferentes Factory Methods")
    print(" ")

    for i in range(5):
        print("Ejemplo", i)
        print("App: Launched with the ConcreteCreator1.")
        print(ConcreteCreatorTime().some_operation())
        print("\n")

        print("App: Launched with the ConcreteCreatorRandom.")
        print(ConcreteCreatorRandom().some_operation())
        print("\n")


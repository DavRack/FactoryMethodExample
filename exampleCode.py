from __future__ import annotations
from abc import ABC, abstractmethod
from random import randint
import time


class Creator(ABC):
    """
    The Creator class declares the factory method that is supposed to return an
    object of a Product class. The Creator's subclasses usually provide the
    implementation of this method.
    """

    @abstractmethod
    def factory_method(self):
        """
        Note that the Creator may also provide some default implementation of
        the factory method.
        """
        pass

    def some_operation(self) -> str:
        """
        Also note that, despite its name, the Creator's primary responsibility
        is not creating products. Usually, it contains some core business logic
        that relies on Product objects, returned by the factory method.
        Subclasses can indirectly change that business logic by overriding the
        factory method and returning a different type of product from it.
        """

        # Call the factory method to create a Product object.
        product = self.factory_method()

        # Now, use the product.
        result = f"Creator: The same creator's code has just worked with {product.operation()}"

        return result


"""
Concrete Creators override the factory method in order to change the resulting
product's type.
"""


class ConcreteCreatorTime(Creator):
    """
    Note that the signature of the method still uses the abstract product type,
    even though the concrete product is actually returned from the method. This
    way the Creator can stay independent of concrete product classes.
    """

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
    """
    The Product interface declares the operations that all concrete products
    must implement.
    """

    @abstractmethod
    def operation(self) -> str:
        pass


"""
Concrete Products provide various implementations of the Product interface.
"""


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


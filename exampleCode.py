#!/usr/bin/env python 
from __future__ import annotations
from abc import ABC, abstractmethod
from random import randint
import time

state = 1

class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self) -> str:
        product = self.factory_method()

        result = f"El factory method ha lanzado {product.operation()}"

        return result

class CreatorToggle(Creator):
    def factory_method(self) -> Product:
        global state
        if state == 1:
            state *= -1
            return Car()
        state *= -1
        return Boat()

class CreatorRandom(Creator):
    def factory_method(self) -> Product:

        if randint(1,2) == 1:
            return Car()
        
        return Boat()

class Vehicle(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass

class Car(Vehicle):
    def operation(self) -> str:
        return "Car"

class Boat(Vehicle):
    def operation(self) -> str:
        return "Boat"

if __name__ == "__main__":
    for i in range(5):
        print ("###############")
        print ("## Ejemplo",i,"##")
        print ("###############")
        print("Usando ConcreteCreatorToggle.")
        print(CreatorToggle().some_operation())

        print("")

        print("Usando ConcreteCreatorRandom.")
        print(CreatorRandom().some_operation())
        print("")
        print("")


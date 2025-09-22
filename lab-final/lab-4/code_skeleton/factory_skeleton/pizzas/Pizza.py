from abc import ABC, abstractmethod
from typing import List, Any

from ingredients.cheese.Cheese import Cheese
from ingredients.clams.Clams import Clams
from ingredients.dough.Dough import Dough
from ingredients.pepperoni.Pepperoni import Pepperoni
from ingredients.sauce.Sauce import Sauce
from ingredients.veggies.Veggies import Veggies


class Pizza(ABC):
    _name: str = None
    _dough: Dough = None
    _sauce: Sauce = None
    _veggies: List[Veggies] = []
    _cheese: Cheese = None
    _pepperoni: Pepperoni = None
    _clams: Clams = None

    @abstractmethod
    def prepare(self) -> None:
        pass

    def bake(self) -> None:
        print('Bake for 25 minutes at 350')

    def cut(self) -> None:
        print('Cutting the pizza into diagonal slices')

    def box(self) -> None:
        print('Place pizza in official PizzaStore box')

    def set_name(self, name: str):
        self._name = name

    def get_name(self) -> str:
        return self._name

    def __get_class_name(self, object: Any):
        return type(object).__name__

    def __str__(self) -> str:
        return f'''
            Name: {self.get_name()}, 
            Dough: {self.__get_class_name(self._dough)}, 
            Sauce: {self.__get_class_name(self._sauce)}, 
            Veggies: {[self.__get_class_name(veggie) for veggie in self._veggies]},
            Cheese: {self.__get_class_name(self._cheese)}, 
            Pepperoni: {self.__get_class_name(self._pepperoni)}, 
            Clams: {self.__get_class_name(self._clams)}'''

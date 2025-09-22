from abc import ABC, abstractmethod
from ingredients.dough.Dough import Dough
from ingredients.sauce.Sauce import Sauce
from ingredients.cheese.Cheese import Cheese
from ingredients.veggies.Veggies import Veggies
from ingredients.pepperoni.Pepperoni import Pepperoni
from ingredients.clams.Clams import Clams


class PizzaIngredientFactory(ABC):
    @abstractmethod
    def create_dough(self) -> Dough: ...
    
    @abstractmethod
    def create_sauce(self) -> Sauce: ...
    
    @abstractmethod
    def create_cheese(self) -> Cheese: ...
    
    @abstractmethod
    def create_veggies(self) -> list[Veggies]: ...
    
    @abstractmethod
    def create_pepperoni(self) -> Pepperoni: ...
    
    @abstractmethod
    def create_clams(self) -> Clams: ...
    
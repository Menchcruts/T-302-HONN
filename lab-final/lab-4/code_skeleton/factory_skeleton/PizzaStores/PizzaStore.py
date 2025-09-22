from abc import ABC, abstractmethod
from pizzas.Pizza import Pizza
from pizzas.PizzaType import PizzaType
from ingredient_factories.PizzaIngredientFactory import PizzaIngredientFactory

class PizzaStore(ABC):
    _IngredientFactory: PizzaIngredientFactory = None
    _name: str = ""

    def order_pizza(self, pizza_type: PizzaType) -> Pizza:
        pizza = self.create_pizza(pizza_type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza

    @abstractmethod
    def create_pizza(self, pizza_type: PizzaType) -> Pizza: ...

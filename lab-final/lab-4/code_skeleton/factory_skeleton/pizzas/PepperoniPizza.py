from ingredient_factories.PizzaIngredientFactory import PizzaIngredientFactory
from pizzas.Pizza import Pizza

class PepperoniPizza(Pizza):
    def __init__(self, ingredient_factory: PizzaIngredientFactory, name: str):
        super().__init__()
        self._ingredient_factory = ingredient_factory
        self.set_name(f"{name} Style Pepperoni Pizza")

    def prepare(self):
        self._cheese = self._ingredient_factory.create_cheese()
        self._dough = self._ingredient_factory.create_dough()
        self._sauce = self._ingredient_factory.create_sauce()
        self._pepperoni = self._ingredient_factory.create_pepperoni() 
        return print(f"preparing: {self.get_name()}")

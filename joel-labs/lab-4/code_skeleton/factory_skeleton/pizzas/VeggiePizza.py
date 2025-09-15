from ingredient_factories.PizzaIngredientFactory import PizzaIngredientFactory
from pizzas.Pizza import Pizza

class VeggiePizza(Pizza):
    def __init__(self, ingredient_factory: PizzaIngredientFactory, name: str):
        super().__init__()
        self._ingredient_factory = ingredient_factory       
        self.set_name(f"{name} Style Veggie Pizza")

    def prepare(self):
        self._dough = self._ingredient_factory.create_dough()
        self._sauce = self._ingredient_factory.create_sauce()
        self._cheese = self._ingredient_factory.create_cheese()
        self._veggies = self._ingredient_factory.create_veggies()
        return print(f"preparing: {self.get_name()}")

from PizzaStores.PizzaStore import PizzaStore
from pizzas.PizzaType import PizzaType
from ingredient_factories.NYPizzaIngredientFactory import NYPizzaIngredientFactory
from pizzas.CheesePizza import CheesePizza
from pizzas.PepperoniPizza import PepperoniPizza
from pizzas.ClamPizza import ClamPizza
from pizzas.VeggiePizza import VeggiePizza
from pizzas.Pizza import Pizza

class NYStylePizzaStore(PizzaStore):
    def __init__(self):
        super().__init__()
        self._IngredientFactory = NYPizzaIngredientFactory()
        self._name = "New York"
    
    def create_pizza(self, pizza_type):
        pizza = None
        match pizza_type:
            case PizzaType.CHEESE:
                pizza = CheesePizza(self._IngredientFactory, self._name)
            case PizzaType.PEPPERONI:
                pizza = PepperoniPizza(self._IngredientFactory, self._name)
            case PizzaType.CLAM:
                pizza = ClamPizza(self._IngredientFactory, self._name)
            case PizzaType.VEGGIE:
                pizza = VeggiePizza(self._IngredientFactory, self._name)
        return pizza

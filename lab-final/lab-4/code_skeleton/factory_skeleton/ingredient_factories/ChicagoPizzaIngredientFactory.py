from ingredient_factories.PizzaIngredientFactory import PizzaIngredientFactory
from ingredients.dough.ThickCrustDough import ThickCrustDough
from ingredients.sauce.PlumTomatoSauce import PlumTomatoSauce
from ingredients.cheese.Mozzarella import Mozzarella
from ingredients.veggies import EggPlant, BlackOlives, Spinach
from ingredients.pepperoni.SlicedPepperoni import SlicedPepperoni
from ingredients.clams.FrozenClams import FrozenClams


class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self):
        return ThickCrustDough()
    
    def create_sauce(self):
        return PlumTomatoSauce()
    
    def create_cheese(self):
        return Mozzarella()
    
    def create_veggies(self):
        return [EggPlant.EggPlant(), BlackOlives.BlackOlives(), Spinach.Spinach()]
    
    def create_pepperoni(self):
        return SlicedPepperoni()
    
    def create_clams(self):
        return FrozenClams()

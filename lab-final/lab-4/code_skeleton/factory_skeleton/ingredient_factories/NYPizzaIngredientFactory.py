from ingredient_factories.PizzaIngredientFactory import PizzaIngredientFactory
from ingredients.dough.ThinCrustDough import ThinCrustDough
from ingredients.sauce.MarinaraSauce import MarinaraSauce
from ingredients.cheese.ReggianoCheese import ReggianoCheese
from ingredients.veggies import Garlic, Onion, Mushroom, RedPepper
from ingredients.pepperoni.SlicedPepperoni import SlicedPepperoni
from ingredients.clams.FreshClams import FreshClams


class NYPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self):
        return ThinCrustDough()
    
    def create_sauce(self):
        return MarinaraSauce()
    
    def create_cheese(self):
        return ReggianoCheese()
    
    def create_veggies(self):
        return [Garlic.Garlic(), Onion.Onion(), Mushroom.Mushroom(), RedPepper.RedPepper()]
    
    def create_pepperoni(self):
        return SlicedPepperoni()
    
    def create_clams(self):
        return FreshClams()
from PizzaStores.ChicagoStylePizzaStore import ChicagoStylePizzaStore
from PizzaStores.NYStylePizzaStore import NYStylePizzaStore
from PizzaStores.PizzaStore import PizzaStore
from pizzas.PizzaType import PizzaType


def order_all_pizzas_from_pizza_store(pizza_store: PizzaStore):
    for pizza_type in PizzaType:
        pizza = pizza_store.order_pizza(pizza_type)
        print(pizza)
        print('\n---\n')


if __name__ == '__main__':
    print('\n\n--- New York Style Pizzas ---\n\n')
    pizza_store = NYStylePizzaStore()
    order_all_pizzas_from_pizza_store(pizza_store)

    print('\n\n--- Chicago Style Pizzas ---\n\n')
    pizza_store = ChicagoStylePizzaStore()
    order_all_pizzas_from_pizza_store(pizza_store)

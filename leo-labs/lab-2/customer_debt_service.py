from ast import Try
from dataclasses import dataclass


@dataclass
class Customer:
    id: str
    debt: float

class CustomerNotFoundException(Exception):
    pass

class CustomerDebtService:
    def __init__(self) -> None:
        self.__fakeCustomers = [Customer(1,None), Customer(2, 3), Customer(3, 4)]
        # This example is initialized with int values but the methods enforce float i dont know if that
        # is intentional or not but i added a float conversion just in case. 

    def get_debt_of_customer(self, id: str) -> float:
        try:
            customer = self.__get_customer(id)
            if customer.debt is None: 
                return 0.0
            return float(customer.debt)   # enforce float return
        except StopIteration:
            return 0.0   #Problem 1.2.2 tells us to return 0 if no debt is registered i will 
                         #take it as the problem also wants me to return 0 if there is no customer found, 
                         #also 0 is not a float so i return 0.0 instead.

    def set_debt_of_customer(self, id: str, debt: float) -> None:

        try: 
            customer = self.__get_customer(id)
            customer.debt = debt
        except StopIteration:
            raise CustomerNotFoundException(f"Customer with id {id} not found")


    def __get_customer(self, id: str) -> Customer:
        return next((customer for customer in self.__fakeCustomers if customer.id == id))


def print_debt(customerId: str, debt: float):
    if debt == 0.0:
        print(f"Debt of customer with id: {customerId} is {0}")
    else:
        print(f"Debt of customer with id: {customerId} is {debt}")


if __name__ == '__main__':
    service = CustomerDebtService()

    customer_id = 1
    debt = service.get_debt_of_customer(customer_id)
    print_debt(customer_id, debt)

    status = service.set_debt_of_customer(customer_id, 10)
    debt = service.get_debt_of_customer(customer_id)
    print(status) 
    print_debt(customer_id, debt)

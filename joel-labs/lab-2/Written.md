# 1 - Clean Code
## 1.1
### 1)
The violation is in the `set_debt_of_customer` method, where it changes the state (sets the debt) and then returns some value, in this case a boolean. As the method is classified as a 'command', it should not return anything, according to the CQS guideline.
```py
class CustomerDebtService:
    def __init__(self) -> None:
        self.__fakeCustomers = [Customer(1, 2), Customer(2, 3), Customer(3, 4)]

    def get_debt_of_customer(self, id: str) -> float | None:
        try:
            customer = self.__get_customer(id)
            return customer.debt
        except StopIteration:
            return None

    def set_debt_of_customer(self, id: str, debt: float) -> bool:
        try:
            customer = self.__get_customer(id)
            customer.debt = debt
            return True
        except StopIteration:
            return False

    def __get_customer(self, id: str) -> Customer:
        return next((customer for customer in self.__fakeCustomers if customer.id == id))
```
### 2)
See code.

### 3)
We are adhering to the 'Prefer exceptions over error codes' guidline. This forces us to make our code more robust and less error-prone. 

## 1.2
### 1)
The problem with returning None/Null is that a method in the future that uses the debt variable might not be equipped to handle a Null debt, and will probably throw an exception and crash the program.

### 2)
See code

## 1.3
### 1)
```py
def get_breads(user_name_str: str):
    bro = fetch_user(user_name_str)
    save_user(bro)
    return bro.b4s
```
The given snippet of code is unclean because of:
- **Command-Query Separation**: It both changes the state and returns a value.
- `get_breads`: What does `breads` mean? What does the function return?
- `user_name_str`: We shouldn't encode types in the names.
- `bro`: Why is the variable called `bro` and not `user`?
- `b4s`: The variable name `b4s` is very unclear as to what it stores.
- **Errors**: There is no error handling to make sure `fetch_user` or `save_user` don't throw exceptions and crash the program. 

### 2)
a) What's wrong:
- There is only one function that does everything. The function:
    - Loads data.
    - Has no error handling for said data loading.
    - Creates merchant and buyer instances with base initalizers .instead of using dedicated methods.
    - Finally creates the order.
    - Loads data again to save the order.
    - Finally saves the order.
- The function takes in a lot of arguments.
- Unclear naming schemes for variables.

b) See code

# 2 - Design Principles
## 2.1
### 1
The _Rule of Three_ states that we may repeat the same snippet of code twice without abstraction. With the third time we should create some function or method instead.
### 2
_DRY_ states that we should never repeat ourselves, kind of like a _Rule of Two_, in which case we aren't allowed to write the same snippet of code more than once without abstraction. The problem with _DRY_ is that we may create an abstraction that turns out to be bad in the future.

### 3
At first glance this looks like a good use of _Rule of Three_, but further inspection reveals that it isn't. All the methods are inherently different. `EmailSender` uses all arguments, as it was created alongside the `MessagingSender`, but `SmsSender` and `AppNotificationSender` don't. `AppNotificationSender` even uses only two. We see now that this was a bad use of _Rule of Three_ because it doesn't really fall under it.

## 2.2
We want to make our code faster and more optimized so we can scale more easily, but we must also take into consideration readability. Most optimizations make little difference to the overall speed of a system and thus aren't worth the hit in readability.

## 2.3
_KISS_ states that we should keep everything as simple as possible. Many desing patterns and principles can fall on either side of that statement, such as the _Single Responsibility Principle_. It states that a class, function or method should only have one responsibility, thus keeping it simple. On the other hand, _Open/Closed Principle_ can be a violation of _Kiss_ as it states that entities should be open for extension but closed for modification. This can sometimes introduce abstractions that make the overall class more complicated.

## 2.4
A loosely coupled system is a system that's made up of components that know little about each other and communicate through interfaces. This makes it easier to replace components or test them.
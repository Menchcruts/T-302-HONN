# 1 Design Principles
## 1.1 Law of Demeter
### 1
The Law of Demeter states that an object should only talk to its immediate neighbours. It builds on loose coupling between classes so that A doesn't talk to C through B, making A dependent on C as well as B.
### 2
Lots of wrapper methods and functions can create a lot of clutter and boilerplate, making our program more bug prone. 
### 3
a) `ShapeRenderer` is technically now dependent on the `Circle` object, as it's reaching through `ShapeFactory` to get a `Circle` object, and then calling its methods directly.
b) This is acceptable because creating another class that does this will introduce more complexity to the program that might be difficult to understand or fix bugs in later.

## 1.2 SOLID
### 1
a) A class should only have on reason to change. In other words, a class should have one job only. We might have a class that creates orders and saves them to some file, but in the future we might change the data model to save to a database instead. Now we have to change the order creating class to also save to a database.

b) A module should be open to extension but closed to modification. This reduces regression bugs and lets multiple variants coexist (e.g. CSV_Exporter, JSON_Exporter and PDF_Exporter).

c) A subclass should behave like its base class when given to a function or method expecting the base class. If a function takes in a `Bird` instance and calls the method `fly()`, but we give it an instance of `Penguin`, the function might not behave correctly or crash the program altogether.

d) A class should not be forced to depend on methods it doesn't use. If a class has to implement a method it doesn't use and the interface changes that method in the future, the class has to do unnecessary changes.

e) High-level modules should not depend on low-level modules. If a payment system calls a `PayPalAPI` class to handle payments, it becomes a problem when we want to add another payment method. Instead, the class should call a `PaymentGateway` interface to handle payments, allowing us to add many more gateways while keeping the overall system clean and testable.

## 1.3 
### 1
a) 

### 2
a) This violates LSP as a penguin doesn't implement `fly()` like normal birds would.

b) We could have a base `Bird` class, with `FlyingBird` and `SwimmingBird` subclasses. Penguin would inherit from `SwimmingBird`. 

### 3
a) This violates DIP 

b) 
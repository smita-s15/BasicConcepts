# 🐍 Python OOP and Advanced Concepts

---

## 🔹 Object-Oriented Programming (OOP)

### 1. Inheritance
- Mechanism to derive a class (child) from another (parent).
- Promotes **code reuse**.

**Example:**
```python
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):  # Inherits from Animal
    def speak(self):
        return "Bark"

dog = Dog()
print(dog.speak())  # Output: Bark
```

---

### 2. Polymorphism
- Ability of different classes to implement the same method in different ways.
- Achieved via **method overriding** or **duck typing**.

**Example:**
```python
class Cat:
    def speak(self):
        return "Meow"

class Dog:
    def speak(self):
        return "Bark"

for animal in [Cat(), Dog()]:
    print(animal.speak())
# Output: Meow / Bark
```

---

### 3. Encapsulation
- Restricting direct access to variables and methods.
- Achieved using **private/protected attributes** (`_var`, `__var`).

**Example:**
```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # 1500
```

---

## 🔹 Decorators, Generators, Iterators

### 1. Decorators
- Functions that modify the behavior of another function.
- Often used for **logging, authentication, performance measurement**.

**Example:**
```python
def log_decorator(func):
    def wrapper():
        print("Before function call")
        result = func()
        print("After function call")
        return result
    return wrapper

@log_decorator
def greet():
    print("Hello!")

greet()
```

---

### 2. Generators
- Functions that use `yield` to produce a sequence of values.
- **Memory efficient** because values are produced lazily.
- In essence, yield transforms a regular function into a generator, providing a powerful and efficient way to manage and process data iteratively without the memory overhead associated with constructing entire collections upfront.

**Example:**
```python
def count_up_to(n):
    num = 1
    while num <= n:
        yield num
        num += 1

for val in count_up_to(3):
    print(val)
# Output: 1, 2, 3
```

---

### 3. Iterators
- An object with `__iter__()` and `__next__()` methods.
- Used to iterate over sequences.

**Example:**
```python
class Counter:
    def __init__(self, limit):
        self.limit = limit
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.num < self.limit:
            self.num += 1
            return self.num
        else:
            raise StopIteration

for i in Counter(3):
    print(i)
# Output: 1, 2, 3
```

---

## ✅ Summary
- **Inheritance** → Code reuse  
- **Polymorphism** → One interface, many implementations  
- **Encapsulation** → Restrict access, protect data  
- **Decorators** → Modify function behavior  
- **Generators** → Lazy evaluation, memory efficient  
- **Iterators** → Objects that support iteration with `__next__()`  

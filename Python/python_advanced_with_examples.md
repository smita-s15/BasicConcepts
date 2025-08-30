# 🐍 Python Quick Reference Guide (Extended with Examples)

## 9️⃣ Advanced Concepts

-   **Decorators** → Modify functions\

``` python
def decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()
```

-   **Generators** → `yield` values lazily\

``` python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for i in countdown(3):
    print(i)
```

-   **Comprehensions** → `[x*x for x in range(5)]`\

``` python
squares = [x*x for x in range(5)]
print(squares)  # [0,1,4,9,16]
```

-   **Context Managers** → `with open() as f:`\

``` python
with open("sample.txt", "w") as f:
    f.write("Hello File!")
```

-   **Type Hinting** → `def func(x: int) -> str:`\

``` python
def greet(age: int) -> str:
    return f"Age is {age}"
```

-   **Iterators** → `__iter__()`, `__next__()`\

``` python
class Counter:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.n:
            self.current += 1
            return self.current
        raise StopIteration

for num in Counter(3):
    print(num)
```

-   **Metaclasses, Dunder Methods, Data Classes**\

``` python
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

p = Point(1,2)
print(p)   # Point(x=1, y=2)
```

------------------------------------------------------------------------

## Python Methods

  ------------------------------------------------------------------------------
  Method Type  Decorator         First    Access Scope         Example Use Case
                                 Arg                           
  ------------ ----------------- -------- -------------------- -----------------
  Instance     (none)            `self`   Object attributes    Dog actions
  Method                                                       (`bark`)

  Class Method `@classmethod`    `cls`    Class-level          Count objects
                                          attributes           

  Static       `@staticmethod`   None     No object/class      Utility functions
  Method                                  required             
  ------------------------------------------------------------------------------

### Example:

``` python
class Dog:
    count = 0

    def __init__(self, name):
        self.name = name
        Dog.count += 1

    def bark(self):  # Instance Method
        print(f"{self.name} says Woof!")

    @classmethod
    def total_dogs(cls):  # Class Method
        return cls.count

    @staticmethod
    def info():  # Static Method
        return "Dogs are loyal animals."

d1 = Dog("Max")
d2 = Dog("Bella")
d1.bark()
print(Dog.total_dogs())
print(Dog.info())
```

------------------------------------------------------------------------

## 🔟 Object-Oriented Programming

  Concept         Meaning
  --------------- --------------------------------
  Class           Blueprint for objects
  Inheritance     Child gets parent properties
  Polymorphism    Same function, different types
  Encapsulation   `_var` or `__var`
  Abstraction     `abc` module

### Example:

``` python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

for pet in [Dog(), Cat()]:
    print(pet.sound())
```

------------------------------------------------------------------------

## Concurrency & Execution Models

  --------------------------------------------------------------------------------------
  Feature         Synchronous   Asynchronous          Multithreading   Multiprocessing
                                (`asyncio`)                            
  --------------- ------------- --------------------- ---------------- -----------------
  Execution Model One by one    Event loop            Many threads     Many processes
                                (non-blocking)                         

  Best for        Simple code   I/O-bound (APIs, DB)  I/O-bound        CPU-bound

  Memory Sharing  Single flow   Single flow           Shared memory    Separate memory

  Speed (I/O      Slow          Fast                  Fast             Fast
  tasks)                                                               

  Speed (CPU      Normal        Still single-threaded Blocked by GIL   True parallel
  tasks)                                                               

  Example         ---           FastAPI, aiohttp      Flask, Django    ML, NumPy, SciPy
  Frameworks                                                           
  --------------------------------------------------------------------------------------

### Example:

``` python
# Synchronous
def sync_func():
    print("Running sync")

sync_func()

# Asynchronous
import asyncio
async def async_func():
    print("Running async")
asyncio.run(async_func())

# Multithreading
import threading
def worker():
    print("Thread running")
t = threading.Thread(target=worker)
t.start()

# Multiprocessing
from multiprocessing import Process
def process_worker():
    print("Process running")
p = Process(target=process_worker)
p.start()
p.join()
```

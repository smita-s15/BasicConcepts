# Python Decorators – One Page Cheat Sheet 🚀

Decorators in Python allow you to **modify or enhance the behavior of functions and classes** without changing their actual code.  
They are used in logging, caching, authentication, profiling, and more.

---

## 🔹 Function Decorators

### Simple Decorator
```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function.")
        result = func(*args, **kwargs)
        print("After function.")
        return result
    return wrapper

@my_decorator
def greet(name):
    print(f"Hello, {name}!")

greet("Smita")
```

---

### Decorator with Arguments
```python
def repeat(num_times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def say_hello():
    print("Hello!")

say_hello()
```

---

## 🔹 Built-in Decorators

### @property
```python
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @name.deleter
    def name(self):
        del self._name

p = Person("Alice")
print(p.name)
p.name = "Bob"
print(p.name)
del p.name
```

---

### @classmethod
```python
class MyClass:
    count = 0
    def __init__(self):
        MyClass.count += 1

    @classmethod
    def get_instance_count(cls):
        return cls.count

a = MyClass()
b = MyClass()
print(MyClass.get_instance_count())  # 2
```

---

### @staticmethod
```python
class MathUtils:
    @staticmethod
    def add(x, y):
        return x + y

print(MathUtils.add(3, 5))  # 8
```

---

### @functools.wraps
```python
import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Before function")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet(name):
    """This function greets the user"""
    print(f"Hello, {name}!")

print(greet.__name__)  # greet
print(greet.__doc__)   # This function greets the user
```

---

### @functools.lru_cache
```python
import functools

@functools.lru_cache(maxsize=3)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print(fib(30))  # Cached & fast
```

---

## 🔹 Class Decorators
```python
def add_method(cls):
    def new_method(self):
        print("New method added by decorator!")
    cls.new_method = new_method
    return cls

@add_method
class MyClass:
    pass

obj = MyClass()
obj.new_method()
```

---

## 🔹 Advanced Use Cases

### Logging
```python
def log(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args} {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log
def multiply(a, b):
    return a * b

print(multiply(2, 5))
```

---

### Timing / Profiling
```python
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} executed in {end-start:.4f} sec")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)

slow_function()
```

---

### Authentication
```python
def requires_role(role):
    def decorator(func):
        def wrapper(user, *args, **kwargs):
            if user.get("role") == role:
                return func(user, *args, **kwargs)
            else:
                print("Access Denied!")
        return wrapper
    return decorator

@requires_role("admin")
def view_admin_panel(user):
    print("Welcome Admin!")

user1 = {"role": "user"}
user2 = {"role": "admin"}
view_admin_panel(user1)  # Access Denied!
view_admin_panel(user2)  # Welcome Admin!
```

---

## 🎯 Summary

- **Function decorators** → Wrap/extend functions.  
- **Built-in decorators** → `@property`, `@classmethod`, `@staticmethod`, `@functools.wraps`, `@functools.lru_cache`.  
- **Class decorators** → Modify or enhance classes.  
- **Advanced use cases** → Logging, profiling, authentication, caching.  

---

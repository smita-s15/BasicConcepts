# Python Quick Reference Notes

## 1. Control Flow

| Keyword        | Purpose                      | Example Use Case                   |
| -------------- | ---------------------------- | ---------------------------------- |
| `if/elif/else` | Conditional branching        | Decide grades based on marks       |
| `for`          | Loop through items           | Print all fruits in a list         |
| `while`        | Loop while condition is True | Count until a condition is met     |
| `break`        | Exit loop immediately        | Stop loop if a condition is met    |
| `continue`     | Skip current iteration       | Skip unwanted items in a loop      |
| `pass`         | Do nothing placeholder       | Empty loop or function placeholder |

## 2. \*args and \*\*kwargs

| Keyword    | Purpose                                        | Example Usage        |
| ---------- | ---------------------------------------------- | -------------------- |
| `*args`    | Accept variable number of positional arguments | `def func(*args)`    |
| `**kwargs` | Accept variable number of keyword arguments    | `def func(**kwargs)` |

**Example:**

```python
def greet(*args, **kwargs):
    print(args)
    print(kwargs)

greet(1, 2, 3, name='Alice', age=25)
```

## 3. Scope & Namespace

| Keyword / Concept | Purpose                                                                | Example       |
| ----------------- | ---------------------------------------------------------------------- | ------------- |
| `global`          | Modify a global variable inside a function                             | `global x`    |
| `nonlocal`        | Modify a variable in an enclosing function                             | `nonlocal y`  |
| LEGB Rule         | Order Python searches variables: Local → Enclosing → Global → Built-in | `x = 'local'` |

**Example:**

```python
x = 'global'

def outer():
    x = 'enclosing'
    def inner():
        x = 'local'
        print(x)  # local
    inner()
    print(x)  # enclosing

outer()
print(x)  # global
```

## 4. Advanced Concepts

| Concept               | Purpose / Use Case                            | Example                   |
| --------------------- | --------------------------------------------- | ------------------------- |
| Decorators            | Modify functions or classes                   | `@decorator`              |
| Generators            | Yield values one at a time (memory efficient) | `yield`                   |
| Generator Expressions | Compact lazy generator                        | `(x*x for x in range(5))` |
| Iterators             | Objects that can be iterated using `__next__` | `iter(lst)`               |
| Comprehensions        | Short way to create list, set, dict           | `[x*x for x in range(5)]` |
| Context Managers      | Auto-manage resources (`with`)                | `with open(...)`          |
| Metaclasses           | Classes for creating classes                  | `metaclass=Meta`          |
| Dunder Methods        | Special methods for object behavior           | `__init__, __str__`       |
| Data Classes          | Auto-generate common class methods            | `@dataclass`              |
| Type Hinting          | Indicate types for variables/functions        | `List[str]`               |

## 5. Object-Oriented Programming (OOP)

| Concept       | Purpose / Use Case                              | Example                               |
| ------------- | ----------------------------------------------- | ------------------------------------- |
| Classes       | Blueprints for objects                          | `class MyClass:`                      |
| Inheritance   | Child class gets properties of parent           | `class Child(Parent):`                |
| Polymorphism  | Same function name works for different types    | `def add(a,b): ...`                   |
| Encapsulation | Hide internal details using `_var` or `__var`   | `self._hidden`                        |
| Abstraction   | Define structure without implementation (`abc`) | `from abc import ABC, abstractmethod` |

## 6. Common Python Libraries

| Library     | Purpose / Use Case                                   | Example Usage                     |
| ----------- | ---------------------------------------------------- | --------------------------------- |
| os          | Interact with the operating system                   | `os.listdir('.')`                 |
| sys         | Access system-specific parameters & functions        | `sys.argv`                        |
| datetime    | Date/time manipulation                               | `datetime.datetime.now()`         |
| json        | Encode/decode JSON data                              | `json.loads()` / `json.dumps()`   |
| collections | Specialized container datatypes (`Counter`, `deque`) | `from collections import Counter` |
| itertools   | Iteration helpers (`permutations`, `combinations`)   | `itertools.permutations(lst)`     |
| functools   | Function tools (`reduce`, `lru_cache`)               | `functools.reduce(func, lst)`     |
| re          | Regular expression operations                        | `re.match()` / `re.sub()`         |
| subprocess  | Run external commands                                | `subprocess.run(['ls'])`          |
| math        | Mathematical functions                               | `math.sqrt(16)`                   |
| statistics  | Statistical functions                                | `statistics.mean([1,2,3])`        |
| logging     | Logging system events                                | `logging.info('message')`         |

## 7. Concurrency & Parallelism

| Concept         | Purpose / Use Case       | Example Usage                     |
| --------------- | ------------------------ | --------------------------------- |
| threading       | Run multiple threads     | `import threading`                |
| multiprocessing | Run multiple processes   | `import multiprocessing`          |
| async / await   | Asynchronous programming | `async def fetch(): await coro()` |
| queue.Queue     | Thread-safe queue        | `from queue import Queue`         |

**Example:**

```python
import threading, multiprocessing, asyncio, queue

# Thread example
def worker():
    print('Thread running')

t = threading.Thread(target=worker)
t.start()

# Async example
async def hello():
    print('Hello async')

asyncio.run(hello())

# Queue example
q = queue.Queue()
q.put(10)
print(q.get())  # Output: 10
```

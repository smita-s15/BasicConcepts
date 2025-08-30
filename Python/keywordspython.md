# 🐍 Python Quick Reference Guide

## 1️⃣ Core Python Concepts

### Data Types

| Type      | Mutable | Ordered   | Duplicates           | Example              |
| --------- | ------- | --------- | -------------------- | -------------------- |
| int       | ❌      | ✅        | ✅                   | `5`                  |
| float     | ❌      | ✅        | ✅                   | `3.14`               |
| complex   | ❌      | ✅        | ✅                   | `3+4j`               |
| str       | ❌      | ✅        | ✅                   | `"hello"`            |
| list      | ✅      | ✅        | ✅                   | `[1,2,3]`            |
| tuple     | ❌      | ✅        | ✅                   | `(1,2,3)`            |
| dict      | ✅      | ✅ (3.7+) | Keys: ❌, Values: ✅ | `{"a":1}`            |
| set       | ✅      | ❌        | ❌                   | `{1,2,3}`            |
| frozenset | ❌      | ❌        | ❌                   | `frozenset([1,2,3])` |
| bytes     | ❌      | ✅        | ✅                   | `b"abc"`             |
| bytearray | ✅      | ✅        | ✅                   | `bytearray(b"abc")`  |
| bool      | ❌      | ✅        | ✅                   | `True` / `False`     |

**Mnemonics:**

- **Mutable:** L = List, D = Dict, S = Set, B = Bytearray
- **Ordered:** Sequences (`list`, `tuple`, `str`, `dict`, `bytes`, `bytearray`, `range`)
- **Unique:** Set family (`set`, `frozenset`, `dict keys`)

---

## 2️⃣ Variables & Constants

- Assignment: `x = 5`
- Dynamic Typing: Type decided at runtime
- Unpacking: `a, b = [1, 2]`

---

## 3️⃣ Operators

### Arithmetic

| Operator | Meaning        | Example | Result |
| -------- | -------------- | ------- | ------ |
| `+`      | Addition       | `5+3`   | `8`    |
| `-`      | Subtraction    | `5-3`   | `2`    |
| `*`      | Multiplication | `5*3`   | `15`   |
| `/`      | Float Division | `5/2`   | `2.5`  |
| `//`     | Floor Division | `5//2`  | `2`    |
| `%`      | Modulus        | `5%2`   | `1`    |
| `**`     | Exponent       | `2**3`  | `8`    |

### Comparison

| Operator | Meaning          | Example | Result  |
| -------- | ---------------- | ------- | ------- |
| `==`     | Equal            | `5==5`  | `True`  |
| `!=`     | Not equal        | `5!=3`  | `True`  |
| `<`      | Less than        | `5<3`   | `False` |
| `>`      | Greater than     | `5>3`   | `True`  |
| `<=`     | Less or equal    | `5<=5`  | `True`  |
| `>=`     | Greater or equal | `5>=7`  | `False` |

### Logical

| Operator | Meaning           | Example           | Result  |
| -------- | ----------------- | ----------------- | ------- |
| `and`    | True if both True | `(5>3) and (2<4)` | `True`  |
| `or`     | True if any True  | `(5>3) or (2>4)`  | `True`  |
| `not`    | Negation          | `not (5>3)`       | `False` |

### Bitwise

| Operator | Meaning     | Example  | Result |     |     |
| -------- | ----------- | -------- | ------ | --- | --- |
| `&`      | AND         | `5 & 3`  | `1`    |     |     |
| \`       | \`          | OR       | \`5    | 3\` | `7` |
| `^`      | XOR         | `5 ^ 3`  | `6`    |     |     |
| `~`      | NOT         | `~5`     | `-6`   |     |     |
| `<<`     | Left Shift  | `5 << 1` | `10`   |     |     |
| `>>`     | Right Shift | `5 >> 1` | `2`    |     |     |

### Membership

| Operator | Meaning             | Example            | Result |
| -------- | ------------------- | ------------------ | ------ |
| `in`     | Exists in container | `'a' in 'cat'`     | `True` |
| `not in` | Not exists          | `5 not in [1,2,3]` | `True` |

### Identity

| Operator | Meaning          | Example                    | Result |
| -------- | ---------------- | -------------------------- | ------ |
| `is`     | Same object      | `a=[1]; b=a; a is b`       | `True` |
| `is not` | Different object | `a=[1]; b=[1]; a is not b` | `True` |

---

## 4️⃣ Control Flow

| Keyword            | Purpose               | Example                |
| ------------------ | --------------------- | ---------------------- |
| `if / elif / else` | Conditional branching | Grade decision         |
| `for`              | Loop through items    | `for fruit in list:`   |
| `while`            | Loop until condition  | `while x<5:`           |
| `break`            | Exit loop             | Stop if condition      |
| `continue`         | Skip iteration        | Skip unwanted items    |
| `pass`             | Placeholder           | Empty function or loop |

---

## 5️⃣ Functions

- Define: `def func_name(params):`
- Return: `return value`
- Default Args: `def f(x=10)`
- Variable Args: `*args` → positional args, `**kwargs` → keyword args

```python
def add(*args): return sum(args)
def greet(*args, **kwargs):
    print(args)
    print(kwargs)
```

---

## 6️⃣ Scope & Namespace

# ⚡ Python LEGB Rule (Single Example)

Python resolves variables in the order:  
**Local → Enclosing → Global → Built-in**

## 🔹 LEGB Rule

- **Local (L)** → Variables inside the current function/block.
- **Enclosing (E)** → Variables in the enclosing (outer) function(s).
- **Global (G)** → Variables defined at the top level of the module (file).
- **Built-in (B)** → Names preloaded by Python (e.g., `len`, `range`, `print`).

---

## 🔹 Example

```python
x = "Global X"   # Global

def outer():
    x = "Enclosing X"   # Enclosing

    def inner():
        x = "Local X"   # Local
        print("1) Local:", x)  # Local wins

    def inner_no_local():
        print("2) Enclosing:", x)  # Found in enclosing scope

    def inner_global():
        global x
        print("3) Global (before change):", x)  # Uses global
        x = "Changed Global X"
        print("3) Global (after change):", x)

    def inner_builtin():
        print("4) Built-in len:", len("hello"))  # Built-in

    inner()
    inner_no_local()
    inner_global()
    inner_builtin()

outer()
print("Outside:", x)  # Global modified
```

---

## 7️⃣ Exception Handling

| Keyword   | Purpose                  |
| --------- | ------------------------ |
| `try`     | Test block               |
| `except`  | Handle errors            |
| `finally` | Always execute           |
| `raise`   | Raise exception manually |
| `assert`  | Debug check              |

---

## 8️⃣ Imports & Modules

- `import module`, `from module import item`, `as` → alias
- `__init__.py` → marks package

---

## 9️⃣ Advanced Concepts

- Decorators → Modify functions
- Generators → `yield` values lazily
- Comprehensions → `[x*x for x in range(5)]`
- Context Managers → `with open() as f:`
- Type Hinting → `def func(x: int) -> str:`
- Iterators → `__iter__()`, `__next__()`
- Metaclasses, Dunder Methods, Data Classes

---

## Python Methods

# 🐍 Python Methods: Instance vs Class vs Static

---

## 📌 1. Instance Method

- Default method type.
- Takes `self` as the first argument (represents the object).
- Used to access/modify **object attributes**.

```python
class Dog:
    def __init__(self, name):
        self.name = name

    # Instance method
    def bark(self):
        return f"{self.name} is barking!"

d = Dog("Bruno")
print(d.bark())
# Output: Bruno is barking!
```

---

## 📌 2. Class Method

- Declared with `@classmethod`.
- Takes `cls` as the first argument (represents the **class itself**).
- Used to access/modify **class-level data**.

```python
class Dog:
    count = 0  # Class variable

    def __init__(self, name):
        self.name = name
        Dog.count += 1

    @classmethod
    def get_count(cls):
        return f"Total Dogs: {cls.count}"

d1 = Dog("Bruno")
d2 = Dog("Rocky")
print(Dog.get_count())
# Output: Total Dogs: 2
```

---

## 📌 3. Static Method

- Declared with `@staticmethod`.
- No `self` or `cls`.
- Behaves like a **normal function inside a class** (logical grouping).

```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

print(MathUtils.add(5, 7))
# Output: 12
```

---

## 🔹 Quick Comparison

| Method Type     | Decorator       | First Arg | Access Scope             | Example Use Case     |
| --------------- | --------------- | --------- | ------------------------ | -------------------- |
| Instance Method | (none)          | `self`    | Object attributes        | Dog actions (`bark`) |
| Class Method    | `@classmethod`  | `cls`     | Class-level attributes   | Count objects        |
| Static Method   | `@staticmethod` | None      | No object/class required | Utility functions    |

---

## 🔟 Object-Oriented Programming

| Concept       | Meaning                        |
| ------------- | ------------------------------ |
| Class         | Blueprint for objects          |
| Inheritance   | Child gets parent properties   |
| Polymorphism  | Same function, different types |
| Encapsulation | `_var` or `__var`              |
| Abstraction   | `abc` module                   |

---

| Feature            | Synchronous | Asynchronous (`asyncio`)  | Multithreading | Multiprocessing  |
| ------------------ | ----------- | ------------------------- | -------------- | ---------------- |
| Execution Model    | One by one  | Event loop (non-blocking) | Many threads   | Many processes   |
| Best for           | Simple code | I/O-bound (APIs, DB)      | I/O-bound      | CPU-bound        |
| Memory Sharing     | Single flow | Single flow               | Shared memory  | Separate memory  |
| Speed (I/O tasks)  | Slow        | Fast                      | Fast           | Fast             |
| Speed (CPU tasks)  | Normal      | Still single-threaded     | Blocked by GIL | True parallel    |
| Example Frameworks | —           | FastAPI, aiohttp          | Flask, Django  | ML, NumPy, SciPy |

## 1️⃣1️⃣ Common Python Libraries

- `os`, `sys`, `datetime`, `json`
- `collections`, `itertools`, `functools`
- `re`, `subprocess`, `math`, `statistics`, `logging`

---

## 1️⃣2️⃣ File & Data Handling

- `open()`, `read()`, `write()`, `csv`, `pickle`, `sqlite3`

---

## 1️⃣3️⃣ Web & API

- `Flask`, `Django`, `FastAPI`, `requests`, `urllib`, JSON APIs

---

## 1️⃣4️⃣ Data Science & AI

- `NumPy`, `Pandas`, `Matplotlib`, `Seaborn`, `Scikit-learn`, `PyTorch`, `TensorFlow`

---

## 1️⃣5️⃣ Concurrency

- `threading`, `multiprocessing`, `async / await`, `queue.Queue`

```python
import threading, asyncio, queue

def worker():
    print('Thread running')

t = threading.Thread(target=worker)
t.start()

async def hello():
    print('Hello async')

asyncio.run(hello())

q = queue.Queue()
q.put(10)
print(q.get())  # 10
```

---

## 1️⃣6️⃣ Best Practices

- PEP8, venv/pipenv, pip, requirements.txt, unittest, pytest

---

## 1️⃣7️⃣ Key Python Concepts

- Everything is an object, Dynamic & Duck Typing
- Mutable vs Immutable, Shallow vs Deep Copy, Pass-by-reference
- First-class functions & closures, Iterable vs Iterator
- Global Interpreter Lock (GIL) & Garbage Collection, EAFP vs LBYL
- String formatting: f-strings, `.format()`, `%`
- Virtual environments & modular code
- Garbage Collection is the process by which Python automatically frees memory that is no longer in use, i.e., objects that are no longer referenced anywhere in your program.

# 🐍 Python Copying: Shallow vs Deep Copy

---

## 🔹 What They Are

- **Shallow Copy** → Creates a **new object**, but **does not create copies of nested objects**.
  Changes in nested objects affect both original and copied object.

- **Deep Copy** → Creates a **new object** and also **recursively copies all nested objects**.
  Changes in nested objects **do not affect** the original object.

---

## 🔹 Example

```python
import copy

# Original nested list
original = [[1, 2], [3, 4]]

# Shallow copy
shallow = copy.copy(original)

# Deep copy
deep = copy.deepcopy(original)

# Modify nested object
original[0][0] = 99

print("Original:", original)   # [[99, 2], [3, 4]]
print("Shallow:", shallow)     # [[99, 2], [3, 4]] -> affected
print("Deep:", deep)           # [[1, 2], [3, 4]]  -> unaffected
```

---

## 🔹 Key Points

| Feature                               | Shallow Copy             | Deep Copy                        |
| ------------------------------------- | ------------------------ | -------------------------------- |
| Copies top-level object               | ✅                       | ✅                               |
| Copies nested objects                 | ❌                       | ✅                               |
| Affected by changes in nested objects | ✅                       | ❌                               |
| Use                                   | Fast, for simple objects | Safe, for nested/complex objects |

---

## 🔹 Summary

- **Use `copy.copy()`** → Shallow copy.
- **Use `copy.deepcopy()`** → Deep copy.
- Remember: If your object contains nested structures (lists, dicts, objects), \*\*shallow copy may lead to unexpected m

# ⚡ Python Error Handling Styles: EAFP vs LBYL

---

## 🔹 What They Mean

Python programmers often follow **two styles** to handle potential errors:

| Style    | Full Form                                 | Description                                                               | Example                                                          |
| -------- | ----------------------------------------- | ------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| **EAFP** | Easier to Ask Forgiveness than Permission | Try to do the operation directly and **handle exceptions** if they occur. | `try: value = my_dict['key'] except KeyError: value = None`      |
| **LBYL** | Look Before You Leap                      | Check conditions **before performing the operation** to avoid exceptions. | `if 'key' in my_dict: value = my_dict['key'] else: value = None` |

---

## 🔹 Key Differences

| Aspect      | EAFP                                                                        | LBYL                                               |
| ----------- | --------------------------------------------------------------------------- | -------------------------------------------------- |
| Approach    | Attempt first, handle errors if they happen                                 | Check first, then act                              |
| Pythonic?   | ✅ Pythonic, preferred in Python                                            | ❌ Less Pythonic, more common in other languages   |
| Performance | Often faster for normal cases; may be slower if exceptions occur frequently | Can be slower if checks are redundant              |
| Use Case    | File operations, dictionary access, type conversion                         | Simple validations, avoiding exceptions altogether |

---

## 🔹 Examples

### 1. EAFP (Pythonic way) Easier to Ask Forgiveness than Permission

```python
my_dict = {'a': 1}

try:
    value = my_dict['b']
except KeyError:
    value = 0

print(value)  # 0
```

### 2. LBYL (Check first) Look Before You Leap

```python
my_dict = {'a': 1}

if 'b' in my_dict:
    value = my_dict['b']
else:
    value = 0

print(value)  # 0
```

---

### ✅ Takeaways

- **EAFP**: “Ask forgiveness later” → rely on exceptions.
- **LBYL**: “Check before you act” → rely on checks.
- Python generally encourages **EAFP** because it’s clean, concise, and fits dynamic typing.

| Mode   | Meaning      | Notes                                           |
| ------ | ------------ | ----------------------------------------------- |
| `"r"`  | Read         | Default, file must exist                        |
| `"w"`  | Write        | Creates file if not exist, overwrites if exists |
| `"a"`  | Append       | Adds content at the end, creates if not exist   |
| `"rb"` | Read binary  | For images, pdf, etc.                           |
| `"wb"` | Write binary | For binary files                                |
| `"r+"` | Read & write | Must exist, cursor at start                     |
| `"w+"` | Write & read | Overwrites file                                 |

---

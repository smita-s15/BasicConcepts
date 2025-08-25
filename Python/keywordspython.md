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

- LEGB Rule: Local → Enclosing → Global → Built-in
- `global` → Access global variable
- `nonlocal` → Access enclosing variable

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

| Method Type     | Decorator       | First Arg | Access Scope             | Example Use Case     |
| --------------- | --------------- | --------- | ------------------------ | -------------------- |
| Instance Method | (none)          | `self`    | Object attributes        | Dog actions (`bark`) |
| Class Method    | `@classmethod`  | `cls`     | Class-level attributes   | Count objects        |
| Static Method   | `@staticmethod` | None      | No object/class required | Utility functions    |

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
- GIL & Garbage Collection, EAFP vs LBYL
- String formatting: f-strings, `.format()`, `%`
- Virtual environments & modular code

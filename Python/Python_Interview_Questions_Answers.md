# Python Interview Questions and Answers

## 🧩 1. Core Python (Basics)

**Q1: What are Python’s key features?**

- High-level, interpreted
- Dynamically typed
- Object-oriented
- Large standard library
- Extensible and embeddable
- Portable across platforms
- Readable syntax

**Q2: Difference between Python 2 and Python 3**

| Feature  | Python 2                  | Python 3                  |
| -------- | ------------------------- | ------------------------- |
| Print    | Statement `print 'Hello'` | Function `print('Hello')` |
| Unicode  | ASCII by default          | Unicode by default        |
| Division | `/` does integer division | `/` does float division   |

**Q3: What is PEP 8 and why is it important?**

- PEP 8 is Python's style guide.
- It ensures code readability, consistency, and maintainability.

**Q4: Mutable vs Immutable data types**

- Mutable: can be changed in place (list, dict, set)
- Immutable: cannot be changed (tuple, str, int, frozenset)

**Q5: Python’s memory management and garbage collection**

- Python uses reference counting and a cyclic garbage collector.
- Automatically frees memory of objects not referenced.

**Q6: Difference between shallow copy and deep copy**

- Shallow copy: copies object structure but nested objects still shared
- Deep copy: copies everything recursively, no shared objects

**Q7: Global, local, and nonlocal variables**

- Local: defined inside function
- Global: defined outside function
- Nonlocal: used to modify variable in outer non-global scope

**Q8: Difference between `is` and `==`**

- `is`: compares memory location (identity)
- `==`: compares value

**Q9: `id()` function**

- Returns unique identifier (memory address) of an object

**Q10: Output**

```python
a = [1, 2, 3]
b = a
a.append(4)
print(b)
```

Output: `[1, 2, 3, 4]` (b references same list as a)

## 📦 2. Data Types and Data Structures

**Q1: Python’s built-in data types**

- int, float, complex, bool, str, list, tuple, set, frozenset, dict, bytes, bytearray, NoneType

**Q2: Difference between list, tuple, set, dictionary**

- List: ordered, mutable, allows duplicates
- Tuple: ordered, immutable, allows duplicates
- Set: unordered, mutable, no duplicates
- Dict: key-value pairs, keys unique

**Q3: Why are sets faster for membership testing?**

- Implemented as hash tables, O(1) average time

**Q4: Strings are immutable**

- Cannot modify existing string, only create new ones

**Q5: Modifying a tuple**

- Raises `TypeError`; elements cannot be changed

**Q6: Python handles large integers**

- Automatically converts to long integers (arbitrary precision)

**Q7: Slicing**

```python
lst[1:5:2]  # start:stop:step
str[::2]    # every second character
```

**Q8: Flatten nested list**

```python
def flatten(lst):
    return [item for sublist in lst for item in sublist]
```

**Q9: Set inside another set**

- Not allowed; sets must contain hashable (immutable) elements

**Q10: Dictionary implementation**

- Implemented as a hash table for fast key lookup

## ⚙️ 3. Functions and Scope

**Q1: \*args and **kwargs\*\*

- `*args`: variable positional arguments
- `**kwargs`: variable keyword arguments

**Q2: Lambda function**

- Anonymous function: `lambda x: x+1`

**Q3: Closures**

- Function remembers environment where it was defined

**Q4: Recursion example**

```python
def factorial(n):
    return 1 if n==0 else n*factorial(n-1)
```

**Q5: return vs yield**

- `return`: returns value and exits function
- `yield`: returns generator and pauses function

**Q6: Decorators example**

```python
def decorator(func):
    def wrapper():
        print('Before')
        func()
    return wrapper
```

**Q7: Higher-order functions**

- Functions taking functions as arguments or returning them

**Q8: nonlocal keyword**

- Allows modifying outer (non-global) variables inside nested function

**Q9: Function annotation**

- Syntax: `def add(a: int, b: int) -> int:`

**Q10: Positional-only vs keyword-only**

- Positional-only: `/` in parameters
- Keyword-only: `*` in parameters

## 🧱 4. Object-Oriented Programming (OOP)

**Q1: Class and object**

- Class: blueprint
- Object: instance of class

**Q2: Class vs instance variable**

- Class variable shared among all instances
- Instance variable unique per object

**Q3: Inheritance types**

- Single, multiple, multilevel, hierarchical, hybrid

**Q4: Method overriding vs overloading**

- Overriding: subclass redefines parent method
- Overloading: not supported directly; can use default args

**Q5: Multiple inheritance and MRO**

- Python uses C3 linearization to resolve conflicts

**Q6: Polymorphism**

- Same interface, different implementations

**Q7: Magic/dunder methods**

- `__init__`, `__str__`, `__repr__`, etc.

**Q8: Operator overloading example**

```python
class Number:
    def __init__(self, n): self.n = n
    def __add__(self, other): return self.n + other.n
```

**Q9: Encapsulation**

- Private variables with `_` or `__` prefix, access via methods

**Q10: @classmethod, @staticmethod, instance method**

- Instance: access instance (`self`)
- Class: access class (`cls`)
- Static: no access to instance or class

## 💾 5. File Handling & Exceptions

**Q1: Read/write files**

```python
with open('file.txt', 'r') as f:
    data = f.read()
```

**Q2: File modes**

- `'r'`, `'w'`, `'a'`, `'rb'`, `'wb'` etc.

**Q3: Handle exceptions**

```python
try:
    ...
except Exception as e:
    print(e)
```

**Q4: Exception vs BaseException**

- BaseException is parent of all exceptions
- Exception is for normal errors

**Q5: finally block**

- Always executed, used for cleanup

**Q6: Custom exception**

```python
class MyError(Exception): pass
```

**Q7: If file not closed**

- Can lead to memory leaks, data not flushed

**Q8: with open()**

- Automatically closes file, ensures cleanup

**Q9: try, except, else, finally**

- `try -> except -> else -> finally`
- `else` runs if no exception

**Q10: Raise exception manually**

```python
raise ValueError('Error')
```

## 🧮 6. Advanced Topics

**Q1: Iterators and generators**

- Iterator: object with `__iter__()` and `__next__()`
- Generator: yields values lazily using `yield`

**Q2: deepcopy vs copy**

- `copy.copy()`: shallow copy
- `copy.deepcopy()`: deep copy

**Q3: Context manager**

- Object defining `__enter__` and `__exit__` for `with` statement

**Q4: Python GIL**

- Global Interpreter Lock; allows only one thread to execute Python bytecode at a time

**Q5: Modules and packages**

- Module: single Python file
- Package: directory of modules with `__init__.py`

**Q6: **init**.py**

- Marks directory as package; can execute initialization code

**Q7: Metaprogramming**

- Writing code that manipulates code itself (e.g., class decorators)

**Q8: Monkey patching**

- Modify classes or modules at runtime

**Q9: Coroutines and async/await**

- Coroutine: pause/resume execution using `await`
- async/await syntax for asynchronous programming

**Q10: Threading vs multiprocessing**

- Threading: multiple threads, share memory, limited by GIL
- Multiprocessing: separate processes, independent memory, parallel execution

## 🧰 7. Libraries and Tools

**Q1: Dependency management**

- Use `pip`, `requirements.txt`, virtual environments

**Q2: virtualenv or venv**

- Isolated Python environment to manage dependencies

**Q3: Common libraries**

- pandas: dataframes
- numpy: arrays, matrices, math operations

**Q4: Connect to SQL database**

```python
import sqlite3
conn = sqlite3.connect('db.sqlite3')
```

**Q5: pytest and test case**

```python
def test_add():
    assert add(2,3) == 5
```

## 🧩 8. Coding Practice (Short Exercises)

**1. Reverse string without slicing**

```python
def reverse_string(s):
    return ''.join(reversed(s))
```

**2. Factorial (recursion and loop)**

```python
def fact_rec(n):
    return 1 if n==0 else n*fact_rec(n-1)

def fact_loop(n):
    res=1
    for i in range(1,n+1): 
        res*=i
    return res
```

**3. Count word frequency**

```python
from collections import Counter
Counter('some string'.split())
```

**4. Find duplicates in list**

```python
[item for item in lst if lst.count(item)>1]
```

**5. Check prime**

```python
def is_prime(n):
    if n<=1: return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0: return False
    return True
```

**6. Remove duplicates without set()**

```python
list(dict.fromkeys(lst))
```

**7. Merge two sorted lists**

```python
import heapq
merged = list(heapq.merge(list1, list2))
```

**8. Second largest element**

```python
sorted(set(lst))[-2]
```

**9. Check anagrams**

```python
sorted(str1) == sorted(str2)
```

**10. Fibonacci using generator**

```python
def fib(n):
    a,b=0,1
    for _ in range(n):
        yield a
        a,b=b,a+b
```

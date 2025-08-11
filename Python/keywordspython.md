# Python Big Keywords & Key Concepts (with Meanings)

## 1. Core Python Language

### Data Types

- **int** → Integer number (e.g., `5`, `-42`)
- **float** → Decimal number (e.g., `3.14`)
- **complex** → Number with real and imaginary parts (e.g., `3+4j`)
- **str** → Text (string of characters)
- **list** → Mutable ordered collection (e.g., `[1, 2, 3]`)
- **tuple** → Immutable ordered collection (e.g., `(1, 2, 3)`)
- **dict** → Key-value mapping (e.g., `{"a": 1}`)
- **set** → Unordered unique values (e.g., `{1, 2, 3}`)
- **frozenset** → Immutable set
- **bool** → Boolean value `True` or `False`
- **bytes** → Immutable sequence of bytes
- **bytearray** → Mutable sequence of bytes

### Variables & Constants

- **Assignment** → Store a value in a variable (`x = 5`)
- **Dynamic Typing** → Variable type is decided at runtime
- **Unpacking** → Assign multiple values from a collection to variables (`a, b = [1, 2]`)

### Operators

- **Arithmetic** → `+`, `-`, `*`, `/`, `//`, `%`, `**`
- **Comparison** → `==`, `!=`, `<`, `>`, `<=`, `>=`
- **Logical** → `and`, `or`, `not`
- **Bitwise** → `&`, `|`, `^`, `~`, `<<`, `>>`
- **Membership** → `in`, `not in`
- **Identity** → `is`, `is not`

### Control Flow

- **if / elif / else** → Conditional branching
- **for** → Loop through an iterable
- **while** → Loop while condition is true
- **break** → Exit loop immediately
- **continue** → Skip to the next loop iteration
- **pass** → Do nothing (placeholder)

### Functions

- **def** → Define a function
- **Parameters** → Variables inside function definition
- **Return Values** → Send result back using `return`
- **Default Arguments** → Parameters with default values (`def f(x=10)`)
- **\*args** → Variable number of positional arguments
- **\*\*kwargs** → Variable number of keyword arguments

### Scope & Namespace

- **global** → Use a variable from the global scope
- **nonlocal** → Use variable from an enclosing scope (but not global)
- **LEGB Rule** → Local → Enclosing → Global → Built-in

### Exception Handling

- **try** → Block of code to test for errors
- **except** → Handle the error
- **finally** → Always executed (cleanup)
- **raise** → Manually raise an exception
- **assert** → Debugging check, raises error if condition false

### Imports & Modules

- **import** → Bring in a module
- **from ... import** → Import specific items from a module
- **as** → Alias for a module or function
- **packages** → Folder containing multiple modules
- **\_\_init\_\_.py** → Marks a folder as a Python package

---

## 2. Advanced Python Concepts

- **Decorators** → Functions that modify other functions/classes
- **Generators** → Functions that yield values (`yield`) one at a time
- **Generator Expressions** → `(x*x for x in range(5))`
- **Iterators** → Objects with `__iter__()` and `__next__()` methods
- **Comprehensions** → Short way to create collections: list, dict, set
- **Context Managers** → Use `with` to manage resources automatically
- **Metaclasses** → Classes for creating other classes
- **Dunder Methods** → Special methods like `__init__`, `__str__`
- **Data Classes** → Use `@dataclass` to auto-generate class methods
- **Type Hinting** → Indicate variable/function parameter types (`List[str]`)

---

## 3. Object-Oriented Programming (OOP)

- **Classes** → Blueprints for objects
- **Inheritance** → Child class gets properties of parent class
- **Polymorphism** → Same function name works for different types
- **Encapsulation** → Hide internal details using `_var` or `__var`
- **Abstraction** → Define structure without implementation (`abc` module)

---

## 4. Python Standard Library Keywords

- **os** → Interact with the operating system
- **sys** → Access system-specific parameters & functions
- **datetime** → Date/time manipulation
- **json** → Encode/decode JSON data
- **collections** → Specialized container datatypes (`Counter`, `deque`)
- **itertools** → Iteration helpers (`permutations`, `combinations`)
- **functools** → Function tools (`reduce`, `lru_cache`)
- **re** → Regular expression operations
- **subprocess** → Run external commands
- **math / statistics** → Mathematical functions
- **logging** → Logging system events

---

## 5. Data & File Handling

- **open()** → Open a file
- **read() / write()** → Read/write to file
- **csv** → Work with CSV files
- **pickle** → Serialize/deserialize Python objects
- **sqlite3** → Built-in lightweight database

---

## 6. Web & API Development

- **Flask / Django / FastAPI** → Web frameworks
- **requests** → Make HTTP requests
- **urllib** → URL handling
- **JSON APIs** → Data exchange between systems

---

## 7. Data Science & AI Keywords

- **NumPy** → Numerical computing with arrays
- **Pandas** → Data manipulation with DataFrames
- **Matplotlib / Seaborn** → Data visualization
- **Scikit-learn** → Machine learning algorithms
- **PyTorch / TensorFlow** → Deep learning frameworks

---

## 8. Concurrency & Parallelism

- **threading** → Run multiple threads
- **multiprocessing** → Run multiple processes
- **async / await** → Asynchronous programming
- **queue.Queue** → Thread-safe queue

---

## 9. Best Practices

- **PEP 8** → Python style guide
- **venv / pipenv** → Virtual environments
- **pip** → Install packages
- **requirements.txt** → Dependency list
- **unittest / pytest** → Testing frameworks

---

## 10. Key Python Concepts

- **Everything is an object** → All values are objects
- **Dynamic Typing** → Types decided at runtime
- **Duck Typing** → Type compatibility based on behavior
- **Mutable vs Immutable** → Objects that can/can’t change
- **Shallow vs Deep Copy** → Copy references vs actual data
- **Pass-by-Object-Reference** → Arguments passed as references
- **First-Class Functions** → Functions as variables/arguments
- **Closures** → Inner functions remember outer scope
- **Iterable vs Iterator** → Iterable can be looped, iterator generates items
- **Interning** → Reusing small immutable objects for performance
- **GIL** → Only one Python thread runs bytecode at a time
- **Garbage Collection** → Auto memory cleanup
- **EAFP vs LBYL** → Try/except vs checking before acting
- **Unpacking** → Assign multiple values from collections
- **String Formatting** → f-strings, `.format()`, `%` formatting
- **Virtual Environment Isolation** → Isolate dependencies
- **Modules & Packages** → Organize reusable code

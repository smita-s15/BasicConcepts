# JavaScript Interview Keywords & Trending Concepts (Optimized)

---

## Temporal Dead Zone (TDZ)

**Temporal Dead Zone (TDZ)** is a behavior in JavaScript related to the `let` and `const` declarations.

### What is TDZ?

- When a variable is declared using `let` or `const`, it is **hoisted** to the top of its block scope, similar to `var`.
- However, unlike `var`, these variables are **not initialized** immediately.
- The time between entering the scope and the actual declaration line is called the **Temporal Dead Zone**.
- During this period, **accessing the variable results in a `ReferenceError`**.

### Why does TDZ exist?

- TDZ helps catch errors where a variable is used **before it is declared**, making the code safer and more predictable.
- It prevents accidental use of variables before their proper initialization.

### Example:

````javascript
{
  // Accessing before declaration causes ReferenceError
  console.log(a); // ReferenceError: Cannot access 'a' before initialization

  let a = 10; // Variable is declared and initialized here
  console.log(a); // 10
}

# 1. Variable Declarations (var, let, const)

### var

- **Scope:** Function-scoped
  Variables declared with `var` are accessible anywhere within the function they are declared in. If declared outside a function, they are global.

- **Hoisting:** Yes
  `var` declarations are hoisted to the top of their scope and initialized with `undefined`. Accessing them before the declaration line returns `undefined`.

- **Redeclaration:** Allowed
  You can declare the same variable multiple times without error.

- **Example:**

  ```javascript
  function example() {
    console.log(x); // undefined (hoisted)
    var x = 5;
    console.log(x); // 5

    var x = 10; // redeclaration allowed
    console.log(x); // 10
  }
  example();
````

### let

- **Scope:** Block-scoped  
  Variables exist only within the nearest enclosing `{}` block (loops, if blocks, functions).


- **Hoisting:** Yes, but with Temporal Dead Zone (TDZ)  
  Accessing a `let` variable before its declaration causes a ReferenceError.

- **Redeclaration:** Not allowed  
  Declaring the same variable twice in the same block throws an error.

- **Reassignment:** Allowed  
  You can assign a new value to a `let` variable after declaration.

- **Example:**

  ```javascript
  {
    // console.log(y); // ReferenceError: Cannot access 'y' before initialization
    let y = 10;
    console.log(y); // 10

    // let y = 20; // SyntaxError: Identifier 'y' has already been declared

    y = 30; // reassignment allowed
    console.log(y); // 30
  }

  // console.log(y); // ReferenceError: y is not defined
  ```

### const

- **Scope:** Block-scoped  
  Variables exist only within the nearest enclosing `{}` block (loops, if blocks, functions).

- **Hoisting:** Yes, but with Temporal Dead Zone (TDZ)  
  Accessing a `const` variable before its declaration causes a ReferenceError.

- **Redeclaration:** Not allowed  
  Declaring the same variable twice in the same block throws an error.

- **Assignment:** Must be initialized at declaration and **cannot be reassigned** later.

- **Mutation:** If the variable points to an object or array, its contents can be changed, but the reference itself cannot be changed.

- **Example:**

  ```javascript
  {
    const z = 5;
    // z = 10; // TypeError: Assignment to constant variable.

    const obj = { name: "Alice" };
    obj.name = "Bob"; // Allowed - mutating object properties
    console.log(obj.name); // "Bob"

    // obj = { name: "Charlie" }; // TypeError: Assignment to constant variable.
  }

  // console.log(z); // ReferenceError: z is not defined
  ```

### Temporal Dead Zone (TDZ) Table

| Declaration | Hoisted? | Initialized at Hoisting?         | Access Before Declaration Behavior    |
| ----------- | -------- | -------------------------------- | ------------------------------------- |
| `var`       | Yes      | Yes (initialized as `undefined`) | Returns `undefined`                   |
| `let`       | Yes      | No                               | Throws `ReferenceError` (TDZ applies) |
| `const`     | Yes      | No                               | Throws `ReferenceError` (TDZ applies) |

## 2. Scope & Closures

- Scope defines variable accessibility: global, function, block.
- Closures: functions retain access to their creation scope, enabling data privacy.

## 3. Hoisting

- Declarations are moved to the top of their scope.
- `var` and function declarations hoisted and initialized as undefined.
- `let` and `const` hoisted but inaccessible before declaration (TDZ).

## 4. Modern Syntax & Features (ES6+)

### Arrow Functions

- Provide a concise syntax for writing functions.
- Use `=>` notation.
- Do **not** have their own `this` context; they inherit `this` from the surrounding scope (lexical `this`).
- Useful for writing short functions, especially callbacks.

**Example:**

```javascript
const add = (a, b) => a + b;
```

---

### Template Literals

- Allow embedding expressions inside string literals.
- Use backticks `` ` `` instead of quotes.
- Support multiline strings without special characters.
- Variables or expressions can be inserted using `${...}` syntax.

**Example:**

```javascript
const name = "Smita";
const greeting = `Hello, ${name}!
Welcome to ES6 features.`;
```

---

### Destructuring

- Allows unpacking values from arrays or properties from objects into distinct variables.
- Makes code cleaner and more readable.
- Can set default values while destructuring.

**Example with arrays:**

```javascript
const [first, second] = [10, 20];
```

**Example with objects:**

```javascript
const { name, age } = { name: "Smita", age: 25 };
```

---

### Spread & Rest Operators (`...`)

- **Spread operator:** expands elements of an iterable (like array) into individual elements.
- **Rest operator:** collects multiple elements into an array.

**Spread example:**

```javascript
const arr1 = [1, 2];
const arr2 = [...arr1, 3, 4]; // [1, 2, 3, 4]
```

**Rest example:**

```javascript
function sum(...numbers) {
  return numbers.reduce((a, b) => a + b, 0);
}
```

---

### Default Parameters

- Allow setting default values for function parameters.
- If no argument is passed or `undefined` is passed, the default value is used.

**Example:**

```javascript
function greet(name = "Guest") {
  console.log(`Hello, ${name}!`);
}
```

---

### Modules (`import` / `export`)

- Help organize code into reusable files (modules).
- `export` keyword makes variables, functions, or classes available to other modules.
- `import` keyword is used to bring exported parts from another module.

**Example:**

**math.js**

```javascript
export function add(a, b) {
  return a + b;
}
```

**app.js**

```javascript
import { add } from "./math.js";
console.log(add(2, 3)); // 5
```

## 5. Asynchronous Programming

### Callbacks

- The basic pattern to handle asynchronous operations.
- A function is passed as an argument and called once the async task completes.
- Can lead to "callback hell" if nested deeply, making code hard to read and maintain.

**Example:**

```javascript
function fetchData(callback) {
  setTimeout(() => {
    callback("Data loaded");
  }, 1000);
}

fetchData((data) => {
  console.log(data);
});
```

---

### Promises

- Represent the future completion (or failure) of an asynchronous operation.
- Can be in one of three states: pending, fulfilled, or rejected.
- Provide `.then()` and `.catch()` methods to handle success and errors.
- Help avoid deeply nested callbacks.

**Example:**

```javascript
const promise = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve("Promise resolved");
  }, 1000);
});

promise
  .then((result) => {
    console.log(result);
  })
  .catch((error) => {
    console.error(error);
  });
```

---

### Async/Await

- Syntactic sugar built on top of promises.
- Allows writing asynchronous code that looks synchronous, improving readability.
- Use `async` keyword before function and `await` before promise calls.
- Automatically handles promise resolution and errors can be caught with `try/catch`.

**Example:**

```javascript
async function fetchData() {
  try {
    const result = await new Promise((resolve) =>
      setTimeout(() => resolve("Async/Await result"), 1000)
    );
    console.log(result);
  } catch (error) {
    console.error(error);
  }
}

fetchData();
```

---

### Fetch API / Axios

- Modern methods to perform HTTP requests in JavaScript.
- **Fetch API:** built-in browser API returning promises.
- **Axios:** popular third-party library that supports older browsers and provides additional features like request cancellation and automatic JSON transformation.

**Fetch API example:**

```javascript
fetch("https://api.example.com/data")
  .then((response) => response.json())
  .then((data) => console.log(data))
  .catch((error) => console.error("Error:", error));
```

**Axios example:**

```javascript
import axios from "axios";

axios
  .get("https://api.example.com/data")
  .then((response) => console.log(response.data))
  .catch((error) => console.error("Error:", error));
```

## 6. Event Loop & Concurrency

- JS runs single-threaded with event loop managing call stack, microtasks (promises), and macrotasks (timers).
- Ensures non-blocking execution.

## 7. Prototypal Inheritance & Classes

- Objects inherit via prototype chains.
- ES6 Classes: syntactic sugar over prototypes for OOP patterns.

## 8. Functional Programming Concepts

- Higher-order functions: take/return functions (`map`, `filter`, `reduce`).
- Immutability and pure functions to avoid side effects.

## 9. Error Handling

- `try...catch` blocks.
- Throwing and catching exceptions.

## 10. DOM Manipulation & Events

### 1. Dynamically accessing/updating HTML elements

The DOM (Document Object Model) represents the webpage structure as objects accessible via JavaScript.

- Use methods like `document.getElementById()`, `document.querySelector()`, or `document.getElementsByClassName()` to select elements dynamically.
- Update content, styles, or attributes using properties like `.innerHTML`, `.textContent`, `.style`, or methods like `.appendChild()`, `.removeChild()`.

**Example:**

````js
const heading = document.getElementById('title');
heading.textContent = 'New Title';
## 2. Event propagation: capturing and bubbling

Events propagate through the DOM in three phases:

- **Capturing phase (top-down):** The event travels from the root (`document`) down to the target element.
- **Target phase:** The event reaches the target element.
- **Bubbling phase (bottom-up):** The event bubbles up from the target element back up to the root.

By default, event listeners listen during the **bubbling phase**. You can also listen during **capturing** by passing `true` as the third argument in `addEventListener`.

---

## 3. Event delegation

Event delegation is a technique to handle events efficiently by taking advantage of event bubbling.

- Instead of attaching event listeners to multiple child elements, attach one listener to a common parent.
- Inside the listener, check the event target to identify which child was interacted with.

**Benefits:**

- Improves performance by reducing the number of event listeners.
- Automatically works for dynamically added elements.

**Example:**

```js
document.getElementById('parent').addEventListener('click', function(event) {
  if (event.target && event.target.matches('button.classname')) {
    console.log('Button inside parent clicked!');
  }
});

````

## 11. Memory Management & Garbage Collection

- Automatic freeing of unused memory.
- Closures can retain references affecting memory.

## 12. Debouncing and Throttling

- Techniques to limit function execution frequency:
  - Debounce delays until events stop.
  - Throttle limits calls to fixed intervals.

## 13. Call, Apply, and Bind

- Control `this` context in function execution:
  - `call` and `apply`: invoke immediately.
  - `bind`: returns new function with bound context.

## 14. JSON (JavaScript Object Notation)

- Lightweight format to serialize/transfer data.

## 15. Equality Operators (== vs ===)

- `==`: compares with type coercion.
- `===`: strict equality, compares type and value.

## 16. Template Literals

- Use backticks for strings with embedded expressions and multiline support.

## 17. Null vs Undefined

- `undefined`: declared but uninitialized.
- `null`: intentional absence of value.

## 18. Modules & Tooling

- ES6 modules for better code structure.
- Bundlers (Webpack, Rollup), transpilers (Babel) for compatibility and optimization.

## 19. New & Trending APIs

- Web Workers: background threads.
- Service Workers: offline support and caching.
- WebSockets: real-time communication.
- Intl API: internationalization support.

## 20. Type Safety Enhancements

- TypeScript: static typing on top of JavaScript for robust code.

## 21. # Types of Errors in Programming

## 1. Syntax Errors

- Occur when the code violates the language's grammar rules.
- Prevent the program from running.
- Example: Missing a semicolon, unmatched parentheses, or incorrect keywords.

## 2. Runtime Errors

- Occur while the program is running.
- Cause the program to crash or behave unexpectedly.
- Examples: Division by zero, accessing a null reference, out-of-bound array index.

## 3. Logical Errors

- Code runs without crashing but produces incorrect results.
- Caused by mistakes in the algorithm or logic.
- Example: Using `>` instead of `<` in a condition.

## 4. Compilation Errors

- Errors detected by the compiler during the compilation phase.
- Include syntax errors and type-checking errors.
- Prevent successful compilation of code.

## 5. Semantic Errors

- Code is syntactically correct but does not do what the programmer intended.
- Often leads to logical errors.
- Example: Misusing a function that behaves differently than expected.

## 6. Linker Errors

- Occur during the linking phase of compiled programs.
- Caused by missing references or multiple definitions.
- Example: Calling a function without providing its definition.

## 7. Type Errors

- Occur when operations are applied to incompatible data types.
- Often caught during compilation or runtime (in dynamically typed languages).
- Example: Adding a number to a string without explicit conversion.

## 8. Memory Errors

- Related to incorrect handling of memory allocation/deallocation.
- Examples: Memory leaks, buffer overflows, dangling pointers.

## 9. I/O Errors

- Occur during input/output operations.
- Examples: File not found, permission denied, network connection lost.

## 10. Exception Errors

- Errors represented as exceptions that can be caught and handled.
- Examples: NullPointerException, IndexOutOfBoundsException, IOError.

---

_Note:_ Understanding these error types helps in debugging and writing more robust code.

**Summary:**
This optimized list covers all essential JavaScript concepts, from core syntax and asynchronous programming to modern APIs and tooling — all crucial for interviews and modern development.

---

_Use this streamlined guide to focus your learning and interview prep effectively._

````

```

```

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

- Arrow Functions: concise syntax, lexical `this`.
- Template Literals: string interpolation and multiline strings.
- Destructuring: unpack arrays/objects.
- Spread & Rest Operators (`...`): expand or collect elements.
- Default Parameters.
- Modules: `import`/`export` for code organization.

## 5. Asynchronous Programming

- Callbacks: basic async pattern.
- Promises: represent future result or failure of async operations.
- Async/Await: syntactic sugar over promises for cleaner code.
- Fetch API/Axios: modern HTTP requests.

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

- Dynamically accessing/updating HTML elements.
- Event propagation: capturing (top-down) and bubbling (bottom-up).
- Event delegation to efficiently handle events.

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

```

```

# 📝 JavaScript Rules & Best Practices

## 1. Variables & Declarations

- Use `let` and `const` instead of `var`.
- `const` → value cannot be reassigned.
- `let` → value can be reassigned.
- `var` → function-scoped, avoid in modern JS.

## 2. Semicolons

- Optional in most cases, but **recommended** to avoid automatic semicolon insertion bugs.

## 3. Case Sensitivity

- JS is **case-sensitive**.

  ```javascript
  let Name = "Smita"; // different from name
  ```

## 4. Data Types

- **Primitive types:** `string`, `number`, `boolean`, `null`, `undefined`, `symbol`, `bigint`.
- **Reference types:** `object`, `array`, `function`.
- JS can **dynamically render types at runtime**.

## 5. Variables as Storage

- Variables act as **containers to store data**.
- Each variable has a **memory location** where the data is stored.

## 6. Syntax

- **Rules to write programs** are called **syntax**.

## 7. Functions

- Can be declared as:

  - **Function Declaration**

    ```javascript
    function greet() {}
    ```

  - **Function Expression**

    ```javascript
    const greet = function () {};
    ```

  - **Arrow Function**

    ```javascript
    const greet = () => {};
    ```

- Arrow functions **do not have their own `this`**.

## 8. Objects & Arrays

- Use `{}` for objects, `[]` for arrays.
- Access arrays with index, objects with keys.

  ```javascript
  const arr = [1, 2, 3];
  const obj = { name: "Smita" };
  console.log(arr[0]);
  console.log(obj.name);
  ```

## 9. Equality Operators

- `==` → compares values (type coercion occurs).
- `===` → compares value **and type** (recommended).

## 10. Comments

- Single-line: `// comment`
- Multi-line: `/* comment */`

## 11. Strict Mode

- Use `"use strict";` at the top to enforce stricter parsing and error handling.

## 12. Naming Conventions

- Use camelCase for variables and functions.
- PascalCase for classes.
- UPPERCASE for constants.

## 13. Scope Rules

- `var` → function scope.
- `let` & `const` → block scope.

## 14. Hoisting

- Variable and function declarations are **hoisted**.
- Only function declarations and `var` are hoisted; `let` & `const` are not accessible before declaration.

## 15. Avoid Global Variables

- Minimize use of global variables to prevent collisions and bugs.

## 16. Error Handling

- Use `try { } catch(e) { }` to handle runtime errors gracefully.

## 17. Best Practices

- Always declare variables.
- Use strict equality (`===`).
- Keep functions small and single-purpose.
- Use meaningful names.
- Comment your code for clarity.

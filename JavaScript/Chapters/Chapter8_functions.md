# 📝 JavaScript Functions

Functions in JavaScript are **blocks of reusable code** designed to perform a specific task. They make code modular, maintainable, and easier to debug.

## Syntax

```javascript
function functionName(parameters) {
  // code to execute
  return value; // optional
}
```

- **functionName**: The name of the function (used to call it).
- **parameters**: Values passed to the function.
- **return**: Sends a value back to the caller.

## 1. Function Declaration

```javascript
function greet(name) {
  return `Hello, ${name}!`;
}
console.log(greet("Smita")); // Output: Hello, Smita!
```

✅ **Hoisted** – can be called before it is defined.

## 2. Function Expression

```javascript
const greet = function (name) {
  return `Hello, ${name}!`;
};
console.log(greet("Smita"));
```

❌ **Not hoisted** – cannot be called before it is defined.

## 3. Arrow Function (ES6)

```javascript
const greet = (name) => `Hello, ${name}!`;
console.log(greet("Smita"));
```

✅ Shorter syntax.
❌ Does **not** have its own `this`, `arguments`, or `super`.

## 4. Anonymous Function

A function without a name, often used as callbacks.

```javascript
setTimeout(function () {
  console.log("This runs after 2 seconds");
}, 2000);
```

## 5. Immediately Invoked Function Expression (IIFE)

Executes immediately after creation.

```javascript
(function () {
  console.log("I run immediately!");
})();
```

✅ Used to avoid polluting the global scope.

## 6. Higher-Order Function

Functions that **take other functions as arguments** or **return functions**.

```javascript
function operate(a, b, fn) {
  return fn(a, b);
}

function add(x, y) {
  return x + y;
}

console.log(operate(5, 3, add)); // Output: 8
```

## 7. Callback Function

A function passed as an argument and executed later.

```javascript
function greetUser(name, callback) {
  console.log("Hi, " + name);
  callback();
}

function sayBye() {
  console.log("Goodbye!");
}

greetUser("Smita", sayBye);
```

## 8. Constructor Function

Used to create multiple similar objects.

```javascript
function Person(name, age) {
  this.name = name;
  this.age = age;
}

const user1 = new Person("Smita", 22);
console.log(user1.name); // Smita
```

✅ Used with `new` keyword.

## 9. Recursive Function

A function that calls itself until a condition is met.

```javascript
function factorial(n) {
  if (n === 1) return 1;
  return n * factorial(n - 1);
}
console.log(factorial(5)); // Output: 120
```

## 10. Default Parameters

You can assign default values to parameters.

```javascript
function greet(name = "Guest") {
  console.log(`Hello, ${name}`);
}
greet(); // Output: Hello, Guest
```

## 11. Rest Parameters

Combine all arguments into an array.

```javascript
function sum(...nums) {
  return nums.reduce((a, b) => a + b, 0);
}
console.log(sum(1, 2, 3, 4)); // Output: 10
```

## 12. Function with Return Value

```javascript
function add(a, b) {
  return a + b;
}
let result = add(5, 3);
console.log(result); // 8
```

## 13. Pure Function

A function that has **no side effects** and returns the same output for the same input.

```javascript
function add(a, b) {
  return a + b;
}
```

## 14. Impure Function

A function that depends on external data or causes side effects.

```javascript
let total = 0;
function addToTotal(num) {
  total += num;
}
addToTotal(5);
console.log(total); // 5
```

## 15. Generator Function (ES6)

Returns an iterator object and can pause/resume execution.

```javascript
function* generateNumbers() {
  yield 1;
  yield 2;
  yield 3;
}

const gen = generateNumbers();
console.log(gen.next().value); // 1
console.log(gen.next().value); // 2
```

## Summary

| Type                 | Hoisted | `this` Binding  | Use Case                 |
| -------------------- | ------- | --------------- | ------------------------ |
| Function Declaration | ✅ Yes  | Own `this`      | Reusable named functions |
| Function Expression  | ❌ No   | Own `this`      | Assign to variables      |
| Arrow Function       | ❌ No   | Inherits `this` | Short syntax, callbacks  |
| IIFE                 | ❌ No   | Own `this`      | Run immediately          |
| Constructor          | ✅ Yes  | Own `this`      | Object creation          |

**Functions are the backbone of JavaScript programming** — they enable modular, reusable, and organized code.

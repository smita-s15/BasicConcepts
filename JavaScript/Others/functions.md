# 🧠 JavaScript Function Types & Invocation Styles

JavaScript provides multiple ways to define and invoke functions — each suited for specific use cases. Below is a complete overview with examples.

---

## 1. IIFE (Immediately Invoked Function Expression)

Executes immediately after being defined.

```js
(function () {
  console.log("IIFE executed immediately");
})();

(() => console.log("Arrow IIFE executed immediately"))();
```

✅ Use case: Private scope, initialization code, avoiding global variable pollution.

---

## 2. Named Function Declaration

A traditional way to define reusable functions.

```js
function greet() {
  console.log("Hello");
}
greet();
```

✅ Key point: Function declarations are hoisted, so you can call them before their definition.

---

## 3. Function Expression

A function assigned to a variable.

```js
const sayHi = function () {
  console.log("Hi");
};
sayHi();
```

✅ Use case: Useful for callbacks, closures, and controlling function availability.

---

## 4. Arrow Function

Shorter syntax introduced in ES6; does not have its own `this`, `arguments`, or `prototype`.

```js
const add = (a, b) => a + b;
console.log(add(2, 3)); // 5
```

✅ Use case: Compact callbacks, inline logic, functional patterns.

---

## 5. Anonymous Function

A function without a name — often used inline as callbacks.

```js
setTimeout(function () {
  console.log("Anonymous function executed");
}, 1000);
```

✅ Use case: One-time logic inside event handlers or timers.

---

## 6. Callback Function

A function passed as an argument to another function and executed later.

```js
function processUserInput(callback) {
  callback("Smita");
}
processUserInput((name) => console.log("Hello " + name));
```

✅ Use case: Asynchronous operations, event handling, or sequencing logic.

---

## 7. Constructor Function

Used with the `new` keyword to create objects.

```js
function Person(name) {
  this.name = name;
}
const p = new Person("Smita");
console.log(p.name); // Smita
```

✅ Use case: Object-oriented programming before ES6 `class`.

---

## 8. Generator Function

A special function that can pause and resume execution using `yield`.

```js
function* numbers() {
  yield 1;
  yield 2;
  yield 3;
}
const gen = numbers();
console.log(gen.next().value); // 1
console.log(gen.next().value); // 2
console.log(gen.next().value); // 3
```

✅ Use case: Controlled iteration, async flow, or lazy data sequences.

---

## 9. Async Function

Used for asynchronous (Promise-based) code that uses `await`.

```js
async function fetchData() {
  const response = await fetch("https://api.example.com/data");
  const data = await response.json();
  console.log(data);
}
fetchData();
```

✅ Use case: Cleaner async code without nested `.then()` chains.

---

## 10. Recursive Function

A function that calls itself until a base condition is met.

```js
function countDown(n) {
  if (n === 0) return;
  console.log(n);
  countDown(n - 1);
}
countDown(5);
```

✅ Use case: Tasks that can be broken down into similar subtasks, like traversing trees or factorial calculation.

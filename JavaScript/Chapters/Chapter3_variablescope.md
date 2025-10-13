# 📝 JavaScript Variables: `var`, `let`, `const` & Scope

## 1. `var`

- **Scope:** Function-scoped.
- **Hoisting:** Yes, initialized as `undefined`.
- **Re-declaration & Update:** Allowed.
- **Use:** Legacy code; avoid in modern JS.

```javascript
var x = 10;
var x = 20; // Re-declaration allowed
function testVar() {
  var y = 5;
  console.log(y);
}
```

## 2. `let`

- **Scope:** Block-scoped `{ }`.
- **Hoisting:** Yes, but **uninitialized** (Temporal Dead Zone).
- **Re-declaration:** Not allowed in same block; **Update allowed**.
- **Use:** For variables that change.

```javascript
let a = 10;
a = 20; // Update allowed
// let a = 30; // Error: Re-declaration in same block
```

## 3. `const`

- **Scope:** Block-scoped.
- **Hoisting:** Yes, uninitialized (TDZ).
- **Re-declaration & Update:** Not allowed.
- **Use:** Constants; immutable references.
- **Note:** Object/array contents **can be mutated**.

```javascript
const PI = 3.14;
// PI = 3.1415; // Error

const obj = { name: "Smita" };
obj.name = "Shinde"; // Allowed
// obj = {}; // Error
```

## Quick Comparison

| Keyword | Scope    | Hoisting  | Re-declare | Update | Use Case              |
| ------- | -------- | --------- | ---------- | ------ | --------------------- |
| var     | Function | Yes       | Yes        | Yes    | Legacy code           |
| let     | Block    | Yes (TDZ) | No         | Yes    | Mutable variables     |
| const   | Block    | Yes (TDZ) | No         | No     | Constants / immutable |

## Scope Types

### Global Scope

- Declared outside functions/blocks.
- Accessible anywhere.

```javascript
var globalVar = "I am global";
console.log(globalVar);
```

### Function Scope

- `var` inside a function is accessible **only inside the function**.

```javascript
function myFunc() {
  var funcVar = "Inside function";
  console.log(funcVar);
}
// console.log(funcVar); // Error
```

### Block Scope

- `let`/`const` are block-scoped `{ }`.

```javascript
if (true) {
  let blockVar = "Inside block";
  const constVar = 100;
  console.log(blockVar, constVar);
}
// console.log(blockVar); // Error
// console.log(constVar); // Error
```

### Hoisting Behavior

- `var`: hoisted, initialized as `undefined`.
- `let`/`const`: hoisted, uninitialized (TDZ).

```javascript
console.log(a); // undefined
var a = 10;

// console.log(b); // Error
let b = 20;
```

# 📝 JavaScript `for…of` Loop

The `for…of` loop is used to iterate over **iterable objects** such as arrays, strings, maps, sets, and more. It provides access to the **values** directly.

## Syntax

```javascript
for (variable of iterable) {
  // code block to execute
}
```

- **variable**: A variable that holds the value of the current element in the iteration.
- **iterable**: An iterable object such as an array, string, map, or set.

## Key Points

- Iterates over **values**, not keys.
- Works only with **iterable objects** (arrays, strings, maps, sets, etc.).
- Does **not** work directly on plain objects.
- Does not include inherited properties or non-enumerable properties.

## Examples

### Iterating Over an Array

```javascript
const numbers = [10, 20, 30];

for (const num of numbers) {
  console.log(num); // Outputs: 10, 20, 30
}
```

### Iterating Over a String

```javascript
const str = "Hello";

for (const char of str) {
  console.log(char); // Outputs: H, e, l, l, o
}
```

### Iterating Over a Set

```javascript
const mySet = new Set([1, 2, 3]);

for (const value of mySet) {
  console.log(value); // Outputs: 1, 2, 3
}
```

### Iterating Over a Map

```javascript
const myMap = new Map([
  ["a", 1],
  ["b", 2],
]);

for (const [key, value] of myMap) {
  console.log(key, value); // Outputs: a 1, b 2
}
```

## Summary

- Use `for…of` to iterate **values** of iterable objects.
- Prefer `for…of` over `for…in` for arrays and other iterables.
- Cannot be used directly on plain objects; for objects use `Object.keys()`, `Object.values()`, or `Object.entries()` with `for…of`.

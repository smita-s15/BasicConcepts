# 📝 JavaScript Arrays

An **array** in JavaScript is a special type of object used to store multiple values in a single variable. Arrays can hold any data type — numbers, strings, objects, or even other arrays.

---

## 🧩 Declaration

```javascript
let fruits = ["apple", "banana", "mango"];
let numbers = new Array(1, 2, 3, 4);
```

---

## 📘 Accessing Elements

```javascript
let fruits = ["apple", "banana", "mango"];
console.log(fruits[0]); // 'apple'
console.log(fruits[2]); // 'mango'
```

Index starts from **0**.

---

## ⚙️ Common Array Methods

### 🔹 Adding and Removing Elements

```javascript
let arr = [1, 2, 3];
arr.push(4); // [1, 2, 3, 4]
arr.pop(); // [1, 2, 3]
arr.unshift(0); // [0, 1, 2, 3]
arr.shift(); // [1, 2, 3]
```

### 🔹 Finding Elements

```javascript
let colors = ["red", "blue", "green"];
colors.indexOf("blue"); // 1
colors.includes("green"); // true
```

### 🔹 Iterating Over Arrays

```javascript
let fruits = ["apple", "banana", "mango"];

// Using for loop
for (let i = 0; i < fruits.length; i++) {
  console.log(fruits[i]);
}

// Using for...of
for (let fruit of fruits) {
  console.log(fruit);
}

// Using forEach
fruits.forEach((fruit, index) => console.log(index, fruit));
```

### 🔹 Transforming Arrays

```javascript
let numbers = [1, 2, 3, 4];

let doubled = numbers.map((num) => num * 2); // [2, 4, 6, 8]
let even = numbers.filter((num) => num % 2 === 0); // [2, 4]
let sum = numbers.reduce((acc, num) => acc + num, 0); // 10
```

### 🔹 Sorting and Reversing

```javascript
let nums = [3, 1, 4, 2];
nums.sort(); // [1, 2, 3, 4]
nums.reverse(); // [4, 3, 2, 1]
```

For numeric sorting with custom order:

```javascript
nums.sort((a, b) => a - b); // Ascending
nums.sort((a, b) => b - a); // Descending
```

### 🔹 Combining and Slicing

```javascript
let a = [1, 2];
let b = [3, 4];
let c = a.concat(b); // [1, 2, 3, 4]

let fruits = ["apple", "banana", "mango", "orange"];
fruits.slice(1, 3); // ['banana', 'mango']
```

### 🔹 Splice Method (Add/Remove from specific index)

```javascript
let fruits = ["apple", "banana", "mango"];
fruits.splice(1, 1, "grape"); // remove 1 element at index 1, add 'grape'
console.log(fruits); // ['apple', 'grape', 'mango']
```

### 🔹 Flattening Arrays

```javascript
let nested = [1, [2, [3, [4]]]];
nested.flat(2); // [1, 2, 3, [4]]
nested.flat(Infinity); // [1, 2, 3, 4]
```

### 🔹 Checking if Variable is an Array

```javascript
Array.isArray([1, 2, 3]); // true
Array.isArray("Hello"); // false
```

---

## 🧠 Important Notes

- Arrays are **mutable** — their contents can be changed.
- They are **zero-indexed**.
- Array methods often return **new arrays** (e.g., `map`, `filter`), while others modify the original (e.g., `push`, `pop`, `splice`).
- Use **`const`** for arrays unless you plan to reassign the variable.

---

## 📚 Summary

- Arrays hold multiple values in a single variable.
- Common operations include adding, removing, transforming, and iterating.
- Modern methods like `map`, `filter`, and `reduce` make array manipulation powerful and concise.

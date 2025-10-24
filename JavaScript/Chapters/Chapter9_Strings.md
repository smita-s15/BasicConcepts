# 📝 JavaScript Strings

A **string** in JavaScript is a sequence of characters used to represent text. Strings are **immutable**, meaning their content cannot be changed once created.

---

## 🧩 Declaration

Strings can be created using:

```javascript
let str1 = "Hello"; // Double quotes
let str2 = "World"; // Single quotes
let str3 = `Hello, ${str2}`; // Template literals (ES6)
```

---

## 📘 String Properties

| Property | Description                                    | Example               |
| -------- | ---------------------------------------------- | --------------------- |
| `length` | Returns the number of characters in the string | `'Hello'.length // 5` |

---

## ⚙️ Common String Methods

### 🔹 Character Access

```javascript
let str = "Hello";
console.log(str[0]); // 'H'
console.log(str.charAt(1)); // 'e'
```

### 🔹 Case Conversion

```javascript
str.toUpperCase(); // 'HELLO'
str.toLowerCase(); // 'hello'
```

### 🔹 Searching

```javascript
str.indexOf("l"); // 2
str.lastIndexOf("l"); // 3
str.includes("He"); // true
str.startsWith("He"); // true
str.endsWith("lo"); // true
```

### 🔹 Extracting Parts

```javascript
let text = "JavaScript";
text.slice(0, 4); // 'Java'
text.substring(4, 10); // 'Script'
text.substr(4, 6); // 'Script' (deprecated)
```

### 🔹 Replacing Text

```javascript
let sentence = "I like JavaScript";
sentence.replace("like", "love"); // 'I love JavaScript'
```

Use a **regular expression** with the `g` flag to replace all occurrences:

```javascript
"I like apples and apples".replace(/apples/g, "mangoes");
// 'I like mangoes and mangoes'
```

### 🔹 Trimming Spaces

```javascript
let name = "  Smita  ";
name.trim(); // 'Smita'
name.trimStart(); // 'Smita  '
name.trimEnd(); // '  Smita'
```

### 🔹 Splitting and Joining

```javascript
let fruits = "apple,banana,mango";
let arr = fruits.split(","); // ['apple', 'banana', 'mango']
arr.join(" | "); // 'apple | banana | mango'
```

### 🔹 Repeating

```javascript
"Hi ".repeat(3); // 'Hi Hi Hi '
```

### 🔹 Template Literals (ES6)

Template literals use backticks (`` ` ``) and allow embedding expressions.

```javascript
let name = "Smita";
let greeting = `Hello, ${name}!`;
console.log(greeting); // 'Hello, Smita!'
```

---

## 🧠 Important Notes

- Strings are **immutable** — methods return new strings, they don’t modify the original.
- Use **template literals** for multiline and dynamic strings.
- Always prefer `includes()` over `indexOf()` for readability.

---

## 📚 Summary

- **Create strings** using single, double, or backticks.
- **Access characters** using index or `charAt()`.
- **Use built-in methods** for searching, slicing, and formatting.
- **Template literals** make string handling easier and cleaner.

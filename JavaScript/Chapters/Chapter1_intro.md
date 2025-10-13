# 🌐 JavaScript Introduction Notes

## 🧠 What is JavaScript?

- **JavaScript (JS)** is a **high-level, interpreted, and dynamic programming language**.
- It is used to make **web pages interactive, dynamic, and responsive**.
- It runs in the **browser** and can also run **outside the browser** using environments like **Node.js**.

---

## 📜 History

- **Created by:** _Brendan Eich_ in **1995** at _Netscape_.
- **Original name:** Mocha → LiveScript → JavaScript.
- **Standardized by:** _ECMA International_ under the name **ECMAScript (ES)**.
- Latest versions: **ES6 (2015)** and onwards (ES7, ES8…).

---

## ⚙️ Features of JavaScript

- **Lightweight & Interpreted:** Runs line by line (no compilation needed).
- **Dynamic Typing:** No need to specify variable types.
- **Prototype-based OOP:** Uses prototypes instead of classical classes (though `class` syntax exists).
- **Event-driven:** Reacts to user actions like clicks, keypresses, etc.
- **Functional:** Functions are first-class citizens.
- **Platform Independent:** Runs anywhere with a JS engine.

---

## 🧩 Where JavaScript Runs

1. **Inside Browser:**

   - JS runs using the browser’s **JS Engine** (like V8, SpiderMonkey, Chakra).
   - You can test it using **browser console** (`console.log("Hello JS")`).
   - Used for **frontend development**.

2. **Outside Browser:**

   - **Node.js** (built on the **V8 engine**, by _Ryan Dahl_).
   - Used for **backend development** and **server-side scripting**.

---

## 💻 How to Add JavaScript to HTML

### Inline Script

```html
<button onclick="alert('Hello JS!')">Click Me</button>
```

### Internal Script

```html
<script>
  console.log("Hello from internal JS");
</script>
```

### External Script

```html
<script src="script.js"></script>
```

---

## 🧮 Basic Syntax Example

```javascript
// Printing to console
console.log("Welcome to JavaScript!");

// Variables
let name = "Smita";
const age = 22;
var city = "Satara";

// Function
function greet(user) {
  return "Hello " + user + "!";
}

console.log(greet(name));
```

---

## ⚡ JavaScript Engine

JavaScript is executed by engines inside browsers:

- **Chrome:** V8
- **Firefox:** SpiderMonkey
- **Safari:** JavaScriptCore
- **Edge:** Chakra

**Note:** V8 (written in C++) compiles JS into **machine code** for fast performance.

---

## 🔁 Role of JavaScript in Web Development

| Layer     | Language   | Purpose            |
| --------- | ---------- | ------------------ |
| Structure | HTML       | Defines content    |
| Style     | CSS        | Defines design     |
| Behavior  | JavaScript | Adds interactivity |

---

## 🚀 Applications of JavaScript

- Web and Mobile App Development
- Backend (Node.js, Express.js)
- Game Development
- Machine Learning (TensorFlow.js)
- Internet of Things (IoT)
- Browser Extensions and Desktop Apps (Electron.js)

---

## ✅ Summary

- **JavaScript = ECMAScript + Browser APIs**
- **Liberal language** → runs even with minor syntax issues
- Can run **inside or outside browsers**
- **Core + DOM + BOM** make JS powerful for web development

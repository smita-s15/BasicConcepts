# 🔁 JavaScript `for` Loop

## 🧠 Definition

The **`for` loop** in JavaScript is used to execute a block of code repeatedly for a specified number of times.  
It continues to run as long as a given condition evaluates to `true`.

---

## 🧩 Syntax

```javascript
for (initialization; condition; update) {
  // code to execute each iteration
}
```

---

## 🧱 Explanation

| Part               | Description                                                                            |
| ------------------ | -------------------------------------------------------------------------------------- |
| **Initialization** | Runs once before the loop starts. Used to declare and initialize the counter variable. |
| **Condition**      | The loop runs while this condition is `true`. Once it becomes `false`, the loop stops. |
| **Update**         | Executed after every iteration. Usually increments or decrements the counter variable. |
| **Code Block**     | The set of statements inside `{}` that executes each time the loop runs.               |

---

## 💡 Example 1: Counting from 1 to 5

```javascript
for (let i = 1; i <= 5; i++) {
  console.log(i);
}
```

**Output:**

```
1
2
3
4
5
```

---

## 💡 Example 2: Iterating Over an Array

```javascript
const fruits = ["apple", "banana", "mango"];

for (let i = 0; i < fruits.length; i++) {
  console.log(fruits[i]);
}
```

**Output:**

```
apple
banana
mango
```

---

## ⚠️ Notes

- You can omit **any part** of the `for` statement:
  ```javascript
  let i = 0;
  for (; i < 3; ) {
    console.log(i);
    i++;
  }
  ```
- Use `break` to stop the loop early.
- Use `continue` to skip to the next iteration.

---

## ✅ Summary

- Use `for` loops when you **know how many times** you want to run the code.
- Ideal for **iterating arrays**, **counting**, or **executing fixed repetitions**.

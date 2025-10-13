# 📝 JavaScript: Primitive Data Types and Variable Scope

## 1. Primitive Data Types

JavaScript has **7 primitive data types**:

1. **String** - Represents text.

```javascript
let name = "Smita";
```

2. **Number** - Represents numeric values.

```javascript
let age = 22;
```

3. **Boolean** - Represents `true` or `false`.

```javascript
let isActive = true;
```

4. **Null** - Represents intentional absence of any value.

```javascript
let value = null;
```

5. **Undefined** - Represents a variable that has been declared but not assigned.

```javascript
let data;
console.log(data); // undefined
```

6. **Symbol** - Represents a unique and immutable value.

```javascript
let sym = Symbol("id");
```

7. **BigInt** - Represents large integers beyond Number limits.

```javascript
let bigNumber = 123456789012345678901234567890n;
```

### Key Points

- **Immutable:** Primitive values cannot be altered; operations create a new value.
- **Assignment:** Copied by value; changing one variable does not affect another.

### Example

```javascript
let a = 10;
let b = a;
b = 20;
console.log(a); // 10, a is unchanged
```

---

## 2. Primitive vs Reference Types

| Type      | Assignment   | Effect on Original | Example                 |
| --------- | ------------ | ------------------ | ----------------------- |
| Primitive | By value     | No effect          | string, number, boolean |
| Reference | By reference | Affects original   | object, array, function |

### Reference Example

```javascript
let obj1 = { name: "Smita" };
let obj2 = obj1;
obj2.name = "Shinde";
console.log(obj1.name); // Shinde
```

---

## 3. Variable Scope in JS

### Global Scope

- Variables declared **outside functions/blocks**.
- Accessible anywhere.

```javascript
var globalVar = "I am global";
console.log(globalVar);
```

### Function Scope

- Variables declared with `var` inside a function.
- Not accessible outside the function.

```javascript
function myFunc() {
  var funcVar = "Inside function";
  console.log(funcVar);
}
```

### Block Scope

- Variables declared with `let` or `const` inside `{ }`.
- Not accessible outside the block.

```javascript
if (true) {
  let blockVar = 10;
  const constVar = 20;
}
// console.log(blockVar); // Error
```

### Hoisting & Scope

- `var` is hoisted and initialized with `undefined`.
- `let` and `const` are hoisted but not initialized (TDZ).

```javascript
console.log(a); // undefined
var a = 10;
// console.log(b); // Error
let b = 20;
```

### Scope Summary Table

| Variable | Scope           | Hoisting Behavior                 | Accessibility               |
| -------- | --------------- | --------------------------------- | --------------------------- |
| var      | Function/Global | Hoisted, initialized as undefined | Inside function or globally |
| let      | Block           | Hoisted, uninitialized (TDZ)      | Inside block only           |
| const    | Block           | Hoisted, uninitialized (TDZ)      | Inside block                |

# 📝 JavaScript: Data Type Operations and Combinations

## 1. Addition (+) Operator

### 1.1 Number + Number

```javascript
console.log(5 + 10); // 15
```

### 1.2 Number + String (Type coercion to String)

```javascript
console.log(5 + "10"); // "510"
```

### 1.3 String + String

```javascript
console.log("Hello" + " World"); // "Hello World"
```

### 1.4 Boolean + Number

- `true` = 1, `false` = 0

```javascript
console.log(true + 5); // 6
console.log(false + 5); // 5
```

### 1.5 Boolean + String

```javascript
console.log(true + "Hello"); // "trueHello"
```

### 1.6 Null + Number

```javascript
console.log(null + 5); // 5 (null treated as 0)
```

### 1.7 Undefined + Number

```javascript
console.log(undefined + 5); // NaN
```

### 1.8 Object + Primitive

```javascript
console.log({ a: 1 } + 5); // "[object Object]5"
```

## 2. Subtraction (-) Operator

```javascript
console.log(10 - 5); // 5
console.log("10" - 5); // 5
console.log(true - 1); // 0
console.log(null - 1); // -1
console.log(undefined - 1); // NaN
```

## 3. Multiplication (\*) Operator

```javascript
console.log(5 * 2); // 10
console.log("5" * 2); // 10
console.log(true * 2); // 2
console.log(null * 2); // 0
console.log(undefined * 2); // NaN
```

## 4. Division (/) Operator

```javascript
console.log(10 / 2); // 5
console.log("10" / 2); // 5
console.log(true / 2); // 0.5
console.log(null / 2); // 0
console.log(undefined / 2); // NaN
```

## 5. Modulus (%) Operator

```javascript
console.log(10 % 3); // 1
console.log("10" % 3); // 1
console.log(true % 2); // 1
console.log(null % 2); // 0
console.log(undefined % 2); // NaN
```

## 6. Exponentiation (\*\*) Operator

```javascript
console.log(2 ** 3); // 8
console.log("2" ** 3); // 8
console.log(true ** 3); // 1
console.log(null ** 2); // 0
console.log(undefined ** 2); // NaN
```

## 7. Special Cases

| Operation     | Result             | Explanation                           |
| ------------- | ------------------ | ------------------------------------- |
| "5" + 5       | "55"               | String concatenation                  |
| 5 + true      | 6                  | true → 1                              |
| 5 + false     | 5                  | false → 0                             |
| 5 - "2"       | 3                  | String converted to number            |
| null + 5      | 5                  | null → 0                              |
| undefined + 5 | NaN                | undefined cannot convert to number    |
| {} + 5        | "[object Object]5" | Object converted to string            |
| [] + 5        | "5"                | Empty array converted to empty string |
| [1] + 5       | "15"               | Array converted to string             |
| [1,2] + 5     | "1,25"             | Array converted to string             |

## 8. Summary

- **Addition (+)** can act as **concatenation** or **arithmetic** depending on operand types.
- **Subtraction (-), Multiplication (\*), Division (/), Modulus (%), Exponentiation (**)\*\* always convert operands to numbers.
- **Type coercion rules:**

  - `true` → 1, `false` → 0, `null` → 0, `undefined` → NaN
  - Objects/arrays → converted to string or primitive via `toString()

# 📝 JavaScript: Full Data Type Operations Reference

## 1. Data Types

- Number
- String
- Boolean
- Null
- Undefined
- Object / Array

## 2. Operators

- `+` (addition / concatenation)
- `-` (subtraction)
- `*` (multiplication)
- `/` (division)
- `%` (modulus)
- `**` (exponentiation)

---

## 3. Number Operations

| Number \ Other | Number | String | Boolean | Null   | Undefined | Object/Array                             |
| -------------- | ------ | ------ | ------- | ------ | --------- | ---------------------------------------- |
| **+**          | number | string | number  | number | NaN       | string "[object Object]" or array string |
| **-**          | number | number | number  | number | NaN       | NaN                                      |
| **\***         | number | number | number  | number | NaN       | NaN                                      |
| **/**          | number | number | number  | number | NaN       | NaN                                      |
| **%**          | number | number | number  | number | NaN       | NaN                                      |
| **\*\***       | number | number | number  | number | NaN       | NaN                                      |

---

## 4. String Operations

| String \ Other | Number | String | Boolean | Null   | Undefined | Object/Array |
| -------------- | ------ | ------ | ------- | ------ | --------- | ------------ |
| **+**          | string | string | string  | string | string    | string       |
| **-**          | number | NaN    | number  | number | NaN       | NaN          |
| **\***         | number | NaN    | number  | number | NaN       | NaN          |
| **/**          | number | NaN    | number  | number | NaN       | NaN          |
| **%**          | number | NaN    | number  | number | NaN       | NaN          |
| **\*\***       | number | NaN    | number  | number | NaN       | NaN          |

---

## 5. Boolean Operations

| Boolean \ Other | Number | String | Boolean | Null   | Undefined | Object/Array |
| --------------- | ------ | ------ | ------- | ------ | --------- | ------------ |
| **+**           | number | string | number  | number | NaN       | string       |
| **-**           | number | number | number  | number | NaN       | NaN          |
| **\***          | number | number | number  | number | NaN       | NaN          |
| **/**           | number | number | number  | number | NaN       | NaN          |
| **%**           | number | number | number  | number | NaN       | NaN          |
| **\*\***        | number | number | number  | number | NaN       | NaN          |

---

## 6. Null Operations

| Null \ Other | Number | String | Boolean | Null | Undefined | Object/Array |
| ------------ | ------ | ------ | ------- | ---- | --------- | ------------ |
| **+**        | number | string | number  | 0    | NaN       | string       |
| **-**        | number | number | number  | 0    | NaN       | NaN          |
| **\***       | number | number | number  | 0    | NaN       | NaN          |
| **/**        | number | number | number  | 0    | NaN       | NaN          |
| **%**        | number | number | number  | 0    | NaN       | NaN          |
| **\*\***     | number | number | number  | 0    | NaN       | NaN          |

---

## 7. Undefined Operations

| Undefined \ Other | Number | String | Boolean | Null | Undefined | Object/Array   |
| ----------------- | ------ | ------ | ------- | ---- | --------- | -------------- |
| **+**             | NaN    | string | NaN     | NaN  | NaN       | string (for +) |
| **-**             | NaN    | NaN    | NaN     | NaN  | NaN       | NaN            |
| **\***            | NaN    | NaN    | NaN     | NaN  | NaN       | NaN            |
| **/**             | NaN    | NaN    | NaN     | NaN  | NaN       | NaN            |
| **%**             | NaN    | NaN    | NaN     | NaN  | NaN       | NaN            |
| **\*\***          | NaN    | NaN    | NaN     | NaN  | NaN       | NaN            |

---

## 8. Object / Array Operations

| Object/Array \ Other | Number | String | Boolean | Null   | Undefined | Object/Array |
| -------------------- | ------ | ------ | ------- | ------ | --------- | ------------ |
| **+**                | string | string | string  | string | string    | string       |
| **-**                | NaN    | NaN    | NaN     | NaN    | NaN       | NaN          |
| **\***               | NaN    | NaN    | NaN     | NaN    | NaN       | NaN          |
| **/**                | NaN    | NaN    | NaN     | NaN    | NaN       | NaN          |
| **%**                | NaN    | NaN    | NaN     | NaN    | NaN       | NaN          |
| **\*\***             | NaN    | NaN    | NaN     | NaN    | NaN       | NaN          |

---

### Notes

- `+` with string converts the other operand to string (concatenation).
- `-`, `*`, `/`, `%`, `**` → numeric conversion.
- boolean → 1 / 0, null → 0, undefined → NaN.
- Objects/arrays → string for `+`, NaN for other arithmetic.

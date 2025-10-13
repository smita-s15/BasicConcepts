# 📝 JavaScript Conditional Statements

## 1. if Statement

```javascript
if (condition) {
  // code executes if condition is true
} else {
  // code executes if condition is false
}
```

## 2. if...else if...else

```javascript
if (condition1) {
  // code if condition1 is true
} else if (condition2) {
  // code if condition2 is true
} else {
  // code if all conditions are false
}
```

## 3. Ternary Operator

- Syntax: `condition ? exprIfTrue : exprIfFalse`

```javascript
let result = 5 > 3 ? "Yes" : "No";
console.log(result); // "Yes"
```

## 4. switch Statement

```javascript
let day = 3;
switch (day) {
  case 1:
    console.log("Monday");
    break;
  case 2:
    console.log("Tuesday");
    break;
  case 3:
    console.log("Wednesday");
    break;
  default:
    console.log("Invalid day");
}
```

## 5. Truthy and Falsy Values

| Value                | Boolean Conversion |
| -------------------- | ------------------ |
| false                | false              |
| 0                    | false              |
| ""                   | false              |
| null                 | false              |
| undefined            | false              |
| NaN                  | false              |
| []                   | true               |
| {}                   | true               |
| any non-empty string | true               |
| any non-zero number  | true               |

## 6. Tricky Conditional Examples

```javascript
if ([]) {
  console.log("runs");
} // true because array is truthy
if ({}) {
  console.log("runs");
} // true because object is truthy
if (null) {
  console.log("no");
} // false
let x;
if (x) {
  console.log("no");
} // undefined is falsy
```

## 7. Summary

- `if`, `else if`, `else`, `switch`, and ternary allow conditional execution.
- Be aware of **truthy/falsy values** when checking conditions.
- Ternary operator is useful for concise conditional expressions.

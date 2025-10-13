# 📝 JavaScript `while` Loop

The `while` loop is used to execute a block of code **repeatedly as long as a specified condition is true**.

## Syntax

```javascript
while (condition) {
  // code block to execute
}
```

- **condition**: An expression that is evaluated before each iteration. If it evaluates to `true`, the loop continues; if `false`, the loop stops.

## Key Points

- The condition is checked **before** each iteration (pre-check loop).
- If the condition is `false` initially, the loop **does not execute**.
- Avoid infinite loops by ensuring the condition eventually becomes `false`.
- Can be used for **any repeated task** where the number of iterations is not known in advance.

## Examples

### Basic Example

```javascript
let i = 0;
while (i < 5) {
  console.log(i); // Outputs: 0, 1, 2, 3, 4
  i++;
}
```

### Summing Numbers Until Condition

```javascript
let sum = 0;
let num = 1;

while (num <= 5) {
  sum += num;
  num++;
}
console.log(sum); // Outputs: 15
```

### Using `break` in a While Loop

```javascript
let i = 0;
while (true) {
  console.log(i);
  if (i >= 3) {
    break; // exit loop when i is 3
  }
  i++;
}
```

### Using `continue` in a While Loop

```javascript
let i = 0;
while (i < 5) {
  i++;
  if (i === 3) {
    continue; // skip when i is 3
  }
  console.log(i); // Outputs: 1, 2, 4, 5
}
```

## Summary

- `while` loops run as long as the condition is true.
- Pre-check loop: condition is checked before each iteration.
- Useful when number of iterations is not known in advance.
- Use `break` and `continue` to control the loop flow.

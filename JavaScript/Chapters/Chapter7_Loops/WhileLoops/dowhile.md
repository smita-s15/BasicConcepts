# 📝 JavaScript `do…while` Loop

The `do…while` loop is used to execute a block of code **at least once**, and then repeatedly as long as a specified condition is true.

## Syntax

```javascript
do {
  // code block to execute
} while (condition);
```

- **condition**: An expression evaluated **after** each iteration. The loop continues if the condition is `true`.

## Key Points

- Executes the code block **at least once**, even if the condition is initially `false`.
- Condition is checked **after** the block execution (post-check loop).
- Useful when you want the loop to run at least once regardless of the condition.
- Avoid infinite loops by ensuring the condition eventually becomes `false`.

## Examples

### Basic Example

```javascript
let i = 0;
do {
  console.log(i); // Outputs: 0, 1, 2, 3, 4
  i++;
} while (i < 5);
```

### Summing Numbers

```javascript
let sum = 0;
let num = 1;
do {
  sum += num;
  num++;
} while (num <= 5);
console.log(sum); // Outputs: 15
```

### Using `break` in a Do…While Loop

```javascript
let i = 0;
do {
  console.log(i);
  if (i >= 3) {
    break; // exit loop when i is 3
  }
  i++;
} while (true);
```

### Using `continue` in a Do…While Loop

```javascript
let i = 0;
do {
  i++;
  if (i === 3) {
    continue; // skip when i is 3
  }
  console.log(i); // Outputs: 1, 2, 4, 5
} while (i < 5);
```

## Summary

- `do…while` ensures the loop runs **at least once**.
- Post-check loop: condition is evaluated after executing the block.
- Use when you need guaranteed first execution followed by conditional iterations.
- `break` and `continue` can control loop flow inside the loop.

# JavaScript Quick Facts / Gotchas

### 1. Boolean in arithmetic

```javascript
true + 4; // 5
false + 4; // 4
```

> `true` is treated as `1`, `false` as `0` in arithmetic expressions.

### 2. Null in arithmetic

```javascript
null + 5; // 5
```

> `null` is converted to `0` when used in numeric operations.

### 3. Undefined in arithmetic

```javascript
undefined + 5; // NaN
```

> `undefined` cannot be converted to a number, so result is `NaN`.

### 4. Empty array in arithmetic

```javascript
[] + 2 // "2"
[] - 2 // -2
```

> `[]` converts to `""` in `+` (string concatenation) and `0` in `-`.

### 5. Array with one number in arithmetic

```javascript
[3] +
  (2)[3] - // "32"
  2; // 1
```

> Single-element array converts to its value; `+` concatenates as string, `-` coerces to number.

### 6. String concatenation with numbers

```javascript
"5" + 3; // "53"
"5" - 3; // 2
```

> `+` concatenates strings, `-` converts strings to numbers.

### 7. Comparison with `==` and type coercion

```javascript
0 == false; // true
"" == false; // true
null == undefined; // true
```

### 8. Comparison with `===` (strict equality)

```javascript
0 === false; // false
null === undefined; // false
```

> No type coercion happens.

### 9. NaN is not equal to itself

```javascript
NaN === NaN; // false
Number.isNaN(NaN); // true
```

### 10. Math functions with no arguments

```javascript
Math.max(); // -Infinity
Math.min(); // Infinity
```

> Identity values for comparisons.

### 11. Unary `+` converts strings to numbers

```javascript
+"42" + // 42
  "hello"; // NaN
```

### 12. Double NOT `!!` converts value to boolean

```javascript
!!0; // false
!!"abc"; // true
```

### 13. `[]` and `{}` in different contexts

```javascript
[] == ![]; // true
{
}
+[]; // 0 (if interpreted as block) or "[object Object]" depending on context
```

### 14. `typeof null` returns "object"

```javascript
typeof null; // "object"
```

> Historical bug in JavaScript.

### 15. Floating point precision

```javascript
0.1 + 0.2 === 0.3; // false
0.1 + 0.2; // 0.30000000000000004
```

> Due to binary floating-point representation.

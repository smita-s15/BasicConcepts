# 📝 JavaScript `for…in` Loop

The `for…in` loop is used to iterate over **enumerable properties** of an object (including inherited enumerable properties).

## Syntax

```javascript
for (variable in object) {
  // code block to execute
}
```

- **variable**: A string representing the property name (key) of the object.
- **object**: The object whose properties you want to iterate over.

## Key Points

- **Iterates over keys**: The loop iterates over property names, not values.
- **Works with objects, not arrays ideally**: Though you can use it on arrays, it is **not recommended** because it iterates over keys, including inherited enumerable properties.
- **Enumerability matters**: Only enumerable properties are iterated. Non-enumerable properties are skipped.
- **Inherited properties**: Properties inherited through the prototype chain are also included.

## Examples

### Iterating Over Object Properties

```javascript
const person = { name: "Alice", age: 25, city: "Mumbai" };

for (let key in person) {
  console.log(key); // Outputs: name, age, city
  console.log(person[key]); // Outputs: Alice, 25, Mumbai
}
```

### Using with Arrays (Not Recommended)

```javascript
const numbers = [10, 20, 30];

for (let index in numbers) {
  console.log(index); // Outputs: 0, 1, 2
  console.log(numbers[index]); // Outputs: 10, 20, 30
}
```

⚠️ Note: For arrays, prefer `for…of` loop or `Array.prototype.forEach()`.

### Checking Own Properties Only

```javascript
const obj = Object.create({ inherited: "value" });
obj.own = "ownValue";

for (let key in obj) {
  if (obj.hasOwnProperty(key)) {
    console.log(key, obj[key]); // Outputs: own ownValue
  }
}
```

## Summary

- Use `for…in` to iterate object keys.
- Avoid for arrays — use `for…of` or `forEach`.
- Combine with `hasOwnProperty()` to exclude inherited properties.

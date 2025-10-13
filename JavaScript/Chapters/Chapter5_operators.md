# 📝 JavaScript Operators

## 1. Arithmetic Operators+

| Operator | Description              | Example                   | Output           | Notes                                          |
| -------- | ------------------------ | ------------------------- | ---------------- | ---------------------------------------------- |
| +        | Addition / Concatenation | 5 + 3, "Hello" + " World" | 8, "Hello World" | If one operand is string, concatenation occurs |
| -        | Subtraction              | 10 - 4                    | 6                | Operands converted to number                   |
| \*       | Multiplication           | 6 \* 3                    | 18               | NaN if invalid type                            |
| /        | Division                 | 12 / 4                    | 3                | NaN if invalid type                            |
| %        | Modulus (Remainder)      | 10 % 3                    | 1                | NaN if invalid type                            |
| \*\*     | Exponentiation           | 2 \*\* 3                  | 8                | Right-associative                              |

## 2. Assignment Operators

| Operator | Description         | Example   | Notes                  |
| -------- | ------------------- | --------- | ---------------------- |
| =        | Assign value        | let a = 5 | simple assignment      |
| +=       | Add and assign      | a += 3    | coerces type if needed |
| -=       | Subtract and assign | a -= 2    | coerces type if needed |
| \*=      | Multiply and assign | a \*= 2   | coerces type if needed |
| /=       | Divide and assign   | a /= 2    | coerces type if needed |
| %=       | Modulus and assign  | a %= 3    | coerces type if needed |
| \*\*=    | Exponent and assign | a \*\*= 2 | coerces type if needed |

## 3. Comparison Operators

| Operator | Description        | Example   | Output | Notes                        |
| -------- | ------------------ | --------- | ------ | ---------------------------- |
| ==       | Equal to (loose)   | 5 == "5"  | true   | type coercion applied        |
| ===      | Equal to (strict)  | 5 === "5" | false  | no type coercion             |
| !=       | Not equal (loose)  | 5 != "6"  | true   | type coercion applied        |
| !==      | Not equal (strict) | 5 !== "5" | true   | no type coercion             |
| >        | Greater than       | 7 > 3     | true   | converts to number if needed |
| <        | Less than          | 3 < 7     | true   | converts to number if needed |
| >=       | Greater or equal   | 5 >= 5    | true   | converts to number if needed |
| <=       | Less or equal      | 4 <= 5    | true   | converts to number if needed |

## 4. Logical Operators

| Operator | Description | Example       | Output     | Notes                                   |     |       |      |                                          |
| -------- | ----------- | ------------- | ---------- | --------------------------------------- | --- | ----- | ---- | ---------------------------------------- |
| &&       | Logical AND | true && false | false      | returns first falsy value or last value |     |       |      |                                          |
|          |             |               | Logical OR | true                                    |     | false | true | returns first truthy value or last value |
| !        | Logical NOT | !true         | false      | converts value to boolean               |     |       |      |                                          |

## 5. Unary Operators

| Operator | Description                 | Example        | Output       | Notes                                   |
| -------- | --------------------------- | -------------- | ------------ | --------------------------------------- |
| +        | Converts to number          | +"5"           | 5            | unary plus forces numeric conversion    |
| -        | Converts to negative number | -"5"           | -5           | unary minus forces numeric conversion   |
| ++       | Increment                   | let a=5; a++   | 5 (then a=6) | post-increment vs pre-increment matters |
| --       | Decrement                   | let a=5; --a   | 4            | pre-decrement vs post-decrement matters |
| typeof   | Returns type                | typeof 5       | "number"     | safe for undefined variables            |
| delete   | Deletes property            | delete obj.key | true/false   | only works on object properties         |

## 6. Special Cases (Type Coercion)

| Operation           | Result             | Explanation                           |
| ------------------- | ------------------ | ------------------------------------- |
| "5" + 5             | "55"               | String concatenation                  |
| 5 + true            | 6                  | Boolean → 1                           |
| 5 + false           | 5                  | Boolean → 0                           |
| 5 - "2"             | 3                  | String converted to number            |
| null + 5            | 5                  | null → 0                              |
| undefined + 5       | NaN                | undefined cannot convert to number    |
| undefined + "Hello" | "undefinedHello"   | undefined converted to string         |
| {} + 5              | "[object Object]5" | Object converted to string            |
| [] + 5              | "5"                | Empty array converted to empty string |
| [1] + 5             | "15"               | Array converted to string             |
| [1,2] + 5           | "1,25"             | Array converted to string             |

# 🚀 JavaScript Interview Quick Notes

------------------------------------------------------------------------

## 1️⃣ Declarations & TDZ

-   **var** → function scope \| hoisted = `undefined` \| redeclare ✅\
-   **let** → block scope \| hoisted but TDZ \| redeclare ❌ \| reassign
    ✅\
-   **const** → block scope \| hoisted but TDZ \| redeclare ❌ \|
    reassign ❌ (but object mutate ✅)\
-   **TDZ** → time between scope entry & declaration → accessing throws
    `ReferenceError`.

**Mnemonic:**\
👉 `var = loose` \| `let = strict but flexible` \|
`const = strict & fixed`

------------------------------------------------------------------------

## 2️⃣ Scope & Closures

-   Scope: **Global → Function → Block**\
-   Closure: Inner fn "remembers" parent scope even after parent exits.

👉 Used for **data privacy, currying, callbacks**.

------------------------------------------------------------------------

## 3️⃣ Hoisting

-   **var & function** declarations hoisted (var = `undefined`).\
-   **let/const** hoisted but inaccessible (TDZ).

------------------------------------------------------------------------

## 4️⃣ ES6+ Must-Knows

-   **Arrow fn:** no own `this`, concise syntax.\
-   **Template literals:** backticks + `${}` + multiline.\
-   **Destructuring:** unpack arrays/objects.\
-   **Spread (`...`):** expand iterable.\
-   **Rest (`...`):** collect into array.\
-   **Default params:** fn params with fallback.\
-   **Modules:** `import / export`.

------------------------------------------------------------------------

## 5️⃣ Async JS

-   **Callbacks:** old, leads to hell.\
-   **Promises:** `then/catch`, 3 states.\
-   **Async/Await:** cleaner promises.\
-   **Fetch API:** built-in HTTP.\
-   **Axios:** external lib (extra features).

**Event Loop:** Single-thread, manages stack + microtasks (Promises) +
macrotasks (Timers).

------------------------------------------------------------------------

## 6️⃣ Objects & Inheritance

-   **Prototype chain** = inheritance backbone.\
-   **Class (ES6):** sugar over prototype.

------------------------------------------------------------------------

## 7️⃣ FP Concepts

-   **HOFs:** `map`, `filter`, `reduce`.\
-   **Immutability + Pure fns** → predictable code.

------------------------------------------------------------------------

## 8️⃣ Error Handling

-   **Types:** Syntax, Runtime, Logical, Type, Memory, I/O.\
-   Handle via `try...catch` or promises `.catch`.

------------------------------------------------------------------------

## 9️⃣ DOM & Events

-   **Access elements:** `getElementById`, `querySelector`.\
-   **Event phases:** Capturing → Target → Bubbling.\
-   **Delegation:** parent listens, detects child target.

------------------------------------------------------------------------

## 🔟 Performance Patterns

-   **Debounce:** run after pause.\
-   **Throttle:** run every X ms.

------------------------------------------------------------------------

## 1️⃣1️⃣ this Binding

-   **call / apply:** run immediately, custom `this`.\
-   **bind:** return new fn with fixed `this`.

------------------------------------------------------------------------

## 1️⃣2️⃣ Equality & Values

-   `==` → loose, coercion.\
-   `===` → strict, no coercion.\
-   `null` → intentional empty.\
-   `undefined` → declared, no value.

------------------------------------------------------------------------

## 1️⃣3️⃣ Modern APIs

-   **Web Workers:** background threads.\
-   **Service Workers:** offline & caching.\
-   **WebSockets:** realtime comms.\
-   **Intl API:** i18n support.

------------------------------------------------------------------------

## 1️⃣4️⃣ Tooling & Safety

-   **Modules:** structure.\
-   **Bundlers:** Webpack, Rollup.\
-   **Transpilers:** Babel.\
-   **TypeScript:** type safety layer.

------------------------------------------------------------------------

🧠 **Memory Hook (Mnemonic Chain):**\
`var-let-const → Scope → Hoist → ES6+ → Async → Proto → FP → Errors → DOM → Perf → this → Equality → APIs → Tooling`

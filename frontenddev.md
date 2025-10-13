# Frontend Developer Interview Questions

## 1. JavaScript Core

1. What is **hoisting** in JavaScript? Which things are hoisted?
2. What are **block-scoped variables**? How are `let` and `const` different from `var`?
3. Explain the **event loop** in JavaScript with an example.
4. Write a program that demonstrates **event loop execution order** (with `setTimeout`, `Promise`, and normal log).
5. What are **closures**? How do they store values even after the outer function has executed?
6. Write a function that **memoizes** results of an array operation.
7. Write a **palindrome program** in JavaScript.
8. Explain **throttling** vs **debouncing** with use cases.
9. If we already limit API calls using a counter, why do we still need **debouncing**?
10. Why use **arrow functions**? When should you not use them?
11. What are **pure functions**? Why are they important?
12. Difference between **shallow copy** and **deep copy** in JS.
13. Explain **prototypal inheritance** in JavaScript.
14. What is the difference between `==` and `===`?
15. How does **JavaScript garbage collection** work?
16. What are **generators** and when to use them?
17. Explain **Promises** vs **async/await**.
18. How does **`this` keyword** behave differently in arrow functions vs normal functions?
19. Explain **call, apply, bind** with examples.
20. How does **event delegation** work in JavaScript?

---

## 2. React / UI

1. What is the **Virtual DOM** and how does it optimize performance?
2. What are **hooks**? How are they different from normal functions?
3. Which **hook** would you use for rendering a string and why?
4. Explain **useMemo hook** with implementation.
5. Explain **useRef hook** in detail. Give an example use case.
6. How do you create a **custom hook**? When should you use it?
7. Difference between **useEffect** and **useLayoutEffect**.
8. What is the role of **keys in React**?
9. Explain **SSR (Server-Side Rendering)** vs **CSR (Client-Side Rendering)**. Why is SSR often more optimized?
10. What are **basic routing techniques** in React?
11. What is a **Single Page Application (SPA)**? How does it differ from MPA?
12. What steps would you take to **debug a slow React app**?
13. What is **React Fiber** and why was it introduced?
14. Explain **reconciliation** in React.
15. Difference between **controlled** vs **uncontrolled components**.
16. How does **React suspense** work?
17. When should you use **React context API** instead of Redux?
18. What is **code splitting** and how do you implement it in React?
19. What are **React portals**? When would you use them?
20. Explain **hydration** in React SSR.

---

## 3. CSS & Styling

1. Difference between **Bootstrap** and **Tailwind CSS**.
2. Explain the **Flexbox model** with examples.
3. What does `flex-direction: row-reverse;` do?
4. What is **Atomic Design Pattern**? How is it used in UI development?
5. Explain **theming** in a frontend app.
6. How do **CSS animations** work? Example of `@keyframes`.
7. Difference between **relative**, **absolute**, **fixed**, and **sticky** positioning.
8. Explain **CSS Grid** vs **Flexbox** – when to use which.
9. What are **CSS Modules**? Why use them?
10. What is the difference between **em**, **rem**, and **px** units?
11. Explain **critical CSS** and why it improves performance.
12. How to implement **dark mode theming** in a React app?
13. What is **FOUC (Flash of Unstyled Content)** and how to prevent it?

---

## 4. Web Architecture & APIs

1. What is **CORS**? Why does it occur and how can you solve it?
2. Explain the **webpage rendering pipeline** (from request → paint).
3. What are **browser push notifications** and how are they implemented?
4. Difference between **Web Workers** and **Service Workers**.
5. How do **build tools** like Webpack/Gulp/Grunt help in frontend development?
6. What are **CSS preprocessors** (SASS/LESS)? Why use them?
7. What are **REST APIs**? How do they differ from **GraphQL**?
8. Explain **JWT authentication** flow.
9. What are **HTTP/2** and **HTTP/3** improvements for frontend performance?
10. What is **lazy loading**? How do you implement it?
11. How do **CDNs** help improve performance?
12. What is **tree shaking** in bundlers like Webpack?
13. What are **micro-frontends**? Benefits and trade-offs.
14. Explain **state hydration** when rendering SSR apps.

---

## 5. Full-Stack / System Awareness

1. What is the role of **caching layers** and **proxies** in web systems?
2. How would you handle performance optimization at **API level**?
3. Why is knowledge of **Node.js** a plus for frontend developers?
4. How do you ensure **cross-browser compliance** in your projects?
5. What is **OAuth2**? How does it differ from **OpenID Connect**?
6. Explain **XSS (Cross-Site Scripting)** and how to prevent it.
7. What is **CSRF (Cross-Site Request Forgery)** and how to prevent it?
8. Explain **Content Security Policy (CSP)**.
9. How does **browser caching** (ETags, cache-control headers) improve performance?
10. How would you design a **rate limiter** for APIs?
11. How do **service workers** enable **offline-first PWAs**?
12. Explain **isomorphic/universal JavaScript**.

# Frontend Developer Interview Q&A

## 1. JavaScript Core

### 1. What is hoisting in JavaScript? Which things are hoisted?

Hoisting is JavaScript's default behavior of moving **function declarations** and **variable declarations (var)** to the top of their scope before execution.

- `var` is hoisted with value `undefined`.
- `let` and `const` are hoisted but remain in the _temporal dead zone_.
- Function declarations are fully hoisted.

### 2. What are block-scoped variables?

Variables declared with `let` and `const` are block-scoped, meaning they exist only within `{ }`.  
`var` is function-scoped.

### 3. Explain the event loop in JavaScript with an example.

The **event loop** continuously checks the call stack and the callback queue.

- Sync code → Call stack.
- Async tasks → Callback/Microtask queues.
- Microtasks (`Promise.then`) run before macrotasks (`setTimeout`).

**Example:**

```js
console.log("A");
setTimeout(() => console.log("B"), 0);
Promise.resolve().then(() => console.log("C"));
console.log("D");
```

**Output:** A → D → C → B

### 4. What are closures?

A closure is a function that remembers the environment in which it was created, even after the outer function has finished executing.

```js
function outer() {
  let count = 0;
  return function inner() {
    count++;
    return count;
  };
}
const counter = outer();
console.log(counter()); // 1
console.log(counter()); // 2
```

### 5. Write a palindrome program in JS

```js
function isPalindrome(str) {
  str = str.toLowerCase();
  return str === str.split("").reverse().join("");
}
console.log(isPalindrome("madam")); // true
```

### 6. Throttling vs Debouncing

- **Throttling**: Limits execution to once every X ms. Good for **scroll, resize** events.
- **Debouncing**: Executes only after no calls have been made for X ms. Good for **search input, API calls**.

---

## 2. React / UI

### 1. What is Virtual DOM?

A lightweight in-memory representation of the real DOM. React compares the Virtual DOM with the previous version (**diffing**) and applies minimal changes to the real DOM (**reconciliation**), improving performance.

### 2. What are hooks?

Hooks let you use state and lifecycle features in functional components.  
They are different from normal functions because React tracks them during rendering.

### 3. useMemo Example

```js
import React, { useMemo } from "react";

function ExpensiveCalc({ num }) {
  const squared = useMemo(() => {
    console.log("Calculating...");
    return num * num;
  }, [num]);

  return <div>{squared}</div>;
}
```

### 4. useRef Example

`useRef` provides a mutable object that persists across renders.  
Use cases: accessing DOM nodes, storing mutable values.

```js
import React, { useRef, useEffect } from "react";

function Timer() {
  const count = useRef(0);
  useEffect(() => {
    count.current++;
    console.log("Render count:", count.current);
  });
  return <h1>Check console</h1>;
}
```

### 5. Keys in React

Keys help React identify which items have changed, are added, or removed in a list.  
Without keys, React re-renders unnecessarily.

### 6. SSR vs CSR

- **CSR**: Rendering happens in browser. Faster after load, but slower initial load.
- **SSR**: HTML is pre-rendered on server, faster first paint, better SEO.  
  React hydrates SSR content to attach event listeners.

---

## 3. CSS & Styling

### 1. Flexbox Example

```css
.container {
  display: flex;
  flex-direction: row-reverse;
}
```

### 2. Atomic Design Pattern

UI is broken into: Atoms → Molecules → Organisms → Templates → Pages.  
This promotes reusability and scalability.

### 3. Theming

Use CSS variables or context API to define themes (light/dark).

### 4. CSS Animations Example

```css
@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
.element {
  animation: fadeIn 2s ease-in;
}
```

---

## 4. Web Architecture & APIs

### 1. What is CORS?

Cross-Origin Resource Sharing (CORS) is a security mechanism restricting requests from different origins.  
Solved by setting proper headers (`Access-Control-Allow-Origin`).

### 2. Web Worker vs Service Worker

- **Web Worker**: Runs JS in background thread for computation.
- **Service Worker**: Proxy between browser and network. Enables caching, offline apps, push notifications.

### 3. SPA

Single Page Application loads once, then updates dynamically using JavaScript (React, Vue, Angular).

---

## 5. Full-Stack / System Awareness

### 1. How do you prevent XSS?

- Escape user input.
- Use `innerText` instead of `innerHTML`.
- Apply CSP (Content Security Policy).

### 2. How do you prevent CSRF?

- Use anti-CSRF tokens.
- SameSite cookies.

### 3. Debugging a slow website

- Use **Lighthouse / DevTools** for performance profiling.
- Optimize images.
- Use lazy loading.
- Minimize bundle size (tree shaking, code splitting).
- Optimize API calls and caching.

Interview-Ready Q&A

1. What is Hoisting in JavaScript?

Answer:
Hoisting means moving declarations (not initializations) to the top of their scope during the compile phase.

var is hoisted as undefined.

let and const are hoisted but stay in Temporal Dead Zone (TDZ) until initialized.

Functions are fully hoisted with definitions.

2. What do you mean by Block Scoped Variables?

Answer:
Variables declared with let and const are block-scoped, meaning they exist only within {}. Unlike var (function/global scoped), they don’t leak outside and prevent accidental overwrites.

3. What is the Event Loop in JavaScript?

Answer:
The Event Loop manages execution:

Executes synchronous code (call stack).

Moves async tasks (setTimeout, promises, I/O) from callback/microtask queues into the call stack when free.

Order:

All synchronous code →

Microtasks (Promises, queueMicrotask) →

Macrotasks (setTimeout, setInterval, I/O).

Code Example (execution order):

console.log("A");
setTimeout(() => console.log("B"), 0);
Promise.resolve().then(() => console.log("C"));
console.log("D");

// Output: A, D, C, B

4. What is the Virtual DOM & How does it Optimize Performance?

Answer:
Virtual DOM is a lightweight JS object copy of the real DOM.
React compares the old and new VDOM using diffing and updates only changed nodes (reconciliation).
This avoids costly direct DOM manipulations and improves performance.

5. What are Closures? How do they Store Values?

Answer:
A closure is a function that remembers the scope it was created in, even after that scope is gone.
It stores variables in the function’s lexical environment, not in memory snapshot.

Example:

function counter() {
let count = 0;
return function() {
return ++count;
}
}
const c1 = counter();
console.log(c1()); // 1
console.log(c1()); // 2

6. What are React Hooks? Which Hook for rendering a string & Why?

Answer:
Hooks are functions that let you use state, lifecycle, and refs in functional components.

To render a string → use useState (re-render when string changes).

Example:

const [text, setText] = useState("Hello");

7. Why useMemo Hook?

Answer:
useMemo memoizes expensive calculations so they don’t recompute on every render.

const memoizedValue = useMemo(() => heavyCalc(arr), [arr]);

This improves performance for heavy/recursive calculations.

8. Why useRef Hook?

Answer:
useRef stores mutable values that persist across renders without causing re-renders.

Used for: accessing DOM nodes, storing previous values, caching.

const countRef = useRef(0);
countRef.current++; // persists across renders

9. Function: Perform operation on Array + Memoize
   function memoizedSum() {
   let cache = {};
   return function(arr) {
   const key = arr.toString();
   if (cache[key]) return cache[key];
   const sum = arr.reduce((a, b) => a + b, 0);
   cache[key] = sum;
   return sum;
   }
   }
   const sumArr = memoizedSum();
   console.log(sumArr([1,2,3])); // 6
   console.log(sumArr([1,2,3])); // from cache: 6

10. Palindrome Program
    function isPalindrome(str) {
    str = str.toLowerCase().replace(/[^a-z0-9]/g,"");
    return str === str.split("").reverse().join("");
    }
    console.log(isPalindrome("Racecar")); // true

11. Throttling vs Debouncing

Throttling: Limit a function execution to once every X ms (used in scroll, resize).

Debouncing: Delays execution until user stops triggering for X ms (used in search input).

Why debouncing for API calls? → It prevents unnecessary requests, ensures only the final intent triggers API call, saving bandwidth.

12. Role of Keys in React

Answer:
Keys identify elements in a list. React uses keys to decide which items changed/added/removed during reconciliation.
Without keys → React may re-render inefficiently or reorder wrongly.

13. CSR vs SSR

CSR (Client-Side Rendering): Browser downloads JS, renders on client. Initial load slower, but faster navigation after load.

SSR (Server-Side Rendering): Server sends pre-rendered HTML, then hydrates on client. Improves SEO + faster first paint.

Why SSR optimized? → Browser gets ready HTML → reduces Time to First Byte (TTFB) & improves performance on slow networks/devices.

✅ Would you like me to also create a "Mock Interview" style list (like: interviewer question → how to answer → follow-up tricky counter-question) for these topics so you can practice speaking answers live?

You said:

- ChatGPT said:

Got it 👍 You want me to now turn these into a Mock Interview Q&A style list with:

Question (as an interviewer would ask)

Answer (short, interview-ready)

Follow-up / Tricky angle (what interviewer might dig deeper into)

🔹 Mock Interview Q&A

1. Hoisting

Q: What is hoisting in JavaScript?
A: JavaScript moves variable and function declarations to the top of their scope at compile time. var is hoisted as undefined, let/const are hoisted but in Temporal Dead Zone, functions are hoisted with their definitions.
Follow-up: Why is accessing a let variable before declaration an error while var gives undefined?

2. Block Scope

Q: Difference between var, let, and const scope?
A: var → function/global scope. let and const → block scope {} and prevent redeclaration.
Follow-up: If const is block scoped, can its value be changed?

3. Event Loop

Q: Explain event loop execution order with example.
A: Event loop executes sync → microtasks (promises) → macrotasks (timeouts).

console.log("A");
setTimeout(()=>console.log("B"),0);
Promise.resolve().then(()=>console.log("C"));
console.log("D");
// Output: A, D, C, B

Follow-up: What happens if you nest setTimeout inside a promise?

4. Virtual DOM

Q: How does Virtual DOM improve performance?
A: It creates a lightweight copy of the DOM, diffs old vs new, and updates only changed nodes. This reduces expensive DOM manipulations.
Follow-up: What is reconciliation?

5. Closures

Q: What are closures?
A: A closure is a function that remembers the variables of its lexical scope, even after the scope is gone.
Follow-up: How do closures help in creating private variables?

6. Hooks

Q: Which Hook would you use to render a string dynamically and why?
A: useState, because state changes trigger re-render.
Follow-up: Why not use useRef for storing string?

7. useMemo

Q: Why use useMemo?
A: To memoize expensive calculations and avoid recomputation on every render.
Follow-up: Difference between useMemo and useCallback?

8. useRef

Q: What’s the deep execution role of useRef?
A: It stores mutable values across renders without triggering re-render. Common for DOM refs and caching values.
Follow-up: How to implement previous state tracking with useRef?

9. Memoization Example

Q: Write a function that memoizes array operations.
A:

function memoizedSum() {
let cache = {};
return arr => {
const key = arr.toString();
if (cache[key]) return cache[key];
return cache[key] = arr.reduce((a,b)=>a+b,0);
};
}

Follow-up: How does useMemo in React handle this internally?

10. Palindrome

Q: Write a palindrome program.
A:

function isPalindrome(str){
str = str.toLowerCase().replace(/[^a-z0-9]/g,"");
return str === [...str].reverse().join("");
}

Follow-up: Optimize without reversing the string?

11. Throttling vs Debouncing

Q: Difference between throttling and debouncing?
A:

Throttle → run at most once per X ms.

Debounce → run only after X ms silence.
Follow-up: Why debounce is preferred in API search calls?

12. React Keys

Q: Why are keys important in React lists?
A: They help React identify which items changed, added, or removed during reconciliation. Without keys, React may re-render inefficiently or reorder incorrectly.
Follow-up: What happens if you use array index as a key?

13. CSR vs SSR

Q: Difference between CSR and SSR?
A:

CSR → browser renders UI after JS loads, slower initial paint, good for apps.

SSR → server sends pre-rendered HTML, improves SEO and initial load.
Follow-up: How does SSR reduce Time To First Byte (TTFB)?

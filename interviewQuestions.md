# Frontend Developer Interview Q&A

## Section 1: HTML & CSS

**Inline vs inline-block vs block**

- Inline: Takes only needed width, no line break (e.g., `<span>`).

- Inline-block: Behaves like inline but allows width/height.
- Block: Takes full width, starts on a new line (e.g., `<div>`).

**Positioning: relative, absolute, fixed, sticky**

- Relative: Positioned relative to its normal position.

- Absolute: Positioned relative to nearest positioned ancestor.
- Fixed: Stays relative to viewport (doesn't scroll).
- Sticky: Switches between relative & fixed based on scroll.

**Flexbox model** - `display: flex;` arranges items along main & cross
axis.

- `flex-direction: row-reverse`: reverses order horizontally.
- `justify-content`: alignment on main axis.
- `align-items`: alignment on cross axis.

**CSS Grid vs Flexbox** - Flexbox: One-dimensional (row OR column).

- Grid: Two-dimensional (rows AND columns).

**Atomic design pattern** - Break UI into atoms (buttons), molecules
(form + label), organisms (header), templates, and pages.

- Encourages reusability and consistency.

**Theming in Tailwind/Bootstrap** - Define reusable color palettes,
fonts, and spacing.

- Tailwind: via `tailwind.config.js`.
- Bootstrap: via SCSS variables.

**Transitions vs Animations** - Transition: Property change over time
(hover effects).

- Animation: Keyframes allow multi-step or looping effects.

---

## Section 2: JavaScript

**Hoisting** - Variable/function declarations moved to top of scope.

- `var` is hoisted & initialized with `undefined`.
- `let/const` hoisted but in "temporal dead zone."

**Block scope: var vs let vs const** - `var`: Function-scoped.

- `let`/`const`: Block-scoped.
- `const`: Must be initialized; value cannot be reassigned.

**Event loop** - Executes call stack first.

- Then processes microtasks (Promises, MutationObserver).
- Then macrotasks (setTimeout, setInterval).
- Example:
  `js   console.log(1);   setTimeout(()=>console.log(2));   Promise.resolve().then(()=>console.log(3));   console.log(4);   // Output: 1,4,3,2`

**Closures** - Function + its lexical scope even after outer function
exits.
in
- Example:
  `js   function outer() {     let x = 10;     return function inner() { return x; }   }   let fn = outer(); fn(); // 10`

**Arrow vs normal functions** - Arrow: Shorter syntax, no `this`, no
`arguments`.

- Normal: Has its own `this`, usable as constructor.

**Pure functions** - Given same input → always same output.

- No side effects.
- Example: `(a,b)=>a+b`.

**Throttling vs Debouncing** - Throttle: Limit function execution to
once in a given interval.

- Debounce: Delay execution until user stops triggering.
- Example: Search bar input → debounce API call.

---

## Section 3: React

**Virtual DOM** - JS object representation of UI.

- React updates only changed nodes via diffing → improves performance.

**Hooks** - Functions to use state & lifecycle in functional
components.

- Examples: `useState`, `useEffect`, `useContext`.

**Normal vs custom hooks** - Normal: General JS function.

- Custom hook: Uses built-in hooks inside, must start with `use`.

**useEffect vs useLayoutEffect** - `useEffect`: Runs after render
(async, non-blocking).

- `useLayoutEffect`: Runs before paint (blocking).

**useMemo** - Memoizes expensive calculations.

- Example:
  `js   const value = useMemo(()=>computeExpensive(data), [data]);`

**useRef** - Holds mutable values across renders without causing
re-render.

- Common uses: Access DOM nodes, store previous value.

**Memoize array operation**

```js
const sum = useMemo(() => arr.reduce((a, b) => a + b, 0), [arr]);
```

**Keys in React** - Help React identify elements in list rendering.

- Avoids re-rendering unchanged elements.

**SPA vs SSR** - SPA: Client-side renders after JS loads. Faster
navigation, worse SEO.

- SSR: Server renders HTML, better SEO & first paint.

---

## Section 4: Browser & Performance

**Webpage rendering process** 1. Parse HTML → DOM. 2. Parse CSS → CSSOM. 3. Combine → Render tree. 4. Layout → Paint → Composite.

**CORS** - Security policy restricting cross-origin requests.

- Fixed with proper headers (`Access-Control-Allow-Origin`).

**Browser push notifications** - Implemented via Service Workers + Push
API.

- Require user permission, work even when site is closed.

**Web Worker vs Service Worker** - Web Worker: Runs JS in background
thread (no DOM access).

- Service Worker: Proxy between browser & network (offline, caching, push).

**Debug slow website** - Check network requests.

- Audit with Chrome DevTools.
- Optimize images, caching, bundle size, avoid re-renders.

---

## Section 5: Coding Round

**Palindrome program**

```js
function isPalindrome(str) {
  return str === str.split("").reverse().join("");
}
```

**React counter**

```jsx
function Counter() {
  const [count, setCount] = React.useState(0);
  return (
    <>
      <button onClick={() => setCount(count - 1)}>-</button>
      {count}
      <button onClick={() => setCount(count + 1)}>+</button>
    </>
  );
}
```

**Debounce function**

```js
function debounce(fn, delay) {
  let timer;
  return (...args) => {
    clearTimeout(timer);
    timer = setTimeout(() => fn(...args), delay);
  };
}
```

**React API component (basic)**

```jsx
function Users() {
  const [users, setUsers] = React.useState([]);
  const [loading, setLoading] = React.useState(true);

  React.useEffect(() => {
    fetch("https://jsonplaceholder.typicode.com/users")
      .then((res) => res.json())
      .then((data) => {
        setUsers(data);
        setLoading(false);
      });
  }, []);

  if (loading) return <p>Loading...</p>;

  return (
    <ul>
      {users.map((u) => (
        <li key={u.id}>{u.name}</li>
      ))}
    </ul>
  );
}
```

---

## Section 6: Situational

**React app slow with large lists** - Use `React.memo`, `useMemo`.

- Virtualize lists (e.g., `react-window`).
- Avoid unnecessary re-renders.

**CORS error in prod** - Check backend headers.

- Configure reverse proxy (e.g., Nginx).
- Validate allowed origins.

**Dark mode theming** - Use CSS variables or Tailwind theme toggle.

- Store preference in `localStorage`.

**Sharing state between components** - Lift state up.

- Or use Context API / Redux.

**SEO optimization: CSR vs SSR** - CSR: JS-heavy, slower initial load,
poor SEO.

- SSR: HTML generated on server, better SEO & performance.

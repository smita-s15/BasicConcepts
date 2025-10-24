# Step 2: React Hooks

React Hooks allow you to **use state and other React features without writing class components**.  
They simplify logic, improve code reusability, and make components cleaner and more maintainable.

---

## 1. useState

### Purpose

`useState` is used to manage **state** in a functional component.

### Syntax

```jsx
const [state, setState] = useState(initialValue);
```

### Example

```jsx
import { useState } from "react";

function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <h1>{count}</h1>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
}
```

---

## 2. useEffect

### Purpose

`useEffect` handles **side effects** such as API calls, DOM manipulation, and subscriptions.

### Syntax

```jsx
useEffect(() => {
  // effect code
  return () => {
    // cleanup code
  };
}, [dependencies]);
```

### Example: Without Dependencies (Runs every render)

```jsx
useEffect(() => {
  console.log("Component rendered");
});
```

### Example: With Dependencies (Runs when `count` changes)

```jsx
useEffect(() => {
  console.log("Count changed:", count);
}, [count]);
```

### Example: Cleanup Function

```jsx
useEffect(() => {
  const interval = setInterval(() => console.log("Running..."), 1000);
  return () => clearInterval(interval); // Cleanup
}, []);
```

### Multiple Effects

You can use multiple `useEffect` hooks for different logic blocks.

---

## 3. useRef

### Purpose

`useRef` stores a **mutable reference** that persists between renders. It does **not trigger re-renders**.

### Example: Accessing DOM

```jsx
import { useRef } from "react";

function FocusInput() {
  const inputRef = useRef();

  const handleFocus = () => inputRef.current.focus();

  return (
    <div>
      <input ref={inputRef} type="text" />
      <button onClick={handleFocus}>Focus Input</button>
    </div>
  );
}
```

### Example: Storing Previous Value

```jsx
const prevValue = useRef();
useEffect(() => {
  prevValue.current = value;
}, [value]);
```

---

## 4. useContext

### Purpose

`useContext` allows you to access global data without prop drilling.

### Example

```jsx
import { createContext, useContext } from "react";

const UserContext = createContext();

function Child() {
  const user = useContext(UserContext);
  return <h1>Hello, {user}</h1>;
}

function App() {
  return (
    <UserContext.Provider value="Smita">
      <Child />
    </UserContext.Provider>
  );
}
```

---

## 5. useMemo

### Purpose

`useMemo` memoizes **expensive computations**, preventing recalculation unless dependencies change.

### Syntax

```jsx
const memoizedValue = useMemo(() => computeExpensiveValue(a, b), [a, b]);
```

### Example

```jsx
const squared = useMemo(() => num * num, [num]);
```

---

## 6. useCallback

### Purpose

`useCallback` memoizes **functions**, preventing unnecessary re-creations on re-render.

### Example

```jsx
const handleClick = useCallback(() => {
  console.log("Clicked!");
}, []);
```

Useful when passing callbacks to **child components** to prevent re-renders.

---

## 7. useReducer

### Purpose

Alternative to `useState` for complex state logic.

### Syntax

```jsx
const [state, dispatch] = useReducer(reducer, initialState);
```

### Example

```jsx
function reducer(state, action) {
  switch (action.type) {
    case "increment":
      return { count: state.count + 1 };
    case "decrement":
      return { count: state.count - 1 };
    default:
      return state;
  }
}

function Counter() {
  const [state, dispatch] = useReducer(reducer, { count: 0 });

  return (
    <div>
      <h1>{state.count}</h1>
      <button onClick={() => dispatch({ type: "increment" })}>+</button>
      <button onClick={() => dispatch({ type: "decrement" })}>-</button>
    </div>
  );
}
```

---

## 8. Custom Hooks (Creation and Usage)

### Purpose

Custom Hooks allow you to **extract reusable logic** from components.

### Example

```jsx
function useFetch(url) {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch(url)
      .then((res) => res.json())
      .then((data) => setData(data));
  }, [url]);

  return data;
}

function App() {
  const users = useFetch("https://jsonplaceholder.typicode.com/users");
  return <pre>{JSON.stringify(users, null, 2)}</pre>;
}
```

---

## 9. Rules of Hooks

1. **Only call Hooks at the top level** (not inside loops, conditions, or nested functions).
2. **Only call Hooks inside React components or Custom Hooks.**
3. Hook names should always start with **“use”** (like `useFetch`, `useForm`).
4. Maintain dependency arrays carefully to avoid infinite loops.

---

## 10. useLayoutEffect

### Purpose

Like `useEffect`, but runs **synchronously after DOM mutations** — useful for layout calculations.

### Example

```jsx
useLayoutEffect(() => {
  console.log("DOM updated before paint");
}, []);
```

---

## 11. useImperativeHandle

### Purpose

Customizes the instance value exposed when using `ref` with `forwardRef`.

### Example

```jsx
import { useImperativeHandle, useRef, forwardRef } from "react";

const Input = forwardRef((props, ref) => {
  const inputRef = useRef();

  useImperativeHandle(ref, () => ({
    focus: () => inputRef.current.focus(),
  }));

  return <input ref={inputRef} />;
});

function App() {
  const ref = useRef();
  return (
    <>
      <Input ref={ref} />
      <button onClick={() => ref.current.focus()}>Focus from Parent</button>
    </>
  );
}
```

---

## 12. useId

### Purpose

Generates a **unique ID** for accessibility or list rendering.

### Example

```jsx
const id = useId();
<label htmlFor={id}>Email</label>
<input id={id} type="email" />
```

---

## 13. useTransition

### Purpose

Used for **smoother UI updates** by marking state updates as “non-urgent.”

### Example

```jsx
const [isPending, startTransition] = useTransition();

function handleInputChange(e) {
  const value = e.target.value;
  startTransition(() => {
    setFilter(value);
  });
}
```

---

## 14. useDeferredValue

### Purpose

Defers a value to improve performance when rendering large lists or slow components.

### Example

```jsx
const deferredValue = useDeferredValue(value);
```

Used with heavy rendering to keep UI responsive.

---

## 15. useDebugValue

### Purpose

Displays a label in React DevTools for **custom hooks debugging**.

### Example

```jsx
function useOnlineStatus() {
  const [online, setOnline] = useState(true);
  useDebugValue(online ? "Online" : "Offline");
  return online;
}
```

---

## ✅ Summary

| Hook                | Purpose                         |
| ------------------- | ------------------------------- |
| useState            | Manage state                    |
| useEffect           | Handle side effects             |
| useRef              | Persist data between renders    |
| useContext          | Access context data             |
| useMemo             | Optimize expensive calculations |
| useCallback         | Optimize functions              |
| useReducer          | Manage complex state logic      |
| Custom Hooks        | Reuse logic                     |
| useLayoutEffect     | Synchronous DOM updates         |
| useImperativeHandle | Control ref behavior            |
| useId               | Generate unique IDs             |
| useTransition       | Smooth transitions              |
| useDeferredValue    | Delay rendering heavy values    |
| useDebugValue       | Debug custom hooks              |

React Hooks simplify React’s structure by eliminating the need for class components while keeping the logic powerful and reusable.

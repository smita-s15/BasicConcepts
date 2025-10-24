## Step 3: Component Lifecycle

React components go through a **lifecycle**, which is a series of phases from creation to removal. Understanding these phases is crucial, especially when working with **class components**, **hooks**, and performing tasks like API calls, timers, and subscriptions.

---

# 1. Lifecycle Phases in Class Components

A class component in React has **three main lifecycle phases**:

1. **Mounting** – When the component is being created and inserted into the DOM.
2. **Updating** – When the component is re-rendered due to changes in **state** or **props**.
3. **Unmounting** – When the component is removed from the DOM.

---

# 2. Lifecycle Methods

Class components have **specific methods** corresponding to these phases.

### 2.1 Mounting

These methods are called when the component is **first rendered**:

- **constructor(props)**

  - Called first before the component is mounted.
  - Used to initialize state and bind methods.

  ```jsx
  constructor(props) {
    super(props);
    this.state = { count: 0 };
  }
  ```

- **render()**

  - Required method.
  - Returns JSX to render the component UI.
  - Should **not** modify state or interact with the DOM directly.

  ```jsx
  render() {
    return <h1>{this.state.count}</h1>;
  }
  ```

- **componentDidMount()**

  - Called after the component is mounted in the DOM.
  - Ideal for **API calls**, **timers**, or **subscriptions**.

  ```jsx
  componentDidMount() {
    fetch("https://api.example.com/data")
      .then(res => res.json())
      .then(data => this.setState({ data }));
  }
  ```

---

### 2.2 Updating

These methods are called when a component **re-renders** due to **state or props changes**:

- **shouldComponentUpdate(nextProps, nextState)**

  - Determines if the component should re-render.
  - Returns `true` (default) or `false`.
  - Useful for **performance optimization**.

  ```jsx
  shouldComponentUpdate(nextProps, nextState) {
    return nextState.count !== this.state.count;
  }
  ```

- **componentDidUpdate(prevProps, prevState)**

  - Called after the component updates.
  - Used for **network requests** when props/state change or **DOM updates**.

  ```jsx
  componentDidUpdate(prevProps, prevState) {
    if(prevState.count !== this.state.count){
      console.log("Count updated!");
    }
  }
  ```

- **render()**

  - Called again during updating to render new UI.

---

### 2.3 Unmounting

- **componentWillUnmount()**

  - Called before the component is removed from the DOM.
  - Used to **clean up timers, subscriptions, or event listeners**.

  ```jsx
  componentWillUnmount() {
    clearInterval(this.timer);
  }
  ```

---

# 3. Mapping Class Lifecycle to Hooks

React **hooks** provide functional component alternatives to class lifecycle methods:

| Class Lifecycle Method | Hook Equivalent                         | Notes                                        |
| ---------------------- | --------------------------------------- | -------------------------------------------- |
| constructor            | useState                                | Initialize state                             |
| componentDidMount      | useEffect(() => {}, [])                 | Empty dependency array runs once after mount |
| componentDidUpdate     | useEffect(() => {}, [deps])             | Runs when dependencies change                |
| componentWillUnmount   | useEffect(() => { return cleanup }, []) | Cleanup function runs before unmounting      |
| shouldComponentUpdate  | React.memo / useMemo / useCallback      | Optimize rendering for props/state changes   |

**Example using Hooks**:

```jsx
import React, { useState, useEffect } from "react";

function Timer() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    const interval = setInterval(() => setCount((c) => c + 1), 1000);
    return () => clearInterval(interval); // cleanup
  }, []);

  return <h1>{count}</h1>;
}
```

---

# 4. API Calls in Lifecycle Methods

- **Class Components**: Use `componentDidMount` to fetch data.
- **Functional Components**: Use `useEffect` with empty dependency array.
- **Best Practices**:

  - Handle errors with `try/catch`.
  - Cancel requests on unmount to avoid memory leaks.

```jsx
useEffect(() => {
  const controller = new AbortController();
  fetch(url, { signal: controller.signal })
    .then((res) => res.json())
    .then(setData)
    .catch((err) => {
      if (err.name !== "AbortError") console.error(err);
    });
  return () => controller.abort();
}, []);
```

---

# 5. Timers and Subscriptions Cleanup

- Always **clear timers** (`setInterval`, `setTimeout`) in `componentWillUnmount` or cleanup function in `useEffect`.
- Unsubscribe from **event listeners** or **WebSocket subscriptions** to prevent memory leaks.

```jsx
useEffect(() => {
  const interval = setInterval(() => console.log("tick"), 1000);
  window.addEventListener("resize", handleResize);

  return () => {
    clearInterval(interval);
    window.removeEventListener("resize", handleResize);
  };
}, []);
```

---

**Key Takeaways:**

- `render()` is the only **required** lifecycle method in class components.
- Use **hooks** in functional components for lifecycle management.
- Always **clean up side effects** like timers and subscriptions.
- Lifecycle knowledge is essential for **performance optimization** and **avoiding bugs**.

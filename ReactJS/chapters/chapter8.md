## Step 8: Advanced Topics

Advanced React concepts help in building **highly performant**, **scalable**, and **maintainable** applications.

---

# 1. SSR vs SSG vs CSR

- **CSR (Client-Side Rendering)**: Entire rendering done on the client.
- **SSR (Server-Side Rendering)**: HTML rendered on the server, faster initial load.
- **SSG (Static Site Generation)**: Pages pre-rendered at build time, served as static files.

**Use Cases:**

- SSR: Dynamic pages requiring SEO.
- SSG: Static content, blogs, landing pages.
- CSR: Single-page apps with heavy interactivity.

---

# 2. Hydration & Rehydration

- **Hydration**: React attaches event listeners to server-rendered HTML.
- **Rehydration**: Updates server-rendered HTML to be fully interactive.
- Ensures SSR/SSG pages work like normal React apps on the client.

---

# 3. Higher Order Components (HOCs)

- HOC is a function that **takes a component and returns a new component**.
- Used for code reuse, conditional rendering, or injecting props.

```jsx
function withAuth(Component) {
  return function Wrapped(props) {
    const isAuth = checkAuth();
    return isAuth ? <Component {...props} /> : <Redirect to="/login" />;
  };
}
```

---

# 4. Render Props Pattern

- Technique where a component **accepts a function as a prop** to determine what to render.

```jsx
function DataProvider({ render }) {
  const data = fetchData();
  return render(data);
}
<DataProvider render={(data) => <div>{data}</div>} />;
```

---

# 5. Controlled vs Uncontrolled Components

- **Controlled**: React state drives input values.

  ```jsx
  const [value, setValue] = useState("");
  <input value={value} onChange={(e) => setValue(e.target.value)} />;
  ```

- **Uncontrolled**: Input manages its own state.

  ```jsx
  <input defaultValue="Hello" ref={inputRef} />
  ```

---

# 6. React Fiber Architecture

- **Fiber**: Rewritten React core for **incremental rendering**.
- Breaks rendering work into units to keep app **responsive**.
- Enables **Concurrent Mode** and **prioritized updates**.

---

# 7. Portals

- Render children **outside the parent DOM hierarchy**.
- Useful for modals, tooltips, or overlays.

```jsx
ReactDOM.createPortal(<Modal />, document.getElementById("modal-root"));
```

---

# 8. Concurrent Mode (Experimental)

- Allows React to **interrupt rendering** for high-priority updates.
- Improves responsiveness for large apps.
- Still experimental; use cautiously.

---

# 9. Suspense for Data Fetching

- Enables components to **wait for async data** before rendering.
- Works with **React.lazy** and concurrent rendering libraries.

```jsx
<Suspense fallback={<Loader />}>
  <LazyComponent />
</Suspense>
```

---

# 10. Error Boundaries

- Components that **catch JavaScript errors** in their child components.
- Prevents the entire app from crashing.

```jsx
class ErrorBoundary extends React.Component {
  state = { hasError: false };
  static getDerivedStateFromError() {
    return { hasError: true };
  }
  render() {
    return this.state.hasError ? (
      <h1>Something went wrong</h1>
    ) : (
      this.props.children
    );
  }
}
```

---

# 11. Context vs Redux for Advanced State Management

- **Context**: Best for medium-level global state, simpler use.
- **Redux**: Best for large-scale apps, complex state, predictable updates.
- Decision depends on **app complexity** and **team preference**.

---

# 12. React Profiler API

- Measures **rendering performance** of components.
- Useful for identifying **performance bottlenecks**.

```jsx
<Profiler
  id="App"
  onRender={(id, phase, actualDuration) =>
    console.log({ id, phase, actualDuration })
  }
>
  <App />
</Profiler>
```

---

**Key Takeaways:**

- Advanced topics enhance **performance, scalability, and maintainability**.
- Understand when to use SSR/SSG/CSR.
- Use HOCs, Render Props, and Portals for reusable and modular code.
- Leverage Profiler API and Suspense for optimizing UX and performance.

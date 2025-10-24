## Step 5: Performance Optimization

Optimizing performance in React is essential for building fast, responsive applications, especially as apps grow in size and complexity.

---

# 1. Reconciliation (Virtual DOM Diffing)

- React uses a **Virtual DOM** to efficiently update the UI.
- **Reconciliation** is the process of comparing the new Virtual DOM with the previous one and updating only the changed parts.
- Minimizes **direct DOM manipulations**, improving performance.

**Example:**

```jsx
// Only changed components will re-render based on Virtual DOM diffing
```

---

# 2. Keys in Lists

- Keys help React **identify which items changed, added, or removed**.
- Always use **unique and stable keys** (avoid indexes unless the list is static).

```jsx
{
  items.map((item) => <li key={item.id}>{item.name}</li>);
}
```

**Best Practices:**

- Use unique IDs if available.
- Avoid using array index if the list can change.
- Keys must be **stable across renders**.

---

# 3. Memoization Techniques

Memoization helps **prevent unnecessary re-renders** by caching values or components.

- **React.memo** – Wraps a component to avoid re-render if props haven't changed.

  ```jsx
  const MemoizedComponent = React.memo(Component);
  ```

- **useMemo** – Memoizes **expensive computations**.

  ```jsx
  const computedValue = useMemo(() => expensiveCalculation(data), [data]);
  ```

- **useCallback** – Memoizes **functions**, preventing re-creation on each render.

  ```jsx
  const handleClick = useCallback(() => {
    console.log(count);
  }, [count]);
  ```

---

# 4. Code Splitting and Lazy Loading

- **Code Splitting** – Breaks code into smaller chunks to **load only what is needed**.
- **React.lazy** – Dynamically imports components.
- **Suspense** – Shows fallback UI while the component loads.

```jsx
const LazyComponent = React.lazy(() => import("./LazyComponent"));

function App() {
  return (
    <Suspense fallback={<div>Loading...</div>}>
      <LazyComponent />
    </Suspense>
  );
}
```

---

# 5. Avoiding Unnecessary Re-renders

- **Use memoization** (`React.memo`, `useMemo`, `useCallback`).
- **Split components** to isolate frequently changing parts.
- **Avoid anonymous functions** or object literals in props.
- **Use state wisely**, only where necessary.

---

# 6. Performance Profiling

- **React DevTools Profiler** helps measure **rendering performance**.
- Detects components that render **too often** or **take too long**.
- Provides **flame graphs** and **commit timings**.

---

# 7. SSR (Server-Side Rendering) & SSG (Static Site Generation)

- **SSR**: Renders React components on the server for faster **first contentful paint (FCP)**.
- **SSG**: Pre-renders pages at **build time**, serving static HTML.
- Popular in **Next.js** for SEO and performance.

```jsx
// SSR: getServerSideProps in Next.js
// SSG: getStaticProps in Next.js
```

---

# 8. Hydration and Rehydration

- **Hydration**: React attaches event listeners to **server-rendered HTML**.
- **Rehydration**: Updates server-rendered content with client-side interactivity.
- Ensures **SSR/SSG pages are interactive** after loading.

---

**Key Takeaways:**

- Use keys, memoization, and lazy loading to optimize rendering.
- Profile performance regularly with React DevTools.
- Leverage SSR/SSG and proper hydration for fast, SEO-friendly pages.
- Avoid unnecessary state changes and re-renders to maintain a snappy UI.

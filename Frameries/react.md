# React Key Concepts & Advanced Topics

## 1. Components

- Building blocks of UI: Functional or Class-based.
- Return JSX to describe UI.

## 2. JSX

- JavaScript XML syntax mixing HTML-like code with JS.
- Compiled to `React.createElement`.

## 3. Props

- Read-only inputs from parent to child.
- Customize components.

## 4. State

- Internal, mutable data within components.
- Changes trigger re-renders.

## 5. Lifecycle Methods (Class Components)

- `componentDidMount`, `componentDidUpdate`, `componentWillUnmount`.
- Manage side effects and resources.

## 6. Hooks (Functional Components)

- React 16.8+ feature for state & lifecycle in functions.
- Common hooks:
  - `useState` — state management.
  - `useEffect` — side effects & lifecycle.
  - `useContext` — access context.
  - `useRef` — mutable references.
  - `useCallback` & `useMemo` — performance optimization.

## 7. Event Handling

- Use camelCase (e.g., `onClick`).
- Pass functions as handlers.

## 8. Conditional Rendering

- Render UI based on conditions (`if`, `&&`, ternary).

## 9. Lists & Keys

- Render lists with `.map()`.
- Use unique keys for list items to optimize rendering.

## 10. Context API

- Global state management without prop drilling.

## 11. React Router

- SPA routing with `<BrowserRouter>`, `<Route>`, `<Link>`.

## 12. Controlled vs Uncontrolled Components

- Controlled: React state controls input.
- Uncontrolled: DOM manages input.

## 13. Error Boundaries (Class Components)

- Catch JS errors and show fallback UI.
- Use `componentDidCatch` and `getDerivedStateFromError`.

## 14. Higher-Order Components (HOC)

- Functions returning enhanced components for code reuse.

## 15. React.memo

- Memoizes components to avoid unnecessary re-renders.

## 16. React Suspense & Lazy Loading

- Code splitting with `React.lazy()` and fallback UI via `Suspense`.

## 17. Portals

- Render outside parent DOM hierarchy (useful for modals/tooltips).

## 18. Forwarding Refs

- Pass refs to child components via `React.forwardRef`.

## 19. PropTypes & TypeScript

- `PropTypes` for runtime prop validation.
- TypeScript for static typing and better tooling.

## 20. State Management Options

- Local: hooks (`useState`, `useReducer`).
- Global: Context API, Redux, MobX, Recoil, Zustand.

## 21. Testing

- Unit: Jest + React Testing Library.
- Snapshot testing.
- E2E: Cypress, Selenium.

---

# Code Examples

### Functional Component with `useState`

```jsx
import React, { useState } from "react";

function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
}

export default Counter;


# Difference Between React and Next.js

| Feature                  | React                                   | Next.js                                       |
|--------------------------|----------------------------------------|-----------------------------------------------|
| **Type**                 | JavaScript library for building UIs   | React framework with additional features      |
| **Rendering**            | Client-Side Rendering (CSR)             | Supports SSR, SSG, ISR, and CSR                |
| **Routing**              | Manual setup with libraries like React Router | File-based automatic routing system           |
| **Data Fetching**        | Client-side only (usually with hooks) | Supports server-side data fetching (`getStaticProps`, `getServerSideProps`) and client-side fetching |
| **SEO**                  | Requires extra setup for SEO           | Built-in SEO support via SSR and SSG           |
| **Performance**          | Depends on CSR                         | Optimized with pre-rendering and code splitting |
| **API Handling**         | Separate backend or API service needed | Built-in API routes inside `/pages/api` folder |
| **File Structure**       | Flexible project structure             | Opinionated file-based routing in `/pages` folder |
| **Deployment**           | Deploy client-only apps                 | Deploy full-stack apps with serverless functions support |
| **Image Optimization**   | Needs manual implementation            | Built-in optimized `<Image />` component       |
| **Learning Curve**       | Simpler, focuses on UI only             | More features, steeper but powerful             |
| **Use Cases**            | Single-page applications (SPAs)        | Static sites, SSR apps, hybrid apps              |

---

# Summary

- **React** is a UI library focused on building components and client-side apps.
- **Next.js** is a React framework adding SSR, SSG, routing, API, and optimizations out of the box.
- Choose React for pure frontend SPA.
- Choose Next.js for SEO-friendly, scalable, and performant React applications with backend capabilities.


```

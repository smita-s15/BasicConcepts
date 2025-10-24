# React.js Interview Questions & Answers

A comprehensive guide for React.js interviews, covering basics to advanced concepts.

---

## 1. Basic React Concepts

**Q1: What is React and why is it used?**

- React is a JavaScript library for building user interfaces, primarily for single-page applications. It allows efficient UI updates using a virtual DOM.

**Q2: What are components in React?**

- Components are reusable, self-contained building blocks of UI.

**Q3: Difference between functional and class components?**

- Functional: Stateless, uses hooks.
- Class: Stateful, uses lifecycle methods.

**Q4: What is JSX?**

- JSX is a syntax extension that allows writing HTML-like code in JavaScript.

**Q5: Why can’t browsers read JSX directly?**

- Browsers understand JavaScript, not JSX. It needs to be transpiled to JS using Babel.

**Q6: What are props?**

- Props are read-only inputs passed to components.

**Q7: What is state?**

- State is a mutable object that determines component behavior and rendering.

**Q8: Difference between props and state?**

- Props: Read-only, passed from parent.
- State: Mutable, managed within component.

**Q9: What is Virtual DOM?**

- Virtual DOM is a lightweight copy of the real DOM that React uses to optimize updates.

**Q10: Explain React’s rendering process.**

- React compares new virtual DOM with old one (diffing) and updates only changed parts in real DOM.

---

## 2. React Hooks

**Q1: What are React Hooks?**

- Hooks allow using state and lifecycle features in functional components.

**Q2: Difference between useState and useEffect?**

- useState: Manages state.
- useEffect: Handles side effects like API calls.

**Q3: When does useEffect run?**

- By default, after every render; can be controlled using dependencies.

**Q4: How do you prevent useEffect from running on every render?**

- By providing a dependency array.

**Q5: What is the cleanup function in useEffect?**

- Runs before the next effect or unmounting to clean subscriptions/timers.

**Q6: What is useRef?**

- Provides a mutable reference to a DOM element or value that persists across renders.

**Q7: Difference between useMemo and useCallback?**

- useMemo: Memoizes a value.
- useCallback: Memoizes a function.

**Q8: What is useContext?**

- Accesses data from React Context without prop drilling.

**Q9: How to create custom hooks?**

- Functions starting with `use` that encapsulate reusable logic.

**Q10: Why do we use custom hooks?**

- To reuse stateful logic across multiple components.

---

## 3. Component Lifecycle

**Q1: Lifecycle methods in class components?**

- Mounting: constructor, render, componentDidMount
- Updating: shouldComponentUpdate, render, componentDidUpdate
- Unmounting: componentWillUnmount

**Q2: How lifecycle maps to hooks?**

- Mounting: useEffect([])
- Updating: useEffect([deps])
- Unmounting: cleanup function in useEffect

**Q3: How to perform API calls?**

- In functional components: useEffect with fetch/axios.
- In class components: componentDidMount.

---

## 4. State Management

**Q1: What is lifting state up?**

- Moving shared state to the closest common ancestor to share data.

**Q2: What is prop drilling?**

- Passing props through multiple layers unnecessarily.

**Q3: How to avoid prop drilling?**

- Use Context API or state management libraries.

**Q4: Explain Context API.**

- Provides global state accessible anywhere in component tree.

**Q5: Alternatives to Context API?**

- Redux, Zustand, Recoil.

**Q6: What is Redux?**

- Predictable state container for JS apps.

**Q7: Explain actions, reducers, and store.**

- Action: describes what happened.
- Reducer: updates state based on action.
- Store: holds the global state.

**Q8: Difference between Redux and Context API?**

- Redux: structured, scalable, middleware support.
- Context: simple, lightweight, for small apps.

**Q9: What is Redux Toolkit?**

- Simplifies Redux setup with default best practices.

**Q10: How to debug Redux?**

- Using Redux DevTools.

---

## 5. Performance Optimization

**Q1: What is reconciliation?**

- Process React uses to update the DOM efficiently.

**Q2: What are keys and why important?**

- Unique identifiers for elements in lists; help React track changes.

**Q3: Why avoid index as key?**

- Can cause incorrect rendering when items reorder.

**Q4: What causes re-renders?**

- State or props changes.

**Q5: How to prevent unnecessary re-renders?**

- Use React.memo, useCallback, useMemo.

**Q6: What is memoization?**

- Caching results to avoid recomputation.

**Q7: What is React.memo()?**

- HOC that memoizes functional components.

**Q8: What is code-splitting?**

- Loading parts of app only when needed to improve performance.

**Q9: React.lazy and Suspense?**

- Lazy: dynamically import components.
- Suspense: handles loading fallback.

**Q10: What is hydration?**

- Attaching event listeners to server-rendered HTML.

---

## 6. React with APIs

**Q1: How to fetch data?**

- Use fetch or axios inside useEffect/componentDidMount.

**Q2: Difference fetch vs axios?**

- axios supports older browsers, interceptors, automatic JSON parsing.

**Q3: Handle loading & error states?**

- Maintain `loading` and `error` in state.

**Q4: Cancel a request?**

- Using AbortController with fetch or cancel token in axios.

**Q5: Handle pagination/infinite scroll?**

- Fetch data in chunks and append to state on scroll event.

---

## 7. React Router

**Q1: What is React Router?**

- Library for routing in React apps.

**Q2: Difference Link vs a tag?**

- Link: prevents full page reload, uses history API.
- a: reloads page.

**Q3: useNavigate/useHistory?**

- Hooks to programmatically navigate routes.

**Q4: Pass parameters in routes?**

- Use URL params (`/user/:id`) and `useParams` hook.

**Q5: Protect routes?**

- PrivateRoute component checking auth.

**Q6: Nested routing?**

- Routes inside routes to create sub-pages.

**Q7: Handle 404?**

- Add a wildcard route (`*`) pointing to NotFound component.

---

## 8. Advanced Topics

**Q1: What is SSR?**

- Rendering on server to improve SEO and initial load.

**Q2: What is SSG?**

- Pre-render pages at build time.

**Q3: Hydration & rehydration?**

- Process of attaching React to server-rendered HTML.

**Q4: Higher Order Components?**

- Functions that take a component and return a new enhanced component.

**Q5: Render Props?**

- Component that passes a function as prop to share code.

**Q6: Controlled vs uncontrolled components?**

- Controlled: state-driven form inputs.
- Uncontrolled: refs manage input values.

**Q7: React Fiber architecture?**

- New reconciliation algorithm improving async rendering.

**Q8: Portals?**

- Render children into DOM node outside parent hierarchy.

**Q9: Concurrent Mode?**

- Enables interruptible rendering for better UX.

**Q10: Suspense for data fetching?**

- Allows waiting for async data before rendering.

---

## 9. Testing in React

**Q1: Jest?**

- JavaScript testing framework.

**Q2: React Testing Library?**

- Testing library to test React components focusing on behavior.

**Q3: Test component with props?**

- Render with props and assert output.

**Q4: Test async code/API calls?**

- Use async/await and mock API responses.

**Q5: Unit vs integration test?**

- Unit: test a single function/component.
- Integration: test multiple units together.

---

## 10. Practical/Scenario-based Questions

**Q1: Handle forms efficiently?**

- Use controlled components or libraries like Formik/React Hook Form.

**Q2: Optimize large list rendering?**

- Use virtualization libraries like react-window/react-virtualized.

**Q3: Persist state after refresh?**

- Use localStorage or sessionStorage.

**Q4: Manage dark/light theme?**

- Use context + CSS variables or libraries like styled-components.

**Q5: Build reusable modal component?**

- Controlled via props; use portals for rendering.

**Q6: Handle errors globally?**

- Use Error Boundaries.

**Q7: Authentication in React?**

- JWT, Context/Redux for storing auth state, private routes.

**Q8: Structure large React project?**

- Feature-based folders, components, services, utils.

**Q9: Manage environment variables?**

- Use `.env` files and `process.env`.

**Q10: Debug React apps?**

- React DevTools, console logs, breakpoints, Redux DevTools.

# Step 1: React Basics

## 1. Introduction to React

React is a **JavaScript library** developed by Facebook for building **user interfaces (UIs)**, especially for **single-page applications (SPAs)**. It helps developers create large web applications that can update and render efficiently without reloading the page.

React uses a **component-based architecture**, allowing you to break down the UI into reusable pieces.

### Key Concepts

- **Declarative:** Describe what the UI should look like for a given state.
- **Component-Based:** Build encapsulated components that manage their own state.
- **Learn Once, Write Anywhere:** Can be used for web (React DOM), mobile (React Native), or even desktop apps.

---

## 2. Features of React

- **JSX (JavaScript XML):** Combines HTML with JavaScript logic.
- **Virtual DOM:** Efficiently updates only the parts of the UI that change.
- **Unidirectional Data Flow:** Data flows in one direction (parent → child).
- **Component-Based Architecture:** Encourages reusable and modular code.
- **Declarative UI:** React updates the UI automatically when data changes.
- **Strong Community Support:** Backed by Meta (Facebook) and open-source developers.

---

## 3. Why React is Used

- Increases **development speed** using reusable components.
- **Improves performance** with Virtual DOM.
- Easier **debugging** and **testing** using tools like React DevTools.
- **SEO-friendly** when used with Next.js or server-side rendering.
- Easy to integrate with other frameworks/libraries.

---

## 4. JSX Syntax and Rules

JSX allows writing HTML-like syntax directly inside JavaScript.

### Example:

```jsx
const element = <h1>Hello, React!</h1>;
```

### JSX Rules:

1. Must return a **single root element**.
2. Use **className** instead of `class`.
3. Use **camelCase** for attributes (e.g., `onClick`, `tabIndex`).
4. JavaScript expressions go inside **{}**.
5. JSX must be **compiled using Babel** to plain JS.

---

## 5. Components (Functional & Class)

### Functional Component (Preferred in Modern React)

```jsx
function Welcome(props) {
  return <h1>Hello, {props.name}</h1>;
}
```

Or using ES6 arrow function:

```jsx
const Welcome = ({ name }) => <h1>Hello, {name}</h1>;
```

### Class Component (Older Approach)

```jsx
class Welcome extends React.Component {
  render() {
    return <h1>Hello, {this.props.name}</h1>;
  }
}
```

---

## 6. Props (Passing Data, Default Props, Prop Types)

**Props** are short for “properties” — used to pass data from parent to child components.

### Example:

```jsx
function User(props) {
  return <p>Welcome, {props.name}</p>;
}
<User name="Smita" />;
```

### Default Props

```jsx
User.defaultProps = {
  name: "Guest",
};
```

### PropTypes (Type Checking)

```jsx
import PropTypes from "prop-types";

User.propTypes = {
  name: PropTypes.string,
};
```

---

## 7. State (setState, useState)

**State** stores dynamic data that changes over time.

### Using Class Component:

```jsx
class Counter extends React.Component {
  constructor() {
    super();
    this.state = { count: 0 };
  }

  increment = () => {
    this.setState({ count: this.state.count + 1 });
  };

  render() {
    return <button onClick={this.increment}>Count: {this.state.count}</button>;
  }
}
```

### Using Functional Component with useState:

```jsx
import { useState } from "react";

function Counter() {
  const [count, setCount] = useState(0);
  return <button onClick={() => setCount(count + 1)}>Count: {count}</button>;
}
```

---

## 8. Virtual DOM & Real DOM

| Feature     | Virtual DOM             | Real DOM                    |
| ----------- | ----------------------- | --------------------------- |
| Speed       | Fast                    | Slow                        |
| Update      | Updates in memory first | Updates actual DOM directly |
| Performance | Efficient               | Less efficient              |
| Re-render   | Partial updates         | Full updates                |

React creates a **Virtual DOM** copy in memory. When state changes, React compares it (via **diffing**) and updates only the changed parts in the real DOM.

---

## 9. Rendering (Initial and Conditional Rendering)

### Initial Rendering

When the component first loads, React creates and displays the Virtual DOM.

### Conditional Rendering

```jsx
function Greeting({ isLoggedIn }) {
  return (
    <div>{isLoggedIn ? <h1>Welcome Back!</h1> : <h1>Please Login</h1>}</div>
  );
}
```

---

## 10. Event Handling (onClick, onChange, onSubmit)

### Example:

```jsx
function App() {
  const handleClick = () => alert("Button clicked!");
  return <button onClick={handleClick}>Click Me</button>;
}
```

### Form Event Example:

```jsx
function Form() {
  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("Form submitted!");
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="text" />
      <button type="submit">Submit</button>
    </form>
  );
}
```

---

## 11. Forms Handling (Controlled & Uncontrolled)

### Controlled Component:

```jsx
function ControlledInput() {
  const [value, setValue] = useState("");
  return <input value={value} onChange={(e) => setValue(e.target.value)} />;
}
```

### Uncontrolled Component:

```jsx
function UncontrolledInput() {
  const inputRef = useRef();
  const handleSubmit = () => alert(inputRef.current.value);

  return (
    <>
      <input ref={inputRef} />
      <button onClick={handleSubmit}>Show Value</button>
    </>
  );
}
```

---

## 12. Lists and Keys

Used for rendering multiple elements dynamically.

### Example:

```jsx
function List() {
  const items = ["Apple", "Banana", "Cherry"];
  return (
    <ul>
      {items.map((item, index) => (
        <li key={index}>{item}</li>
      ))}
    </ul>
  );
}
```

Keys help React identify which items changed or were removed for efficient rendering.

---

## 13. Styling in React

### 1. Inline Styling

```jsx
const style = { color: "blue", fontSize: "20px" };
<h1 style={style}>Hello!</h1>;
```

### 2. CSS Modules

```css
/* App.module.css */
.title {
  color: red;
}
```

```jsx
import styles from "./App.module.css";
<h1 className={styles.title}>Styled with CSS Module</h1>;
```

### 3. Styled Components

```bash
npm install styled-components
```

```jsx
import styled from "styled-components";

const Button = styled.button`
  background-color: teal;
  color: white;
  padding: 10px;
`;

<Button>Click Me</Button>;
```

---

### ✅ Summary

React Basics give you the foundation to build dynamic, modular, and scalable UI components efficiently. Understanding JSX, Components, Props, State, and Rendering is essential before diving into advanced topics like Hooks, Context API, and Routing.

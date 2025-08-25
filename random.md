# Key Concepts: REST APIs, Microservices, AI Tools, DSA, SQL & Databases

---

## 1. REST APIs

- **REST (Representational State Transfer)** is an architectural style for designing networked applications.
- Uses HTTP methods: `GET`, `POST`, `PUT`, `DELETE`.
- Resources are identified by URLs (endpoints).
- Stateless communication: each request contains all necessary info.
- Uses JSON or XML for data exchange.
- Key principles: Uniform Interface, Statelessness, Cacheability, Layered System.

---

## 2. Microservices

- Architectural style that structures an application as a collection of small, loosely coupled services.
- Each microservice focuses on a single business capability.
- Services communicate over network protocols (usually HTTP/REST or messaging).
- Benefits: Scalability, Flexibility, Independent Deployment, Fault Isolation.
- Challenges: Complexity, Distributed system management, Data consistency.

---

## 3. AI Tools Experience

- **Copilot**: AI-powered code completion tool by GitHub.
- **Cursor AI**: AI assistant for code understanding and generation.
- Benefits: Boost productivity, code suggestions, error reduction.
- Usage: Integrated into IDEs to help write and refactor code faster.

---

## 4. Strong Data Structures & Algorithms (DSA) Skills

- Core for efficient problem-solving and coding interviews.
- Key topics:
  - Arrays, Linked Lists, Stacks, Queues
  - Trees, Graphs
  - Sorting & Searching algorithms
  - Recursion, Dynamic Programming, Greedy algorithms
- Helps write optimized code with better time and space complexity.

---

## 5. SQL & Database Skills

- **SQL** (Structured Query Language) for managing relational databases.
- Core concepts:
  - Data querying: `SELECT`, `WHERE`, `JOIN`, `GROUP BY`
  - Data manipulation: `INSERT`, `UPDATE`, `DELETE`
  - Schema management: `CREATE`, `ALTER`, `DROP`
  - Constraints and indexing for data integrity and performance.
- Database types:
  - Relational (e.g., MySQL, PostgreSQL)
  - NoSQL (e.g., MongoDB, Cassandra)

---

# Summary

Mastering REST APIs and Microservices enables building scalable backend systems. Leveraging AI tools accelerates development. Strong DSA and SQL knowledge ensures writing efficient and reliable code, fundamental for high-quality software engineering.

# Frontend Interview Preparation Checklist with Explanations

---

## 1. HTML & CSS

- **Difference between inline, block, and inline-block elements**  
  Inline elements do not start on a new line and only take up as much width as necessary (e.g., `<span>`). Block elements start on a new line and take up the full width available (e.g., `<div>`). Inline-block elements behave like inline elements but allow setting width and height.

- **CSS specificity rules**  
  Determines which CSS rule applies when multiple rules target the same element. Inline styles have highest specificity, followed by IDs, classes, and then element selectors.

- **Flexbox vs Grid layout**  
  Flexbox is one-dimensional (row or column) layout system ideal for distributing space along a single axis. Grid is two-dimensional and more powerful for designing complex layouts involving rows and columns.

- **Semantic HTML**  
  Using HTML elements according to their meaning (e.g., `<header>`, `<article>`, `<footer>`) rather than generic tags like `<div>`. Improves accessibility and SEO.

---

## 2. JavaScript

- **var, let, and const differences**  
  `var` is function-scoped and hoisted; `let` and `const` are block-scoped with `const` being read-only after initialization.

- **Event delegation**  
  Technique to handle events at a parent level rather than attaching listeners to many child elements, improving performance.

- **Closures and scope**  
  Closures occur when a function remembers the variables from its lexical scope even when executed outside that scope. Important for data privacy and functional patterns.

- **Promises vs async/await**  
  Promises represent future results of async operations. `async/await` syntax makes async code easier to read and write by handling Promises more cleanly.

- **Debouncing and throttling**  
  Techniques to control how often a function executes: debouncing delays execution until a pause in events, throttling limits execution to once every set interval.

---

## 3. React

- **Functional vs Class components**  
  Functional components are simpler and use hooks, while class components use lifecycle methods and `this` keyword.

- **State vs Props**  
  State is local and mutable data managed within a component. Props are read-only data passed from parent to child components.

- **useEffect and dependency arrays**  
  `useEffect` runs side-effects in functional components. Dependency arrays control when the effect runs (on mount, update, or unmount).

- **React reconciliation & Virtual DOM**  
  React efficiently updates the UI by comparing a virtual DOM tree to the real DOM and only applying necessary changes.

- **Lifting state up**  
  Moving shared state to a common ancestor component to allow multiple child components to access and update it.

---

## 4. Performance & Optimization

- **Lazy loading & code splitting**  
  Loading parts of the application only when needed to reduce initial load time.

- **Memoization in React**  
  Techniques (`React.memo`, `useMemo`) to prevent unnecessary re-rendering by caching expensive calculations or components.

- **Reducing re-renders**  
  Strategies to optimize React app performance by avoiding unnecessary component updates.

---

## 5. Web Fundamentals

- **How browsers render a page**  
  Understanding parsing HTML into DOM, CSSOM, constructing render tree, layout, and painting.

- **CORS (Cross-Origin Resource Sharing)**  
  Browser security feature that restricts web pages from making requests to a different domain unless allowed by the server.

- **HTTP methods & status codes**  
  Common HTTP methods: GET, POST, PUT, DELETE. Status codes indicate response status, e.g., 200 (OK), 404 (Not Found), 500 (Server Error).

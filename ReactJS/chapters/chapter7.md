## Step 7: React Router

React Router is the standard library for routing in React, enabling navigation and URL management in single-page applications.

---

# 1. Basics of Routing

- Use `react-router-dom` for web applications.
- Wrap your app with `BrowserRouter`.
- Define routes using the `Routes` and `Route` components.

```jsx
import { BrowserRouter, Routes, Route } from "react-router-dom";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
      </Routes>
    </BrowserRouter>
  );
}
```

---

# 2. Route Components, Link vs Anchor Tag

- **Link**: Client-side navigation without page reload.
- **Anchor `<a>` tag**: Causes full page reload.

```jsx
<Link to='/about'>About</Link>
<a href='/about'>About</a> // Not recommended
```

- **Route Components**: Components rendered based on the path.

---

# 3. useNavigate / useHistory

- **useNavigate** (v6) replaces `useHistory`.
- Used for programmatic navigation.

```jsx
import { useNavigate } from "react-router-dom";
function Component() {
  const navigate = useNavigate();
  return <button onClick={() => navigate("/about")}>Go to About</button>;
}
```

---

# 4. Route Parameters and Query Parameters

- **Route Parameters**: Dynamic segments in URL.

```jsx
<Route path="/user/:id" element={<User />} />
```

```jsx
import { useParams } from "react-router-dom";
function User() {
  const { id } = useParams();
  return <div>User ID: {id}</div>;
}
```

- **Query Parameters**: Access using `useLocation`.

```jsx
import { useLocation } from "react-router-dom";
function Component() {
  const query = new URLSearchParams(useLocation().search);
  const name = query.get("name");
  return <div>Name: {name}</div>;
}
```

---

# 5. Nested Routes

- Nested routes allow rendering child components inside parent routes.

```jsx
<Route path="/dashboard" element={<Dashboard />}>
  <Route path="stats" element={<Stats />} />
  <Route path="settings" element={<Settings />} />
</Route>
```

- Use `<Outlet />` in parent to render child routes.

---

# 6. Protected Routes / Private Routes

- Restrict access based on authentication.

```jsx
function PrivateRoute({ children }) {
  const isAuth = // check auth;
  return isAuth ? children : <Navigate to='/login' />;
}
```

```jsx
<Route
  path="/profile"
  element={
    <PrivateRoute>
      <Profile />
    </PrivateRoute>
  }
/>
```

---

# 7. Redirects

- **Redirect** in v6 uses `<Navigate>`.

```jsx
<Route path="/old" element={<Navigate to="/new" />} />
```

---

# 8. 404 / Not Found Handling

- Define a catch-all route for undefined paths.

```jsx
<Route path="*" element={<NotFound />} />
```

---

# 9. Route Transition Animations (Optional)

- Use libraries like **Framer Motion** for smooth transitions.

```jsx
import { motion } from "framer-motion";
<motion.div
  initial={{ opacity: 0 }}
  animate={{ opacity: 1 }}
  exit={{ opacity: 0 }}
>
  Content
</motion.div>;
```

---

**Key Takeaways:**

- Use **Link** for client-side navigation.
- Use **useNavigate** for programmatic navigation.
- Handle **dynamic URLs** with route parameters and query parameters.
- Implement **nested, protected, and 404 routes** for robust routing.
- Optional: Add **animations** for better UX.

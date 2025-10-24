## Step 10: Practical / Scenario-Based Topics

This section focuses on real-world scenarios and practical techniques to build scalable, maintainable, and optimized React applications.

---

# 1. Form Handling with Validation

- **React Hook Form**: Lightweight and performant for managing form state.
- **Formik**: Provides schema-based validation with **Yup**.

```jsx
// React Hook Form example
import { useForm } from "react-hook-form";
function MyForm() {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm();
  const onSubmit = (data) => console.log(data);
  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <input {...register("name", { required: true })} />
      {errors.name && <span>Name is required</span>}
      <button type="submit">Submit</button>
    </form>
  );
}
```

---

# 2. Optimizing Large Lists

- Use **react-window** or **react-virtualized** to render only visible items.

```jsx
import { FixedSizeList as List } from "react-window";
<List height={500} itemCount={1000} itemSize={35} width={300}>
  {({ index, style }) => <div style={style}>Item {index}</div>}
</List>;
```

---

# 3. State Persistence

- Store critical state in **localStorage**, **sessionStorage**, or **IndexedDB**.

```jsx
localStorage.setItem("theme", "dark");
const theme = localStorage.getItem("theme");
```

---

# 4. Theme Implementation (Dark / Light Mode)

- Toggle themes using **Context API** or global state.

```jsx
const ThemeContext = React.createContext();
```

---

# 5. Reusable Modal and Dialog Components

- Create a generic modal component.
- Use **Portals** to render outside the DOM hierarchy.

---

# 6. Global Error Handling

- Use **Error Boundaries** to catch component errors.
- Show notifications using **Toasts** for user-friendly error display.

---

# 7. Authentication & Authorization Handling

- Implement **JWT token storage** and refresh logic.
- Protect routes using **PrivateRoute** pattern.

---

# 8. Project Structure and Folder Organization

- Organize components, pages, hooks, utils, and assets in a **modular folder structure**.
- Example:

```
/src
  /components
  /pages
  /hooks
  /utils
  /assets
  App.js
```

---

# 9. Environment Variables in React (.env files)

- Use `.env` files for **API URLs, keys, and config**.
- Variables prefixed with `REACT_APP_` are accessible in React.

```env
REACT_APP_API_URL=https://api.example.com
```

---

# 10. Debugging React Applications

- Use **React DevTools** to inspect component state and props.
- Use **console logs** and **breakpoints** for step-by-step debugging.

---

# 11. Performance Monitoring

- Track **Web Vitals**: LCP, FID, CLS.
- Use **Lighthouse** to audit performance, accessibility, and SEO.

---

# 12. Deployment Best Practices

- Platforms: **Vercel**, **Netlify**, **AWS Amplify**.
- Optimize build: `npm run build`.
- Use environment variables and proper routing for SPA.

---

**Key Takeaways:**

- Focus on **reusable components, efficient state handling, and performance**.
- Implement **robust authentication, error handling, and theme management**.
- Structure projects cleanly and leverage **deployment best practices** for production-ready apps.

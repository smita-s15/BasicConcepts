## Step 6: API Integration

Integrating APIs is essential for React applications to communicate with servers, fetch data, and update UI dynamically.

---

# 1. Fetching Data (fetch, axios)

- **fetch**: Native JavaScript API for HTTP requests.

  ```jsx
  fetch("https://api.example.com/data")
    .then((res) => res.json())
    .then((data) => console.log(data))
    .catch((err) => console.error(err));
  ```

- **axios**: Popular HTTP client with features like interceptors, cancellation, and JSON parsing.

  ```jsx
  import axios from "axios";
  axios
    .get("https://api.example.com/data")
    .then((res) => console.log(res.data))
    .catch((err) => console.error(err));
  ```

---

# 2. Async/Await and Promises

- Use **async/await** for cleaner asynchronous code.

  ```jsx
  async function fetchData() {
    try {
      const res = await fetch("https://api.example.com/data");
      const data = await res.json();
      console.log(data);
    } catch (err) {
      console.error(err);
    }
  }
  ```

- **Promises** are an alternative for handling async operations using `.then` and `.catch`.

---

# 3. Error Handling and Loading States

- Manage **loading** and **error states** to provide feedback to users.

  ```jsx
  const [data, setData] = React.useState(null);
  const [loading, setLoading] = React.useState(true);
  const [error, setError] = React.useState(null);

  useEffect(() => {
    fetch("https://api.example.com/data")
      .then((res) => res.json())
      .then(setData)
      .catch(setError)
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error: {error.message}</p>;
  ```

---

# 4. Canceling Requests (AbortController, Axios CancelToken)

- Prevent memory leaks or outdated responses using **AbortController** or Axios **CancelToken**.

```jsx
// Fetch with AbortController
useEffect(() => {
  const controller = new AbortController();
  fetch("https://api.example.com/data", { signal: controller.signal })
    .then((res) => res.json())
    .then(setData)
    .catch((err) => {
      if (err.name !== "AbortError") console.error(err);
    });
  return () => controller.abort();
}, []);

// Axios CancelToken
const source = axios.CancelToken.source();
axios.get("/api/data", { cancelToken: source.token });
source.cancel("Request canceled");
```

---

# 5. Pagination and Infinite Scroll Implementation

- **Pagination**: Load data in pages.

  ```jsx
  const [page, setPage] = useState(1);
  useEffect(() => {
    axios.get(`/api/data?page=${page}`).then((res) => setData(res.data));
  }, [page]);
  ```

- **Infinite Scroll**: Load more data as the user scrolls.

  ```jsx
  window.addEventListener("scroll", () => {
    if (window.innerHeight + window.scrollY >= document.body.offsetHeight) {
      setPage((prev) => prev + 1);
    }
  });
  ```

---

# 6. Handling Auth Tokens (JWT)

- Store **JWT tokens** securely (preferably in memory or HttpOnly cookies).
- Attach token to headers for API requests.

```jsx
axios.get("/api/protected", { headers: { Authorization: `Bearer ${token}` } });
```

- Handle token expiration with **refresh tokens** or re-login.

---

# 7. Caching and State Management with API Data

- Cache data to **avoid redundant network requests**.
- Integrate with **state management** libraries like Redux, Zustand, or React Query.

```jsx
// Example using React Query
import { useQuery } from "@tanstack/react-query";

function Data() {
  const { data, error, isLoading } = useQuery(["data"], () =>
    fetch("/api/data").then((res) => res.json())
  );
  if (isLoading) return <p>Loading...</p>;
  if (error) return <p>Error!</p>;
  return <div>{JSON.stringify(data)}</div>;
}
```

---

**Key Takeaways:**

- Use async/await for clean asynchronous code.
- Handle loading, errors, and cancellation for better UX.
- Optimize API calls with caching, pagination, and state management.
- Securely handle authentication tokens when calling protected APIs.

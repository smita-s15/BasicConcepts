# Next.js Key Concepts

## 1. What is Next.js?

- React framework for production.
- Supports Server-Side Rendering (SSR), Static Site Generation (SSG), and Client-Side Rendering (CSR).
- Built on top of React with routing and API features.

## 2. File-based Routing

- Pages created in `/pages` folder map to routes automatically.
- Dynamic routes with `[param].js`.
- Catch-all routes with `[...param].js`.

## 3. Pre-rendering

- **Static Generation (SSG):** Pages built at build time, served as static files.
- **Server-Side Rendering (SSR):** Pages generated on each request.
- Choose per-page basis.

## 4. Data Fetching Methods

- `getStaticProps` (SSG): Fetch data at build time.
- `getServerSideProps` (SSR): Fetch data at request time.
- `getStaticPaths`: For dynamic routes with SSG.
- Client-side data fetching (e.g., `useEffect` with fetch).

## 5. API Routes

- Backend functions inside `/pages/api` folder.
- Serverless functions accessible via `/api/*`.
- Handle HTTP methods: GET, POST, etc.

## 6. Image Optimization

- `<Image />` component for optimized images.
- Automatic resizing, lazy loading, and formats.

## 7. Static File Serving

- `/public` folder serves static assets (images, fonts, etc.).
- Accessible via root URL `/`.

## 8. Middleware & Custom Server

- Middleware for request handling.
- Custom server for advanced routing (optional).

## 9. Built-in CSS Support

- Global CSS in `_app.js`.
- CSS Modules for component-level scoped CSS.
- Support for Sass/SCSS and CSS-in-JS libraries.

## 10. API Routes and Middleware

- Write API endpoints directly in Next.js.
- Use middleware to control request flow.

## 11. Incremental Static Regeneration (ISR)

- Update static pages after build without rebuilding entire site.
- Use `revalidate` option in `getStaticProps`.

## 12. Deployment

- Deploy easily on platforms like Vercel.
- Supports serverless and edge functions.

---

# Example: `getStaticProps` for SSG

```jsx
export async function getStaticProps() {
  const res = await fetch("https://api.example.com/data");
  const data = await res.json();

  return {
    props: { data },
    revalidate: 10, // ISR: re-generate at most every 10 seconds
  };
}

function Page({ data }) {
  return <div>{JSON.stringify(data)}</div>;
}

export default Page;

export default function handler(req, res) {
  res.status(200).json({ message: 'Hello from Next.js API!' });
}

```

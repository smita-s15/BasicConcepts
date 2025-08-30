# Scenario-Based Questions and Answers

## 🔹 Frontend (JavaScript)

### Q1: Memory Leak in Single Page Application (SPA)
**Answer:**  
If I notice memory leaks, I’d use Chrome DevTools’ Performance and Memory tabs to track heap snapshots. Common causes are event listeners not removed, timers left running, or large objects in state. I’d fix it by cleaning up listeners in `useEffect` cleanup in React, clearing intervals, and avoiding holding unnecessary references. Once patched, I’d rerun memory profiling to confirm garbage collection works correctly.

---

### Q2: Event Bubbling Issue
**Answer:**  
If a parent click is firing when I only want the child’s action, I’d either call `event.stopPropagation()` in the child handler or restructure the event delegation. Sometimes using event delegation at the parent is intentional, so I’d carefully decide where events should propagate.

---

### Q3: Cross-Browser Compatibility
**Answer:**  
I’d reproduce the issue in the failing browser and check DevTools console for errors. Often it’s unsupported features, so I’d use polyfills or transpilers like Babel. I’d also rely on tools like BrowserStack for testing and follow feature detection (`if ('fetch' in window)`) instead of user-agent checks.

---

### Q4: Slow Rendering in Large Table/Grid
**Answer:**  
I wouldn’t render 10,000 rows at once. Instead, I’d implement virtualization using libraries like React Virtualized or windowing, which only render visible rows. I’d also paginate data and memoize components to reduce unnecessary re-renders. This way, performance improves drastically while still supporting large datasets.

---

### Q5: Security Issue – XSS
**Answer:**  
To prevent XSS, I’d never render raw HTML from user input. Instead, I’d sanitize inputs using libraries like DOMPurify. On the backend, I’d enforce escaping in templates. Also, I’d add a Content Security Policy (CSP) to block inline scripts. That way, even malicious input won’t execute.

---

### Q6: Asynchronous Problem
**Answer:**  
If API calls finish in random order, I’d use `Promise.all` if they’re independent and need to resolve together. If order matters, I’d await each call sequentially. In React, I’d also guard against state updates after unmount to avoid race conditions.

---

### Q7: Debounce/Throttle Requirement
**Answer:**  
For search input firing too many requests, I’d use debounce so the API is only called after the user stops typing for, say, 300ms. For actions like window scroll events, I’d use throttle so the handler only runs at intervals. This reduces server load and improves UX.

---

### Q8: State Management Issue
**Answer:**  
If multiple components aren’t syncing state properly, I’d centralize the state in a store like Redux, Zustand, or React Context. That way all dependent components get updates consistently. If it’s performance heavy, I’d split state into smaller slices to reduce unnecessary re-renders.

---

## 🔹 Python

### Q1: Performance Bottleneck
**Answer:**  
If a script handling millions of records is too slow, I’d first profile with `cProfile` to find bottlenecks. Then I’d optimize by using vectorized operations with pandas or NumPy instead of loops, and add indexing for database queries. For extreme cases, I’d parallelize with multiprocessing or move heavy tasks to distributed systems like Spark.

---

### Q2: Memory Error with Large File
**Answer:**  
I’d avoid loading the entire file into memory. Instead, I’d stream data line by line with generators or `with open(...):`. For pandas, I’d use `chunksize` to process batches. If memory is still a problem, I’d store intermediate results in a database or use Dask for out-of-core processing.

---

### Q3: Concurrency for API Calls
**Answer:**  
To make 100 API calls faster, I’d switch from sequential requests to asynchronous ones using `asyncio` + `aiohttp`. If CPU-bound, I’d use multiprocessing. This way, calls can be made concurrently, drastically reducing total runtime.

---

### Q4: Debugging Flask/Django 500 Errors
**Answer:**  
I’d first check server logs and enable debug logging temporarily to capture stack traces. If logs are not enough, I’d reproduce the issue locally with the same environment variables. Common causes are migrations not applied, dependency mismatches, or misconfigured settings. Once fixed, I’d add error monitoring like Sentry to catch future issues earlier.

---

### Q5: Data Validation
**Answer:**  
I’d never assume incoming JSON is clean. I’d validate fields with libraries like Pydantic or Marshmallow, applying default values or rejecting bad data. This ensures downstream logic doesn’t break because of unexpected inputs.

---

### Q6: Error Handling in Background Script
**Answer:**  
I’d wrap risky code in `try-except` blocks and log errors instead of crashing. For recurring tasks, I’d use retries with exponential backoff. If it’s a long-running service, I’d add monitoring so failures are reported immediately.

---

### Q7: Testing Frequent Business Rule Changes
**Answer:**  
I’d write unit tests for the discount function with multiple cases, including edge cases. When business rules change, I’d update the test cases alongside the code. This way regression is caught quickly, and I can be confident the logic matches requirements.

---

### Q8: Legacy Code Maintainability
**Answer:**  
With a messy codebase, I’d start by writing tests around critical functionality to avoid breaking things. Then I’d refactor gradually: extract duplicate logic into functions, add docstrings, and apply linting/formatting. For larger projects, I’d also introduce type hints to improve readability and reduce bugs.

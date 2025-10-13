# CitiusTech Python, Django, and SQL Interview Questions with Answers

---

## Python Interview Questions

### Basic

**Q1: Explain Python’s key features. Why is it popular in healthcare IT?**
**A1:** Python is interpreted, dynamically typed, supports OOP, and has extensive libraries. Popular in healthcare IT for data analysis, automation, and AI/ML integration.

**Q2: Difference between list, tuple, and set.**
**A2:**

- List: Ordered, mutable, allows duplicates.
- Tuple: Ordered, immutable, allows duplicates.
- Set: Unordered, mutable, no duplicates.

**Q3: What is Python’s GIL?**
**A3:** Global Interpreter Lock ensures only one thread executes Python bytecode at a time. Affects CPU-bound multithreading but not I/O-bound tasks.

**Q4: Difference between deep copy and shallow copy.**
**A4:**

- Shallow copy: Copies object structure, not nested objects.
- Deep copy: Copies entire object including nested objects.

**Q5: Difference between `is` and `==`.**
**A5:** `is` checks object identity, `==` checks value equality.

### Intermediate

**Q1: Explain Python generators and `yield`.**
**A1:** Generators return values lazily using `yield`, saving memory for large datasets.

**Q2: Difference between @staticmethod, @classmethod, and instance methods.**
**A2:**

- Instance method: Operates on instance (`self`).
- Class method: Operates on class (`cls`), uses @classmethod.
- Static method: No `self` or `cls`, utility function inside class.

**Q3: Explain \*args and **kwargs.\*\*
**A3:**

- `*args`: variable number of positional arguments.
- `**kwargs`: variable number of keyword arguments.

### Advanced

**Q1: Explain Python multithreading vs multiprocessing.**
**A1:**

- Multithreading: Multiple threads share memory, limited by GIL.
- Multiprocessing: Separate processes, true parallelism.

**Q2: How would you implement caching in Python?**
**A2:** Using `functools.lru_cache`, `cachetools`, or external cache like Redis.

**Q3: Explain Python asynchronous programming.**
**A3:** `asyncio` enables non-blocking async code with `async` and `await`.

---

## Django Interview Questions

### Basic

**Q1: What is Django?**
**A1:** Django is a high-level Python web framework following MVT architecture. Used for scalable, secure applications.

**Q2: Difference between ModelForm and Form.**
**A2:**

- Form: Manual form creation.
- ModelForm: Automatically creates form from model fields.

**Q3: Explain Django ORM.**
**A3:** ORM abstracts SQL queries using Python objects, simplifying database interactions.
ORM (Object-Relational Mapping) is a programming technique that creates a bridge between object-oriented programming languages and relational databases

### Intermediate

**Q1: Explain select_related vs prefetch_related.**
**A1:**

- select_related: Single query with JOIN for foreign key.
- prefetch_related: Separate queries, useful for many-to-many.

**Q2: How do you optimize Django queries?**
**A2:** Use select_related/prefetch_related, indexing, caching, pagination.

### Advanced

**Q1: How do you secure Django applications?**
**A1:** Enable CSRF tokens, use parameterized queries, secure cookies, HTTPS.

**Q2: Explain Django REST Framework.**
**A2:** DRF provides tools to create REST APIs, including serializers, viewsets, routers.

---

## SQL Interview Questions

### Basic

**Q1: Difference between INNER JOIN and LEFT JOIN.**
**A1:**

- INNER JOIN: Returns matching rows from both tables.
- LEFT JOIN: Returns all rows from left table + matching rows from right.

**Q2: Difference between WHERE and HAVING.**
**A2:**

- WHERE: Filters rows before aggregation.
- HAVING: Filters groups after aggregation.

### Intermediate

**Q1: Query to find second highest salary.**

```sql
SELECT MAX(salary) FROM employees
WHERE salary < (SELECT MAX(salary) FROM employees);
```

**Q2: Explain subqueries.**
**A2:** Queries nested inside another query. Correlated subquery depends on outer query row.

### Advanced

**Q1: Explain indexing strategies.**
**A1:** Use primary/unique indexes, composite indexes, cover indexes for frequent query columns to improve performance.

**Q2: How do you handle concurrency in SQL?**
**A2:** Use transactions, isolation levels, and locks to manage concurrent access.

---

_This document is a concise preparation guide for Python, Django, and SQL interviews at CitiusTech._

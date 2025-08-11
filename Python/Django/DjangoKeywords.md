# Django Keywords & Key Concepts

## 1. MVT Architecture

- **MVT** → Model–View–Template; Django’s design pattern for organizing code.
  - **Model** → Python class representing the database table. Handles data structure and interactions (CRUD operations).
  - **View** → Python function or class that processes requests, interacts with the model, and returns a response.
  - **Template** → HTML (with Django Template Language) used to render dynamic content for the user.
`
    ---

    ## 2. Core Django Components

    - **Project** → The main Django setup containing settings, URLs, and multiple apps.
    - **App** → A self-contained module within a project that performs a specific function (e.g., blog, shop, accounts).
    - **manage.py** → Command-line tool to manage the Django project (run server, migrations, etc.).
    - **settings.py** → Configuration file (database, installed apps, middleware, etc.).
    - **urls.py** → URL routing table that maps URLs to views.
    - **views.py** → Contains view functions or class-based views (CBVs) for request/response logic.
    - **models.py** → Contains database models using Django ORM.
    - **templates/** → Directory containing HTML files with dynamic placeholders.
    - **static/** → Directory for CSS, JavaScript, and images.
    - **migrations/** → Auto-generated scripts to update the database schema.

    ---`

## 3. Database & ORM

- **ORM (Object Relational Mapper)** → Allows interaction with the database using Python code instead of SQL.
- **QuerySet** → A collection of database records returned by a query.
- **Model Field** → Defines a column in the database table (e.g., `CharField`, `IntegerField`, `DateTimeField`).
- **ForeignKey** → Relationship linking two models (many-to-one).
- **OneToOneField** → One-to-one relationship between two models.
- **ManyToManyField** → Many-to-many relationship between models.
- **Migration** → Schema change script generated from model changes.
- **makemigrations** → Command to generate migration files.
- **migrate** → Command to apply migrations to the database.

---

## 4. Templates & Frontend

- **Django Template Language (DTL)** → Syntax for dynamic HTML (`{{ variable }}`, `{% for %}`, `{% if %}`, etc.).
- **Context** → Data dictionary passed from a view to a template.
- **Template Tag** → Special DTL command for loops, conditions, etc.
- **Template Filter** → Modifies variables in templates (e.g., `{{ name|upper }}`).

---

## 5. Request & Response Cycle

- **HTTP Request Object** → Contains all data from the client (method, headers, body, cookies, etc.).
- **HTTP Response Object** → Data sent back to the client (HTML, JSON, redirect, etc.).
- **URL Dispatcher** → Matches the requested URL with a view.
- **Path Converter** → Extracts parts of URL as parameters (`path('user/<int:id>/')`).

---

## 6. Authentication & Authorization

- **Authentication** → Verifying the identity of a user.
- **Authorization** → Checking user permissions.
- **User Model** → Built-in Django model for users.
- **Login/Logout Views** → Provided by Django's auth system.
- **Permissions** → Rules that control user access to certain features.
- **Groups** → Collections of permissions assigned to multiple users.

---

## 7. Advanced Django Features

- **Admin Site** → Auto-generated admin interface for managing models.
- **Middleware** → Hooks that process requests/responses globally (security, sessions, etc.).
- **Signals** → Event-based triggers (e.g., `post_save` after saving a model).
- **Session** → Stores user data between requests.
- **Cache** → Stores data temporarily to improve performance.
- **Paginator** → Splits large data sets into pages.

---

## 8. API & Async Support

- **Django REST Framework (DRF)** → Toolkit for building REST APIs.
- **Serializer** → Converts complex data (models, querysets) to JSON and vice versa.
- **APIView / ViewSet** → DRF views for handling API endpoints.
- **Async Views** → Handle asynchronous requests using `async def`.

---

## 9. Deployment & Environment

- **DEBUG** → Setting to toggle debug mode (never use `True` in production).
- **ALLOWED_HOSTS** → List of domains that can serve the project.
- **WSGI** → Entry point for deploying Django apps in synchronous mode.
- **ASGI** → Entry point for asynchronous Django apps.
- **Environment Variables** → Store sensitive data (e.g., secret keys, DB credentials).

---

## 10. Best Practices

- Follow **DRY** → Don’t Repeat Yourself.
- Keep **apps modular** → Separate logic into small, reusable apps.
- Use **environment-specific settings** → Separate dev, staging, and production configs.
- Always **validate user input** → Protect against injection attacks.
- Write **unit tests** → Use Django’s built-in test framework.

# Flask Keywords & Concepts

## 1. Basics

- **Flask** → lightweight Python web framework
- **WSGI** → Web Server Gateway Interface (Flask runs on WSGI servers)
- **app** → Flask application instance
- **route** → URL mapping for a function
- **view function** → function that handles a route
- **decorator** → `@app.route()` for mapping routes
- **request** → incoming HTTP request object
- **response** → outgoing HTTP response object
- **redirect** → redirect to another URL
- **abort** → stop request with an error code
- **g** → global variable for request scope

---

## 2. Application Setup

- `Flask(__name__)` → create app instance
- `app.run(debug=True)` → run server with debug mode
- **Environment Variables**:
  - `FLASK_APP` → entry point file
  - `FLASK_ENV` → `development` or `production`
- **Configuration Keys**:
  - `DEBUG`
  - `SECRET_KEY`
  - `ENV`
  - `TESTING`

---

## 3. Routing

- `@app.route("/")` → define route
- `methods=['GET', 'POST']` → allowed HTTP methods
- **Dynamic Routes** → `/user/<username>`
- **Type Converters**:
  - `<int:id>`
  - `<float:price>`
  - `<string:name>`
- **URL Building** → `url_for('function_name', param=value)`

---

## 4. HTTP Methods

- **GET** → retrieve data
- **POST** → send new data
- **PUT** → update existing data
- **DELETE** → remove data
- **PATCH** → partial update

---

## 5. Request Handling

- **Request Object** (`from flask import request`):
  - `request.method`
  - `request.args` → query parameters
  - `request.form` → form data
  - `request.json` → JSON body
  - `request.files` → file uploads
  - `request.headers`
  - `request.cookies`

---

## 6. Response Handling

- `return "Hello"` → plain text
- `return jsonify(data)` → JSON response
- `return render_template("index.html")` → HTML template
- `Response` object (`from flask import Response`)
- Status codes: `return "Error", 404`
- Headers: `response.headers["Custom"] = "Value"`
- File serving:
  - `send_file(path)`
  - `send_from_directory(directory, filename)`

---

## 7. Templates (Jinja2)

- **Template Folder** → `templates/`
- **Static Files** → `static/`
- Syntax:
  - `{{ variable }}` → print variable
  - `{% if %}`, `{% for %}` → control statements
  - `{% include "file.html" %}` → include templates
  - `{% extends "base.html" %}` → inherit from base template
  - `{% block content %}{% endblock %}` → define section
- Load static files: `url_for('static', filename='style.css')`

---

## 8. Blueprints (Modular Apps)

- Create: `Blueprint('name', __name__)`
- Register: `app.register_blueprint(blueprint)`

---

## 9. Middleware & Hooks

- `before_request` → run before each request
- `after_request` → modify response before sending
- `teardown_request` → cleanup after request
- `@app.errorhandler(code)` → custom error pages

---

## 10. Session & Cookies

- `from flask import session`
- Store: `session['user'] = 'name'`
- Requires: `app.secret_key`
- Cookies:
  - Read: `request.cookies`
  - Set: `response.set_cookie(key, value)`

---

## 11. Error Handling

- `@app.errorhandler(404)` → custom 404 page
- `abort(404)` → trigger 404
- `abort(403)` → forbidden

---

## 12. Flask Extensions

- **Flask-SQLAlchemy** → ORM
- **Flask-Migrate** → DB migrations
- **Flask-WTF** → forms
- **Flask-Login** → authentication
- **Flask-RESTful** → APIs
- **Flask-Caching** → caching
- **Flask-Mail** → send emails

---

## 13. Testing

- `app.test_client()` → simulate requests
- Use → `pytest` or `unittest`
- Mocks: `flask.testing`

---

## 14. Deployment

- Production servers: Gunicorn, uWSGI
- Config from object/file:
  - `app.config.from_object('config_module')`
  - `app.config.from_pyfile('config.py')`
- Set environment variables for deployment

---

## 15. Best Practices

- Use Blueprints for modular apps
- Store configs in separate files
- Avoid hardcoded secrets → use `.env`
- Debug mode only in development
- Use correct HTTP methods for APIs

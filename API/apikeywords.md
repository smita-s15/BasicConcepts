# Important API Keywords & Concepts (with Meanings)

## 1. API Basics

- **API (Application Programming Interface)** → A set of rules that allows different software systems to communicate with each other.
- **Endpoint** → A specific URL path that performs a certain function in the API.
- **Base URL** → The root address of the API (e.g., `https://api.example.com`).
- **HTTP Methods** → Actions to perform on resources:
  - `GET` → Retrieve data from the server (read-only).
  - `POST` → Create a new resource.
  - `PUT` → Update an entire existing resource.
  - `PATCH` → Update part of an existing resource.
  - `DELETE` → Remove a resource.
  - `OPTIONS` → Get information about supported request methods for a resource.
  - `HEAD` → Same as `GET` but returns headers only, no body.
- **Request** → The data and metadata the client sends to the server.
- **Response** → The data and metadata the server sends back to the client.
- **Status Codes** → Numbers indicating result of the request:
  - `200 OK` → Request succeeded.
  - `201 Created` → Resource created successfully.
  - `204 No Content` → Success, but no content returned.
  - `400 Bad Request` → Invalid request format or parameters.
  - `401 Unauthorized` → Authentication required or failed.
  - `403 Forbidden` → Authenticated but no permission to access.
  - `404 Not Found` → Resource doesn’t exist.
  - `500 Internal Server Error` → Unexpected server error.
- **Headers** → Key-value pairs with metadata (`Content-Type`, `Authorization`).
- **Body** → Main content of the request or response.
- **Query Parameters** → Key-value pairs in URL after `?` (e.g., `?page=2`).
- **Path Parameters** → Values in URL path (e.g., `/users/{id}`).
- **Versioning** → Version number in the URL (e.g., `/api/v1/resource`).

---

## 2. API Types

- **REST API** → HTTP-based architecture using standard methods like GET, POST.
- **GraphQL** → Query language where clients specify exactly what data they need.
- **SOAP API** → XML-based protocol for exchanging structured data.
- **gRPC** → High-performance remote procedure call framework using Protocol Buffers.
- **WebSocket API** → Real-time, bidirectional communication between client and server.

---

## 3. Authentication & Authorization

- **API Key** → Unique string used to authenticate requests.
- **Basic Auth** → Send username/password encoded in the `Authorization` header.
- **OAuth 2.0** → Token-based authentication with multiple flows for apps and users.
- **JWT (JSON Web Token)** → Signed token containing claims, used for authentication.
- **Bearer Token** → Token sent in the header: `Authorization: Bearer <token>`.
- **HMAC** → Hash-based message authentication code for verifying message integrity.
- **CORS (Cross-Origin Resource Sharing)** → Rules for sharing resources between different domains.

---

## 4. Data Formats

- **JSON** → Lightweight text format for structured data.
- **XML** → Markup language for structured data.
- **Form Data** → Used to send files or form submissions (`multipart/form-data`).
- **URL-encoded** → Encoded form data in `key=value` format.
- **YAML** → Human-readable configuration format.

---

## 5. Python API Development Keywords

- **Flask** → Lightweight Python web framework for APIs.
- **Django REST Framework (DRF)** → Django toolkit for building APIs.
- **FastAPI** → Modern, high-performance Python API framework with async support.
- **Blueprint** → Flask feature for organizing routes into modules.
- **Router** → In FastAPI, defines endpoints and paths.
- **Serializer** → Converts Python objects to JSON and vice versa.
- **Request Object** → Holds incoming request data.
- **Response Object** → Holds outgoing response data.
- **Middleware** → Functions that run before/after requests for extra processing.
- **Pagination** → Splits large results into multiple pages (`limit`, `offset`).
- **Rate Limiting** → Restricts number of requests in a given time.
- **Swagger / OpenAPI** → Standards for documenting APIs.
- **Async/Await** → Keywords for asynchronous request handling.

---

## 6. API Testing & Tools

- **Postman** → GUI tool for testing APIs.
- **cURL** → Command-line tool for making HTTP requests.
- **pytest** → Popular Python testing framework.
- **unittest** → Built-in Python testing library.
- **Requests** → Popular Python HTTP client library.
- **httpx** → Async Python HTTP client library.
- **Mocking** → Simulating API responses for testing purposes.

---

## 7. API Best Practices

- **Idempotency** → Multiple identical requests result in the same outcome (`PUT`, `DELETE`).
- **Statelessness** → Each request is independent; server doesn’t store client state.
- **Pagination & Filtering** → Manage large datasets efficiently.
- **Error Handling** → Use proper status codes and clear error messages.
- **Versioning** → Maintain compatibility by supporting multiple API versions.
- **Security** → Use HTTPS, authentication, and input validation.
- **Caching** → Store responses to reduce load and improve speed.

## Step 9: Testing in React

Testing ensures that your React applications are **robust, reliable, and bug-free**. There are multiple levels of testing from unit to end-to-end.

---

# 1. Unit Testing (Jest)

- **Jest** is a JavaScript testing framework for running **unit tests**.
- Focuses on testing **individual functions, utilities, or components**.

```jsx
import { sum } from "./utils";
test("adds 1 + 2 to equal 3", () => {
  expect(sum(1, 2)).toBe(3);
});
```

---

# 2. Component Testing (React Testing Library)

- Tests components **from the user's perspective**.
- Encourages testing behavior rather than implementation.

```jsx
import { render, screen } from "@testing-library/react";
import Button from "./Button";

test("renders button with text", () => {
  render(<Button>Click Me</Button>);
  expect(screen.getByText(/Click Me/i)).toBeInTheDocument();
});
```

---

# 3. Snapshot Testing

- Captures the **rendered output** of a component to detect changes.

```jsx
import renderer from "react-test-renderer";
import Button from "./Button";

it("matches snapshot", () => {
  const tree = renderer.create(<Button>Click</Button>).toJSON();
  expect(tree).toMatchSnapshot();
});
```

---

# 4. Async Testing and Mocking API Calls

- Test components that fetch data asynchronously.
- Use **mock functions** or libraries like `msw` for API mocking.

```jsx
import { render, screen, waitFor } from "@testing-library/react";
import axios from "axios";
import Users from "./Users";

jest.mock("axios");

test("fetches and displays users", async () => {
  axios.get.mockResolvedValue({ data: [{ name: "John" }] });
  render(<Users />);
  const user = await waitFor(() => screen.getByText("John"));
  expect(user).toBeInTheDocument();
});
```

---

# 5. Props and Event Testing

- Test **props behavior** and **user interactions** like clicks.

```jsx
test("button click calls handler", () => {
  const handleClick = jest.fn();
  render(<Button onClick={handleClick}>Click</Button>);
  screen.getByText("Click").click();
  expect(handleClick).toHaveBeenCalledTimes(1);
});
```

---

# 6. Integration Testing

- Tests **multiple components together** to verify overall functionality.
- Often combines unit tests with API mocking and user events.

---

# 7. End-to-End Testing Overview (Cypress / Playwright)

- **Cypress / Playwright** are tools for **full app testing** in real browsers.
- Tests user flows from start to finish.

```javascript
// Example Cypress test
describe("Login Flow", () => {
  it("logs in successfully", () => {
    cy.visit("/login");
    cy.get("input[name=email]").type("user@example.com");
    cy.get("input[name=password]").type("password");
    cy.get("button[type=submit]").click();
    cy.url().should("include", "/dashboard");
  });
});
```

---

**Key Takeaways:**

- Use **Jest** for unit and utility testing.
- Use **React Testing Library** for component and integration testing.
- Use **snapshot tests** to detect unexpected UI changes.
- Mock API calls for async behavior.
- End-to-end testing ensures **real-world app flow** works correctly.

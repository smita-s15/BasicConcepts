## Step 4: State Management

State management in React is crucial for handling dynamic data and ensuring components reflect the latest state efficiently. It can range from **local component state** to **global state management** solutions like Redux, MobX, or Recoil.

---

# 1. Lifting State Up

- When multiple components need access to the same state, **lift the state up** to their nearest common ancestor.
- Pass the state and state-updating function down via **props**.

```jsx
function Parent() {
  const [value, setValue] = React.useState(0);
  return (
    <>
      <ChildA value={value} setValue={setValue} />
      <ChildB value={value} />
    </>
  );
}
```

**Key Point:** Avoid duplicating state across components; centralize it at the nearest common ancestor.

---

# 2. Prop Drilling Problem

- **Prop drilling** occurs when you pass props through intermediate components that do not need them, just to reach deeply nested components.
- Can make code **hard to maintain** and **verbose**.
- Solutions: **Context API, Redux, Zustand, Recoil**.

```jsx
<GrandParent>
  <Parent>
    <Child value={value} /> // Child needs value, Parent just passes it
  </Parent>
</GrandParent>
```

---

# 3. Context API

The **Context API** provides a way to pass data through the component tree without **prop drilling**.

- **Provider**: Wraps components and supplies state.
- **Consumer**: Reads context in class components.
- **useContext**: Hook to access context in functional components.

```jsx
const ThemeContext = React.createContext();

function App() {
  const [theme, setTheme] = React.useState("dark");
  return (
    <ThemeContext.Provider value={{ theme, setTheme }}>
      <Child />
    </ThemeContext.Provider>
  );
}

function Child() {
  const { theme, setTheme } = React.useContext(ThemeContext);
  return (
    <button onClick={() => setTheme(theme === "dark" ? "light" : "dark")}>
      Toggle Theme
    </button>
  );
}
```

**Key Point:** Best for **medium-level global state**. Avoid overusing for highly dynamic or large applications.

---

# 4. Redux

Redux is a predictable **state container** for JavaScript apps.

- **Store**: Holds the global state.
- **Actions**: Objects describing **what happened**.
- **Reducers**: Functions describing **how state changes** based on actions.
- **Middleware**: Enhances dispatching (e.g., redux-thunk, redux-saga).

```jsx
// Action
const increment = () => ({ type: "INCREMENT" });

// Reducer
function counter(state = 0, action) {
  switch (action.type) {
    case "INCREMENT":
      return state + 1;
    default:
      return state;
  }
}

// Store
const store = Redux.createStore(counter);
store.dispatch(increment());
```

**Key Point:** Ideal for **large-scale applications** with complex state and multiple components needing access.

---

# 5. Redux Toolkit

- Simplifies Redux setup.
- Provides **configureStore**, **createSlice**, and **createAsyncThunk**.
- Reduces boilerplate and improves developer experience.

```jsx
import { configureStore, createSlice } from "@reduxjs/toolkit";

const counterSlice = createSlice({
  name: "counter",
  initialState: 0,
  reducers: {
    increment: (state) => state + 1,
    decrement: (state) => state - 1,
  },
});

const store = configureStore({ reducer: counterSlice.reducer });
store.dispatch(counterSlice.actions.increment());
```

---

# 6. MobX (Overview)

- Reactive state management library.
- Uses **observables**, **actions**, and **computed values**.
- State updates automatically propagate to components that **observe** it.

```jsx
import { makeAutoObservable } from "mobx";

class CounterStore {
  count = 0;
  constructor() {
    makeAutoObservable(this);
  }
  increment() {
    this.count += 1;
  }
}
```

**Key Point:** Easier learning curve than Redux; suitable for apps preferring **reactive programming**.

---

# 7. Zustand / Recoil (Overview)

- **Zustand**: Minimalistic state management library.

  ```jsx
  import create from "zustand";
  const useStore = create((set) => ({
    count: 0,
    increment: () => set((state) => ({ count: state.count + 1 })),
  }));
  ```

- **Recoil**: Facebook's state library for React.

  - Uses **atoms** for state and **selectors** for derived data.
  - Great for complex **component relationships** without prop drilling.

**Key Point:** Both are modern alternatives to Redux for **smaller or medium apps**.

---

# 8. Debugging State

- **Redux DevTools**: Inspect dispatched actions, state changes.
- **React DevTools**: Inspect component state, props, and hooks.
- Best practice: Always monitor state flow in complex apps to avoid bugs.

```jsx
// Redux DevTools example
const store = configureStore({
  reducer: rootReducer,
  devTools: process.env.NODE_ENV !== "production",
});
```

**Key Takeaways:**

- Lift state when multiple components need it.
- Avoid prop drilling using **Context API** or **state libraries**.
- Use Redux / MobX / Zustand / Recoil for **global state**.
- Always debug state using DevTools to ensure correctness.

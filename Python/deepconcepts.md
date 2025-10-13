Python offers various types of decorators, primarily categorized based on their application and the built-in functionalities they provide:

1.  Function Decorators:
    Simple Decorators: These are the most common type, taking a function as an argument and returning a new function (often a wrapper) that adds functionality before or after the original function's execution.
    Python

        def my_decorator(func):
            def wrapper(*args, **kwargs):
                print("Something before the function.")
                result = func(*args, **kwargs)
                print("Something after the function.")
                return result
            return wrapper

        @my_decorator
        def greet(name):
            print(f"Hello, {name}!")

    Decorators with Arguments: These decorators accept arguments when applied, allowing for more dynamic behavior. This typically involves an outer function that takes the decorator arguments and returns the actual decorator function.
    Python

        def repeat(num_times):
            def decorator_repeat(func):
                def wrapper(*args, **kwargs):
                    for _ in range(num_times):
                        func(*args, **kwargs)
                return wrapper
            return decorator_repeat

        @repeat(num_times=3)
        def say_hello():
            print("Hello!")

2.  Built-in Decorators:
    @property:
    Transforms a method into a read-only attribute (getter) and allows defining setter and deleter methods for property management.
    @classmethod:
    Binds a method to the class rather than the instance, meaning it receives the class itself (cls) as the first argument.
    @staticmethod:
    Defines a method that belongs to the class but does not receive either the instance (self) or the class (cls) as an implicit first argument. It behaves like a regular function within the class namespace.
    @functools.wraps:
    A helper decorator used within custom decorators to preserve the metadata (like **name**, **doc**) of the wrapped function, making debugging and introspection easier.
3.  Class Decorators:
    Class Decorators: These decorators are applied to entire classes, modifying or enhancing their behavior, attributes, or methods during class creation. They take a class as an argument and return a modified class or a new class.
    Python

        def add_method(cls):
            def new_method(self):
                print("This is a new method added by the decorator.")
            cls.new_method = new_method
            return cls

        @add_method
        class MyClass:
            pass

    Common Use Cases:
    Decorators are widely used for:
    Logging: Adding logging statements before/after function calls.
    Timing/Profiling: Measuring function execution time.
    Authentication/Authorization: Restricting access to functions based on user roles.
    Caching: Storing and retrieving results of expensive function calls.
    Validation: Enforcing type checking or other constraints on function arguments.
    Metaprogramming: Modifying class behavior or adding methods dynamically.

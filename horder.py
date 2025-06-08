# def my_decorator(func):
#     def wrapper():
#         print("Inside the Decorator")
#         print(func.__name__)
#         func()
#         print("Exitting the Decorator")

#     return wrapper


# @my_decorator
# def my_function():
#     print("I'm running...")


# my_function()


def repeat(num_times):
    """Decorator that repeats the decorated function call num_times."""

    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result  # returns only the last call's result

        return wrapper

    return decorator_repeat


# Usage example
@repeat(num_times=3)
def greet(name, number):
    print(f"Hello, {name}! - {number}")


greet("Alice", 12)

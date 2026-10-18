def greet(name: str) -> str:
    """Return a greeting message."""
    return f"Hello, {name}! Welcome to DevOps learning."


def add_numbers(a: int, b: int) -> int:
    """Add two numbers and return the result."""
    return a + b


if __name__ == "__main__":
    print(greet("Learner"))
    print(f"2 + 3 = {add_numbers(2, 3)}")

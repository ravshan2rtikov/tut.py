# Pythonic implementation leveraging built-in truth value testing
def is_truthy(value) -> str:
    """Return 'Truthy' if value evaluates to True, otherwise 'Falsy'."""
    return "Truthy" if value else "Falsy"


# Demonstration of behavior
def main():
    test_values = [0, 10, 0.0, 10.0, "", "hello", [], [1], {}, {"key": "value"}]
    for val in test_values:
        print(val, "is", is_truthy(val))


if __name__ == "__main__":
    main()

def square(x: int | float) -> int | float:
    """Returns the square of the given parameter"""
    return x ** 2


def pow(x: int | float) -> int | float:
    """Returns the given parameter power itself"""
    return x ** x


def outer(x: int | float, function) -> object:
    """Returns a closure that repeatadly applies the given function / value"""

    count = 0  # Forced to keep this line by the assignment :(

    def inner() -> float:
        """Updates the outer counter for the given function"""

        nonlocal count
        return (count := function(count))

    count = x
    return inner

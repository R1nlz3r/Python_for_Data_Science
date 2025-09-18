from typing import Any


def callLimit(limit: int):
    """Handles the decorator limit parameter"""

    count = 0

    def callLimiter(function):
        """Handles the wrapped function"""

        def limit_function(*args: Any, **kwds: Any):
            """
                Limits the maximum number of calls to the wrapped function
                or prints an error
            """

            nonlocal count
            count += 1
            if count <= limit:
                return function(*args, **kwds)
            else:
                print(f"Error: {function} call too many times")
        return limit_function
    return callLimiter

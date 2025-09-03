import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
        Truncates a 2D array.
    """

    array = []

    try:
        assert type(family) is list, "Input must be a list"
        assert type(start) is int, "Start index must be an integer"
        assert type(end) is int, "End index must be an integer"

        array = np.array(family)
        assert len(array.shape) >= 1, "Input must be a non-empty array"
        print(f"My shape is : {array.shape}")
        array = array[start:end]
        print(f"My shape is : {array.shape}")
        array = array.tolist()

    except AssertionError as e:
        print(f"AssertionError: {e}")

    return array

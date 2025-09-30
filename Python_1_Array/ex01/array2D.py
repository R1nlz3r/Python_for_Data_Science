import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """Truncates a 2D array within two indexes"""

    try:
        if not isinstance(family, list):
            raise TypeError("Input must be a list")
        if not isinstance(start, int):
            raise TypeError("Start index must be an integer")
        if not isinstance(end, int):
            raise TypeError("End index must be an integer")

        array = np.array(family)

        if len(array.shape) < 1:
            raise ValueError("Input must be a non-empty array")

        print(f"My shape is : {array.shape}")
        array = array[start:end]
        print(f"My new shape is : {array.shape}")
        return array.tolist()

    except (TypeError, ValueError) as e:
        print(f"{type(e).__name__}: {e}")
        return []

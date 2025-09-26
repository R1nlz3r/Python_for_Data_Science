def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """Compute BMI (kg/m²) for each height-weight pair"""

    results = []

    try:
        if not isinstance(height, list) or not isinstance(weight, list):
            raise TypeError("Parameters must be lists")
        if len(height) != len(weight):
            raise ValueError("Lists must be of the same size")
        for h, w in zip(height, weight):
            if not isinstance(h, (int, float)):
                raise TypeError("Heights must be numeric")
            if not isinstance(w, (int, float)):
                raise TypeError("Weights must be numeric")
            h = h ** 2
            if h <= 0 or w < 0:
                raise ValueError("Invalid height/weight values")
            results.append(w / h)
    except (TypeError, ValueError) as e:
        print(f"{type(e).__name__}: {e}")
        return []

    return results


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Checks if each BMI value exceeds the given limit"""

    results = []

    try:
        if not isinstance(bmi, list):
            raise TypeError("BMI values should be in a list")
        if not isinstance(limit, int):
            raise TypeError("Limit treshhold must be an integer")
        for value in bmi:
            if not isinstance(value, int) and not isinstance(value, float):
                raise TypeError("BMI values should be numeric")
            results.append(value > limit)
    except TypeError as e:
        print(f"{type(e).__name__}: {e}")
        return []

    return results

def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
        Compute BMI (kg/m²) for each height-weight pair
    """

    results = []

    try:
        assert type(height) is list and type(
            weight) is list, "Parameters must be lists"
        assert len(height) == len(weight), "lists are not of the same size"
        for h, w in zip(height, weight):
            assert type(h) is int or type(
                h) is float, "Heights must be numeric"
            assert type(w) is int or type(
                w) is float, "Weights must be numeric"
            h = h ** 2
            assert h > 0 and w >= 0 and h != w, "Invalid height/weight values"
            results.append(w / h)
    except AssertionError as e:
        print(f"AssertionError: {e}")

    return results


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
        Checks if each BMI value exceeds the given limit
    """

    results = []

    try:
        assert type(bmi) is list, "BMI values should be in a list"
        assert type(limit) is int, "Limit treshhold must be an integer"
        for value in bmi:
            assert type(value) is int or type(
                value) is float, "BMI values must be numeric"
            results.append(value > limit)
    except AssertionError as e:
        print(f"AssertionError: {e}")

    return results

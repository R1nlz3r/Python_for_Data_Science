from typing import Any


def variance(args: Any) -> None:
    """Returns the variance of a given parameter or throws"""

    length = len(args)
    mean_value = sum(args) / length
    return sum((x - mean_value) ** 2 for x in args) / length


def standard_derivation(args: Any) -> None:
    """Returns the standard deviation of a given parameter or throws"""

    return variance(args) ** 0.5


def quartile(args) -> None:
    """Returns the Tukey’s Hinges Q1 and Q3 of a given parameter or throws"""

    sorted_args = sorted(args)
    length = len(args)

    q1_index = (length - 1) * 0.25
    if q1_index.is_integer():
        q1 = sorted_args[int(q1_index)]
    else:
        q1 = (sorted_args[int(q1_index)] + sorted_args[int(q1_index) + 1]) / 2

    q3_index = (length - 1) * 0.75
    if q3_index.is_integer():
        q3 = sorted_args[int(q3_index)]
    else:
        q3 = (sorted_args[int(q3_index)] + sorted_args[int(q3_index) + 1]) / 2

    return [q1, q3]


def median(args) -> None:
    """Returns the median of a given parameter or throws"""

    sorted_args = sorted(args)
    length = len(args)

    return (sorted_args[length // 2] + sorted_args[(length - 1) // 2]) / 2


def mean(args: Any) -> None:
    """Returns the mean of a given parameter or throws"""

    return sum(args) / len(args)


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """Prints asked statistics in kwargs for values contained in args"""

    statistics = {
        "mean": mean,
        "median": median,
        "quartile": quartile,
        "std": standard_derivation,
        "var": variance
    }

    for key, value in kwargs.items():
        if value in statistics:
            try:
                print(f"{value}: {statistics[value](args)}")
            except (IndexError, ZeroDivisionError, TypeError):
                print("ERROR")

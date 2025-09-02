import sys
from ft_filter import ft_filter


def main():
    """
        Filter a string of words as the first argument.
        Print those who are longer than the second integer argument
    """

    assert len(sys.argv) == 3, "the arguments are bad"
    assert type(sys.argv[1]) is str, "the arguments are bad"
    assert type(sys.argv[2]) is str or type(sys.argv[2]) is int, \
        "the arguments are bad"
    try:
        print(list(ft_filter(lambda x: len(x) > int(sys.argv[2]),
                             sys.argv[1].split())))
    except ValueError:
        raise AssertionError("the arguments are bad")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")

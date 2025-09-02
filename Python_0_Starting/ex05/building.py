import sys
import string


def main():
    """
        Prints the sum of uppercase, lowercase, punctuation,
        digit and space characters of the first argument.
        Asks for input is no argument is provided.
    """
    try:
        if len(sys.argv) < 2 or sys.argv[1] is None:
            print("What is the text to count?")
            try:
                text = input()
            except (EOFError, KeyboardInterrupt):
                text = "\n"
        elif len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
        else:
            text = sys.argv[1]
    except AssertionError as e:
        print(f"AssertionError: {e}")
        exit(-1)

        print(text)
    print(f"""The text contains {len(text)} characters:
{sum(c in string.ascii_uppercase for c in text)} uppercase letters
{sum(c in string.ascii_lowercase for c in text)} lowercase letters
{sum(c in string.punctuation for c in text)} punctuation marks
{sum(c in string.whitespace for c in text)} whitespace characters
{sum(c in string.digits for c in text)} digits""")


if __name__ == "__main__":
    main()

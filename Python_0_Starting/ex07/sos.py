import sys


def main():
    """
        Takes a string as argument and prints it encoded into Morse Code.
    """

    NESTED_MORSE = {
        "A": ".-",		"a": ".-",
        "B": "-...",	"b": "-...",
        "C": "-.-.",	"c": "-.-.",
        "D": "-..",		"d": "-..",
        "E": ".",		"e": ".",
        "F": "..-.",	"f": "..-.",
        "G": "--.",		"g": "--.",
        "H": "....",	"h": "....",
        "I": "..",		"i": "..",
        "J": ".---",	"j": ".---",
        "K": "-.-",		"k": "-.-",
        "L": ".-..",	"l": ".-..",
        "M": "--",		"m": "--",
        "N": "-.",		"n": "-.",
        "O": "---",		"o": "---",
        "P": ".--.",	"p": ".--.",
        "Q": "--.-",	"q": "--.-",
        "R": ".-.",		"r": ".-.",
        "S": "...",		"s": "...",
        "T": "-",		"t": "-",
        "U": "..-",		"u": "..-",
        "V": "...-",	"v": "...-",
        "W": ".--",		"w": ".--",
        "X": "-..-",	"x": "-..-",
        "Y": "-.--",	"y": "-.--",
        "Z": "--..",	"z": "--..",
        "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
        "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
        " ": "/"
    }

    assert len(sys.argv) == 2, "the arguments are bad"
    try:
        print(" ".join(NESTED_MORSE[c] for c in sys.argv[1]))
    except KeyError:
        raise AssertionError("the arguments are bad")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")

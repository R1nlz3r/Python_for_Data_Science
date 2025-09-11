import sys
import matplotlib.pyplot as plt
from load_csv import load


def main():
    """Displays a graph of life expectancy in France against years"""

    assert len(sys.argv) == 2, "Usage: python aff_life.py <path_to_csv>"
    if (data := load(sys.argv[1])) is None:
        exit(-1)

    years = data.columns[1:].astype(int).to_numpy()
    life_expct = data.loc[data["country"] == "France"].to_numpy()[0, 1:]

    plt.title("France Life Expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    plt.plot(years, life_expct)
    plt.show()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"{type(e).__name__}: {e}")

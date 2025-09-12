import matplotlib.pyplot as plt
from load_csv import load


def convert_gdp(value: str | float) -> float:
    """Converts custom string format into values"""

    if isinstance(value, str) and 'k' in value:
        return float(value.replace('k', '')) * 1e3
    else:
        return float(value)


def format_gdp(x, pos):
    """Overwrites the x axis ticker format"""

    if x >= 1e3:
        return f'{x/1e3:.0f}k'
    else:
        return f'{x:.0f}'


def main():
    """
        Displays a scatter plot of countries GDP
        against life expectancy in 1900
    """

    data1 = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    data2 = load("life_expectancy_years.csv")
    if data1 is None or data2 is None:
        exit(-1)

    year = "1900"
    data1 = [convert_gdp(x) for x in data1[year].to_numpy()]
    data2 = data2[year]

    fig, ax = plt.subplots()
    plt.xscale("log")
    ax.xaxis.set_major_formatter(format_gdp)

    plt.scatter(data1, data2)
    plt.title(year)
    plt.xlabel("Gross Domestic Product")
    plt.ylabel("Life Expectancy")
    plt.show()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"{type(e).__name__}: {e}")

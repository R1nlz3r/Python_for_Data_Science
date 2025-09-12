import matplotlib.pyplot as plt
from load_csv import load


def convert_population(value: str) -> float:
    """Converts custom string format into values"""

    if 'B' in value:
        return float(value.replace('B', '')) * 1e9
    elif 'M' in value:
        return float(value.replace('M', '')) * 1e6
    elif 'K' in value:
        return float(value.replace('K', '')) * 1e3
    else:
        return float(value)


def format_population(x, pos):
    """Overwrites the y axis ticker format"""

    if x >= 1e9:
        return f'{x/1e9:.1f}B'
    elif x >= 1e6:
        return f'{x/1e6:.0f}M'
    elif x >= 1e3:
        return f'{x/1e3:.0f}K'
    else:
        return f'{x:.0f}'


def main():
    """Displays a population projection in France and Belgium"""

    if (data := load("population_total.csv")) is None:
        exit(-1)

    countries = ["France", "Belgium"]
    years = data.columns[1:].astype(int).to_numpy()
    mask = (years >= 1800) & (years <= 2050)
    years = years[mask]
    data = data[data["country"].isin(countries)]

    fig, ax = plt.subplots()
    ax.yaxis.set_major_formatter(format_population)

    for country in countries:
        pop = data.loc[data["country"] == country].to_numpy()[0, 1:][mask]
        pop = [convert_population(x) for x in pop]
        plt.plot(years, pop, label=country)

    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"{type(e).__name__}: {e}")

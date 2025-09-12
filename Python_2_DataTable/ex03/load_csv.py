import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
        Loads a csv file passed as argument
        Prints the shape and returns the data
    """

    try:
        if not isinstance(path, str):
            raise TypeError("Path is of the wrong type")
        csv = pd.read_csv(path)
    except FileNotFoundError:
        print("FileNotFoundError: The file does not exist")
        return None
    except PermissionError:
        print("PermissionError: Unable to read the file")
        return None
    except pd.errors.EmptyDataError:
        print("EmptyDataError: The file header/data is empty")
        return None
    except UnicodeDecodeError:
        print("UnicodeDecodeError: The codec cannot decode data in the file")
        return None
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        return None

    print(f"Loading dataset of dimensions {csv.shape}")
    return csv

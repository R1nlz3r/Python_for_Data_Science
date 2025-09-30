from PIL import Image, UnidentifiedImageError
import numpy as np


def ft_load(path: str, verbose: bool = True) -> np.ndarray | None:
    """Loads an image and returns its RGB data."""

    try:
        if not isinstance(path, str):
            raise TypeError
        with Image.open(path) as img:
            data = np.array(img.convert("RGB"))
            if verbose:
                print(f"The shape of image is: {data.shape}")
                print(data)
            return data
    except TypeError:
        print("TypeError: Path must be a string")
    except FileNotFoundError:
        print("FileNotFoundError: Incorrect path to image")
    except UnidentifiedImageError:
        print("UnidentifiedImageError: Invalid or corrupted file")
    except PermissionError:
        print("PermissionError: No permission to read the file")
    except Exception as e:
        print(f"{type(e).__name__}: {e}")

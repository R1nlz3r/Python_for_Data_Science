from PIL import Image, UnidentifiedImageError
import numpy as np


def ft_load(path: str) -> np.array:
    """
        Loads an image and returns its RGB data.
    """

    data = []
    try:
        with Image.open(path) as img:
            data = np.array(img.convert("RGB"))
    except FileNotFoundError:
        raise FileNotFoundError("File not found")
    except UnidentifiedImageError:
        raise Exception("Cannot open or identify the file")
    except ValueError:
        raise PermissionError("No permission to read the file")

    print(f"The shape of image is: {data.shape}")
    return data

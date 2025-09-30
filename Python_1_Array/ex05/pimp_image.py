import numpy as np
import matplotlib.pyplot as plt


def ft_invert(array: np.ndarray) -> np.ndarray:
    """Inverts the RGB color values of an array and displays the image"""

    if not isinstance(array, np.ndarray):
        print("TypeError: Input must be a Numpy array")
    elif array.ndim != 3 or array.shape[2] != 3:
        print("ValueError: Input must be a RGB array")
    elif array.dtype != np.uint8:
        print("ValueError: Input array must be of dtype uint8")
    else:
        array = 255 - array.copy()
        plt.imshow(array)
        plt.show()

    return array


def ft_red(array: np.ndarray) -> np.ndarray:
    """Isolates the red channel of an RGB array and displays the image"""

    if not isinstance(array, np.ndarray):
        print("TypeError: Input must be a Numpy array")
    elif array.ndim != 3 or array.shape[2] != 3:
        print("ValueError: Input must be a RGB array")
    elif array.dtype != np.uint8:
        print("ValueError: Input array must be of dtype uint8")
    else:
        array = array.copy()
        array[..., 1:] = 0
        plt.imshow(array)
        plt.show()

    return array


def ft_green(array: np.ndarray) -> np.ndarray:
    """Isolates the green channel of an RGB array and displays the image"""

    if not isinstance(array, np.ndarray):
        print("TypeError: Input must be a Numpy array")
    elif array.ndim != 3 or array.shape[2] != 3:
        print("ValueError: Input must be a RGB array")
    elif array.dtype != np.uint8:
        print("ValueError: Input array must be of dtype uint8")
    else:
        array = array.copy()
        array[..., [0, 2]] = 0
        plt.imshow(array)
        plt.show()

    return array


def ft_blue(array: np.ndarray) -> np.ndarray:
    """Isolates the blue channel of an RGB array and displays the image"""

    if not isinstance(array, np.ndarray):
        print("TypeError: Input must be a Numpy array")
    elif array.ndim != 3 or array.shape[2] != 3:
        print("ValueError: Input must be a RGB array")
    elif array.dtype != np.uint8:
        print("ValueError: Input array must be of dtype uint8")
    else:
        array = array.copy()
        array[..., :2] = 0
        plt.imshow(array)
        plt.show()

    return array


def ft_grey(array: np.ndarray) -> np.ndarray:
    """Converts an RGB array to grayscale and displays the image"""

    if not isinstance(array, np.ndarray):
        print("TypeError: Input must be a Numpy array")
    elif array.ndim != 3 or array.shape[2] != 3:
        print("ValueError: Input must be a RGB array")
    elif array.dtype != np.uint8:
        print("ValueError: Input array must be of dtype uint8")
    else:
        greyscale = np.empty_like(array)
        array = np.mean(array.copy(), axis=2).astype(np.uint8)
        for i in range(3):
            greyscale[:, :, i] = array
        plt.imshow(greyscale)
        plt.show()
        return greyscale

    return array

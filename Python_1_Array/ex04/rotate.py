import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def main() -> None:
    """
        Loads an image, crops a region, converts it to grayscale,
        transposes it to the left then displays it.
    """

    if (image := ft_load("animal.jpeg", verbose=False)) is None:
        return
    image = image[100:500, 450:850]
    if not image.shape[0] or not image.shape[1]:
        raise TypeError("Zoom not possible")
    image = np.mean(image, axis=2).astype(np.uint8)
    image = np.expand_dims(image, axis=-1)
    print(f"The shape of image is: {image.shape} or {image.shape[:2]}")
    print(image)
    rotated = np.empty((image.shape[0], image.shape[1]), dtype=np.uint8)
    for y in range(rotated.shape[1]):
        for x in range(rotated.shape[0]):
            rotated[x, y] = image[y, x, 0]
    print(f"New shape after transpose: {rotated.shape}")
    print(rotated)
    plt.imshow(rotated, cmap="gray")
    plt.show()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"{type(e).__name__}: {e}")

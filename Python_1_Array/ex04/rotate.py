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
    image = image[:, :, 0].T
    print(f"New shape after transpose: {image.shape}")
    print(image)
    plt.imshow(image, cmap="gray")
    plt.show()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"{type(e).__name__}: {e}")

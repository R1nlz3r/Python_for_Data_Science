class calculator:
    """Vector calculator supporting basic mathematics with a scalar"""

    def __init__(self, vector):
        """Initialize the calculator with a vector"""
        self.vector = vector

    def __add__(self, object) -> None:
        """Adds a scalar to every value of the stored vector"""
        self.vector = [x + object for x in self.vector]
        print(self.vector)

    def __mul__(self, object) -> None:
        """Multiplies every value of the stored vector by a scalar"""
        self.vector = [x * object for x in self.vector]
        print(self.vector)

    def __sub__(self, object) -> None:
        """Substracts a scalar to every value of the stored vector"""
        self.vector = [x - object for x in self.vector]
        print(self.vector)

    def __truediv__(self, object) -> None:
        """Divides every value of the stored vector by a scalar"""
        if object == 0:
            print("Error: Division by zero is not allowed")
            return
        self.vector = [x / object for x in self.vector]
        print(self.vector)

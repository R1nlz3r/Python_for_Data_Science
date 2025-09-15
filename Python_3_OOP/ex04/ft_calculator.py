class calculator:
    """Vector calculator supporting basic mathematics with another vector"""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Prints the dot product of two vectors"""
        print(f"Dot product is: {sum([x * y for x, y in zip(V1, V2)])}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Prints the result of two vectors added together"""
        print(f"Add Vector is: {[float(x + y) for x, y in zip(V1, V2)]}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Prints the result of two vectors substracted together"""
        print(f"Sous Vector is: {[float(x - y) for x, y in zip(V1, V2)]}")

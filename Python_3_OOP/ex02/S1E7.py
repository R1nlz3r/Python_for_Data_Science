from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family"""

    def __init__(self, first_name, is_alive=True):
        """Initialize the Baratheon family traits"""
        super().__init__(first_name)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        """Returns a human readable representation of a Baratheon object"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Returns the full representation of a Baratheon object"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def die(self):
        """Boolean irreversible switch on life"""
        self.is_alive = False


class Lannister(Character):
    """Representing the Lannister family"""

    def __init__(self, first_name, is_alive=True):
        "Initialize the Lannister family traits"
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        """Returns a human readable representation of a Lannister object"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Returns the full representation of a Lannister object"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def die(self):
        """Boolean irreversible switch on life"""
        self.is_alive = False

    def create_lannister(self, first_name, is_alive=True):
        """Instantiates and returns a new Lannister"""
        return Lannister(first_name, is_alive)

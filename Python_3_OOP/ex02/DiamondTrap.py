from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Representing the King"""

    def __init__(self, first_name, is_alive=True):
        """Initialize the Baratheon family traits"""
        super().__init__(first_name, is_alive)

    def set_eyes(self, eyes):
        """Modifies the eye color of a King object"""
        self.eyes = eyes

    def get_eyes(self):
        """Returns the eye color of a King object"""
        return self.eyes

    def set_hairs(self, hairs):
        """Modifies the hair color of a King object"""
        self.hairs = hairs

    def get_hairs(self):
        """Returns the hair color of a King object"""
        return self.hairs

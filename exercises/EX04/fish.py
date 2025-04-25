"""File to define Fish class."""

__author__: str = "730431256"


class Fish:
    """Class to define Fish."""

    age: int

    def __init__(self) -> None:
        """Initialize a Fish instance."""
        self.age = 0
        return None

    def one_day(self) -> None:
        """Increase the age of the fish by 1."""
        self.age += 1
        return None

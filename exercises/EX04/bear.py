"""File to define Bear class."""

__author__: str = "730431256"


class Bear:
    """Class to define Bear."""

    age: int
    hunger_score: int

    def __init__(self) -> None:
        """Initialize a Bear instance."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self) -> None:
        """Increase the age of the bear by 1 and decrease hunger score by 1."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int) -> None:
        """Increase the hunger score by 1."""
        self.hunger_score += num_fish
        return None

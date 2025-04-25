"""File to define River class."""

__author__: str = "730431256"

from fish import Fish
from bear import Bear


class River:
    """Class to define River."""

    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int) -> None:
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self) -> None:
        """Remove old Fish and Bear's from River."""
        # Remove old Fish
        # Create a new list for surviving fish
        surviving_fish: list[Fish] = []
        for fish in self.fish:
            if fish.age <= 3:
                surviving_fish.append(fish)
        self.fish = surviving_fish
        # Create a new list for surviving bears
        surviving_bears: list[Bear] = []
        for bear in self.bears:
            if bear.age <= 5:
                surviving_bears.append(bear)
        self.bears = surviving_bears
        return None

    def remove_fish(self, amount: int) -> None:
        """Remove the frontmost `amount` fish from the river."""
        new_fish_list = []
        counter = 0
        for fish in self.fish:
            if counter >= amount:
                new_fish_list.append(fish)
            else:
                counter += 1
        self.fish = new_fish_list
        return None

    def bears_eating(self) -> None:
        """Each bear eats 3 fish if at least 5 fish are available."""
        fish_count = 0
        for _ in self.fish:
            fish_count += 1
        for bear in self.bears:
            if fish_count >= 5:
                self.remove_fish(3)
                bear.eat(3)
        return None

    def check_hunger(self) -> None:
        """Remove hungry Bear's from River."""
        # Create a new list for surviving bears
        surviving_bears = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                surviving_bears.append(bear)
        self.bears = surviving_bears
        return None

    def repopulate_fish(self) -> None:
        """Each pair of fish produces 4 new fish."""
        fish_count = 0
        for fish in self.fish:
            fish_count += 1
        num_new_fish = (fish_count // 2) * 4
        for _ in range(num_new_fish):
            self.fish.append(Fish())
        return None

    def repopulate_bears(self) -> None:
        """Each pair of bears produces 1 new bear."""
        bear_count = 0
        for bear in self.bears:
            bear_count += 1
        num_new_bears = bear_count // 2
        for _ in range(num_new_bears):
            self.bears.append(Bear())
        return None

    def view_river(self) -> None:
        """Print the current state of the river."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")

    def one_river_week(self) -> None:
        """Simulate one week of life in the river."""
        # Simulate 7 days
        for _ in range(7):
            self.one_river_day()
        return None

    def one_river_day(self) -> None:
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        return None

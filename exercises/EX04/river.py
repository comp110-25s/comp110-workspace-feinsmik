"""File to define River class."""

from fish import Fish
from bear import Bear


class River:
    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Remove old Fish and Bear's from River"""
        # Remove old Fish
        # Create a new list for surviving fish
        surviving_fish = []
        for fish in self.fish:
            if fish.age <= 3:
                surviving_fish.append(fish)
        self.fish = surviving_fish
        # Create a new list for surviving bears
        surviving_bears = []
        for bear in self.bears:
            if bear.age <= 5:
                surviving_bears.append(bear)
        self.bears = surviving_bears
        return None

    def remove_fish(self, amount: int):
        # Remove the first `amount` fish (starting from index 0)
        self.fish = self.fish[amount:]
        return None

    def bears_eating(self):
        """Simulate Bear's eating"""
        for bear in self.bears:
            # Check if the bear is hungry
            if len(self.fish) >= 5:
                # Bear eats 5 fish
                bear.eat(3)
                # Remove 5 fish from the river
                self.remove_fish(3)
        return None

    def check_hunger(self):
        """Remove hungry Bear's from River"""
        # Create a new list for surviving bears
        surviving_bears = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                surviving_bears.append(bear)
        self.bears = surviving_bears
        return None

    def repopulate_fish(self):
        """Simulate Fish repopulation"""
        num_new_fish = (len(self.fish) // 2) * 4  # 4 fish per pair
        for _ in range(num_new_fish):
            # Create a new Fish and add it to the river
            new_fish = Fish()
            self.fish.append(new_fish)
        return None

    def repopulate_bears(self):
        """Simulate Bear repopulation"""
        num_new_bears = len(self.bears) // 2
        for _ in range(num_new_bears):
            # Create a new Bear and add it to the river
            new_bear = Bear()
            self.bears.append(new_bear)
        return None

    def view_river(self):
        """Print the current state of the river"""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_week(self):
        """Simulate one week of life in the river"""
        # Simulate 7 days
        for _ in range(0, 7):
            self.one_river_day()
        return None

    def one_river_day(self):
        """Simulate one day of life in the river"""
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
        # Visualize River
        self.view_river()

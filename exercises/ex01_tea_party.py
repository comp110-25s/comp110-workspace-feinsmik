"""Exercise 01 planning a tea party"""

_author_: str = "730431256"


def main_planner(guests: int) -> None:
    """Main Planner Function"""


def tea_bags(people: int) -> int:
    """Calculating the Number of Teabags Needed"""
    return people * 2


def treats(people: int) -> int:
    """Number of Treats per amount of tea"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """cost of teabags and Treats"""
    return 0.50 * tea_count + 0.75 * treat_count

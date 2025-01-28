"""Exercise 01 planning a tea party"""

__author__: str = "730431256"


def main_planner(guests: int) -> None:
    """Main Planner Function"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(round(cost(tea_bags(guests), treats(guests)), 2)))
    return None


def tea_bags(people: int) -> int:
    """Calculating the Number of Teabags Needed"""
    return people * 2


def treats(people: int) -> int:
    """Number of Treats per amount of tea"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """cost of teabags and Treats"""
    return 0.50 * tea_count + 0.75 * treat_count


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))

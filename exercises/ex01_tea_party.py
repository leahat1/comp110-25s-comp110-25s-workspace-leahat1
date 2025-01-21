"""Exercise 01 - Giant Tea party costs and requirements"""

__author__: str = "730489756"


def main_planner(guests: int) -> None:
    """The purpose of this function is to serve as the main entrypoint of the program"""
    print(f"A Cozy Tea Party for {guests} People!")
    print(f"Tea Bags: {tea_bags(people=guests)}")
    print(f"Treats: {treats(people=guests)}")
    print(
        f"Cost: ${cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))}"
    )


def tea_bags(people: int) -> int:
    """Calculates number of tea bags needed based on number of people"""
    return 2 * people


def treats(people: int) -> int:
    """Calculates number of treats needed based on number of people"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Cost of the party based on tea bags and treats)"""
    return 0.5 * tea_count + 0.75 * treat_count


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))

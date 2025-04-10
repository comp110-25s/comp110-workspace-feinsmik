"""Exercise 03 Making a Dictionary"""

__author__: str = "730431256"


def invert(my_dictionary: dict[str, str]) -> dict[str, str]:
    """Inverts key-value pairs of a dictionary."""
    inverted: dict[str, str] = {}
    for key, value in my_dictionary.items():
        if value in inverted:
            raise KeyError(f"Duplicate value found: {value}")
        inverted[value] = key
    return inverted


def count(input_list: list[str]) -> dict[str, int]:
    """Counts the number of times each string appears in the input list.

    Arguments:
        input_list (list[str]): A list of strings to count.

    Returns:
        dict[str, int]: A dictionary mapping each string to its frequency.
    """
    Count_dictionary: dict[str, int] = {}

    for item in input_list:
        if item in Count_dictionary:
            Count_dictionary[item] += 1
        else:
            Count_dictionary[item] = 1

    return Count_dictionary


def favorite_color(name_color_dict: dict[str, str]) -> str:
    """Returns the color that appears most frequently in the input dictionary.

    If there's a tie for most popular color, returns the first one encountered.
    """
    color_counts: dict[str, int] = {}

    # Count the frequency of each color
    for color in name_color_dict.values():
        if color in color_counts:
            color_counts[color] += 1
        else:
            color_counts[color] = 1

    most_frequent_color = ""
    highest_count = 0

    # Loop again in order of appearance to break ties by order
    for color in name_color_dict.values():
        if color_counts[color] > highest_count:
            most_frequent_color = color
            highest_count = color_counts[color]

    return most_frequent_color


def bin_len(words: list[str]) -> dict[int, set[str]]:
    """Bins words by length into a dictionary"""
    binned: dict[int, set[str]] = {}
    for word in words:
        length = len(word)
        if length in binned:
            binned[length].add(word)
        else:
            binned[length] = {word}

    return binned

"""Exercise 03 Testing the Dictionary"""

__author__: str = "730431256"

import pytest
from exercises.ex03.dictionary import invert, favorite_color, count, bin_len


# Edge case: Duplicate values should raise a key error
def test_invert_edge_case_duplicate_values() -> None:
    with pytest.raises(KeyError):
        invert({"kris": "jordan", "michael": "jordan"})


# Use Case 1: Invert a dictionary with multiple key-value pairs
def test_invert_use_case_multiple_pairs() -> None:
    assert invert({"a": "z", "b": "y", "c": "x"}) == {"z": "a", "y": "b", "x": "c"}


# Use Case 2: Invert a dictionary with a single key-value pair
def test_invert_use_case_single_pair() -> None:
    assert invert({"apple": "cat"}) == {"cat": "apple"}


# Edge Case: Empty list
def test_count_edge_case_empty_list() -> None:
    Count_dictionary = []
    assert count(Count_dictionary) == {}


# Use Case 1: List with repeated items
def test_count_use_case_repeated_items() -> None:
    Count_dictionary = ["apple", "banana", "apple", "apple", "banana"]
    assert count(Count_dictionary) == {"apple": 3, "banana": 2}


# Use Case 2: List with all unique items
def test_count_use_case_all_unique() -> None:
    Count_dictionary = ["red", "blue", "green"]
    assert count(Count_dictionary) == {"red": 1, "blue": 1, "green": 1}


# Edge Case: Empty dictionary should return empty string
def test_favorite_color_edge_case_empty() -> None:
    assert favorite_color({}) == ""


# Use Case 1: One color clearly most common
def test_favorite_color_use_case_one_clear_winner() -> None:
    assert (
        favorite_color(
            {"Alice": "blue", "Bob": "green", "Charlie": "blue", "Diana": "blue"}
        )
        == "blue"
    )


# Use Case 2: Tie between two colors, return first one encountered
def test_favorite_color_use_case_tie() -> None:
    assert (
        favorite_color(
            {"Alice": "blue", "Bob": "green", "Charlie": "green", "Diana": "blue"}
        )
        == "blue"
    )  # Both appear 2x, but blue appears first


# Edge Case: Empty list returns an empty dictionary
def test_bin_len_edge_case_empty() -> None:
    assert bin_len([]) == {}


# Use Case 1: Words of different lengths
def test_bin_len_use_case_varied_lengths() -> None:
    assert bin_len(["the", "quick", "fox"]) == {3: {"the", "fox"}, 5: {"quick"}}


# Use Case 2: Duplicate words of the same length
def test_bin_len_use_case_duplicates() -> None:
    assert bin_len(["the", "the", "fox"]) == {3: {"the", "fox"}}

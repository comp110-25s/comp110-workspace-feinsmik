"""Functions for working with a recursive singly-linked list."""

from __future__ import annotations

"""Linked list for EX05."""

__author__: str = "730431256"


class Node:
    """A node in a linked list."""

    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None = None) -> None:
        """Initialize the node with a value and a pointer to the next node."""
        self.value = value
        self.next = next

    def __str__(self) -> str:
        """Return a string representation of the linked list."""
        if self.next is None:
            return f"{self.value} -> None"
        else:
            return f"{self.value} -> {self.next}"

    __repr__ = __str__
    """Return a string representation of the linked list."""


def value_at(head: Node | None, index: int) -> int:
    """Return the value at the given index in the linked list."""
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    if index == 0:
        return head.value
    return value_at(head.next, index - 1)  # Hint 0


def max(head: Node | None) -> int:
    """Return the maximum value in the linked list."""
    if head is None:
        raise ValueError("Cannot call max with None.")
    if head.next is None:
        return head.value
    max_of_rest = max(head.next)
    if head.value > max_of_rest:
        return head.value
    else:
        return max_of_rest


def linkify(items: list[int]) -> Node | None:
    """Convert a list of integers into a linked list."""
    if items == []:
        return None
    return Node(items[0], linkify(items[1:]))


def scale(head: Node | None, factor: int) -> Node | None:
    """Scale the values in the linked list by a given factor."""
    if head is None:
        return None
    return Node(head.value * factor, scale(head.next, factor))

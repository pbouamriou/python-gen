"""Module containing examples of Python generic types."""

from typing import Any, Generic, TypeVar, Union

from typing_extensions import Protocol

# Type variables for generics
T = TypeVar("T")
U = TypeVar("U")
V = TypeVar("V")

# Type variable with constraints
Comparable = TypeVar("Comparable", bound=Union[int, float, str])


class Container(Generic[T]):
    """Simple generic class to store a typed value."""

    def __init__(self, value: T) -> None:
        """Initialize the container with a value."""
        self._value = value

    def get_value(self) -> T:
        """Return the stored value."""
        return self._value

    def set_value(self, value: T) -> None:
        """Set a new value."""
        self._value = value


class Pair(Generic[T, U]):
    """Generic class to store a pair of values of different types."""

    def __init__(self, first: T, second: U) -> None:
        """Initialize the pair with two values."""
        self._first = first
        self._second = second

    def get_first(self) -> T:
        """Return the first value."""
        return self._first

    def get_second(self) -> U:
        """Return the second value."""
        return self._second

    def swap(self) -> "Pair[U, T]":
        """Return a new pair with swapped values."""
        return Pair(self._second, self._first)


class Stack(Generic[T]):
    """Generic stack implementation."""

    def __init__(self) -> None:
        """Initialize an empty stack."""
        self._items: list[T] = []

    def push(self, item: T) -> None:
        """Add an element to the top of the stack."""
        self._items.append(item)

    def pop(self) -> T:
        """Remove and return the element from the top of the stack."""
        if not self._items:
            raise IndexError("Stack is empty")
        return self._items.pop()

    def peek(self) -> T:
        """Return the element from the top without removing it."""
        if not self._items:
            raise IndexError("Stack is empty")
        return self._items[-1]

    def is_empty(self) -> bool:
        """Check if the stack is empty."""
        return len(self._items) == 0

    def size(self) -> int:
        """Return the size of the stack."""
        return len(self._items)


class ComparableProtocol(Protocol):
    """Protocol for comparable types."""

    def __lt__(self, other: Any) -> bool:
        """Compare if self is less than other."""

    def __le__(self, other: Any) -> bool:
        """Compare if self is less than or equal to other."""


class SortedList(Generic[Comparable]):
    """Generic sorted list for comparable types."""

    def __init__(self) -> None:
        """Initialize an empty sorted list."""
        self._items: list[Comparable] = []

    def add(self, item: Comparable) -> None:
        """Add an element while maintaining sorted order."""
        self._items.append(item)
        self._items.sort()

    def get_items(self) -> list[Comparable]:
        """Return all sorted elements."""
        return self._items.copy()

    def get_min(self) -> Comparable:
        """Return the minimum element."""
        if not self._items:
            raise ValueError("List is empty")
        return self._items[0]

    def get_max(self) -> Comparable:
        """Return the maximum element."""
        if not self._items:
            raise ValueError("List is empty")
        return self._items[-1]


# Generic functions
def identity(value: T) -> T:
    """Generic function that returns the input value."""
    return value


def swap_pair(pair: Pair[T, U]) -> Pair[U, T]:
    """Generic function that swaps the elements of a pair."""
    return Pair(pair.get_second(), pair.get_first())


def merge_containers(
    container1: Container[T], container2: Container[U]
) -> Pair[T, U]:
    """Generic function that merges two containers."""
    return Pair(container1.get_value(), container2.get_value())


# Generic type aliases
NumberContainer = Container[Union[int, float]]
StringContainer = Container[str]

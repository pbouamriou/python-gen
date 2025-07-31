"""Unit tests for generic types."""

import pytest

from src.python_gen.generics import (
    Container,
    NumberContainer,
    Pair,
    SortedList,
    Stack,
    StringContainer,
    identity,
    merge_containers,
    swap_pair,
)


class TestContainer:
    """Tests for the Container class."""

    def test_container_int(self) -> None:
        """Test Container with an integer."""
        container = Container(42)
        assert container.get_value() == 42

    def test_container_string(self) -> None:
        """Test Container with a string."""
        container = Container("test")
        assert container.get_value() == "test"

    def test_container_list(self) -> None:
        """Test Container with a list."""
        test_list = [1, 2, 3]
        container = Container(test_list)
        assert container.get_value() == test_list

    def test_set_value(self) -> None:
        """Test the set_value method."""
        container = Container("initial")
        container.set_value("updated")
        assert container.get_value() == "updated"


class TestPair:
    """Tests for the Pair class."""

    def test_pair_creation(self) -> None:
        """Test pair creation."""
        pair = Pair("key", 123)
        assert pair.get_first() == "key"
        assert pair.get_second() == 123

    def test_pair_swap(self) -> None:
        """Test the swap method."""
        pair = Pair("first", "second")
        swapped = pair.swap()
        assert swapped.get_first() == "second"
        assert swapped.get_second() == "first"

    def test_pair_different_types(self) -> None:
        """Test pair with different types."""
        pair = Pair(42, "forty-two")
        assert isinstance(pair.get_first(), int)
        assert isinstance(pair.get_second(), str)


class TestStack:
    """Tests for the Stack class."""

    def test_empty_stack(self) -> None:
        """Test an empty stack."""
        stack = Stack[int]()
        assert stack.is_empty()
        assert stack.size() == 0

    def test_push_pop(self) -> None:
        """Test push and pop."""
        stack = Stack[int]()
        stack.push(1)
        stack.push(2)
        stack.push(3)

        assert stack.size() == 3
        assert stack.pop() == 3
        assert stack.size() == 2

    def test_peek(self) -> None:
        """Test the peek method."""
        stack = Stack[str]()
        stack.push("first")
        stack.push("second")

        assert stack.peek() == "second"
        assert stack.size() == 2  # peek doesn't remove the element

    def test_pop_empty_stack(self) -> None:
        """Test pop on an empty stack."""
        stack = Stack[int]()
        with pytest.raises(IndexError, match="Stack is empty"):
            stack.pop()

    def test_peek_empty_stack(self) -> None:
        """Test peek on an empty stack."""
        stack = Stack[int]()
        with pytest.raises(IndexError, match="Stack is empty"):
            stack.peek()


class TestSortedList:
    """Tests for the SortedList class."""

    def test_empty_sorted_list(self) -> None:
        """Test an empty sorted list."""
        sorted_list = SortedList[int]()
        assert len(sorted_list.get_items()) == 0

    def test_add_and_sort(self) -> None:
        """Test adding and automatic sorting."""
        sorted_list = SortedList[int]()
        sorted_list.add(5)
        sorted_list.add(2)
        sorted_list.add(8)
        sorted_list.add(1)

        assert sorted_list.get_items() == [1, 2, 5, 8]

    def test_get_min_max(self) -> None:
        """Test get_min and get_max methods."""
        sorted_list = SortedList[int]()
        sorted_list.add(10)
        sorted_list.add(5)
        sorted_list.add(15)

        assert sorted_list.get_min() == 5
        assert sorted_list.get_max() == 15

    def test_get_min_empty(self) -> None:
        """Test get_min on an empty list."""
        sorted_list = SortedList[int]()
        with pytest.raises(ValueError, match="List is empty"):
            sorted_list.get_min()

    def test_get_max_empty(self) -> None:
        """Test get_max on an empty list."""
        sorted_list = SortedList[int]()
        with pytest.raises(ValueError, match="List is empty"):
            sorted_list.get_max()

    def test_string_sorting(self) -> None:
        """Test string sorting."""
        sorted_list = SortedList[str]()
        sorted_list.add("zebra")
        sorted_list.add("apple")
        sorted_list.add("banana")

        assert sorted_list.get_items() == ["apple", "banana", "zebra"]


class TestFunctions:
    """Tests for generic functions."""

    def test_identity(self) -> None:
        """Test the identity function."""
        assert identity("test") == "test"
        assert identity(123) == 123
        assert identity([1, 2, 3]) == [1, 2, 3]

    def test_swap_pair(self) -> None:
        """Test the swap_pair function."""
        original = Pair("first", "second")
        swapped = swap_pair(original)

        assert swapped.get_first() == "second"
        assert swapped.get_second() == "first"

    def test_merge_containers(self) -> None:
        """Test the merge_containers function."""
        container1 = Container("test")
        container2 = Container(42)
        merged = merge_containers(container1, container2)

        assert merged.get_first() == "test"
        assert merged.get_second() == 42


class TestTypeAliases:
    """Tests for type aliases."""

    def test_number_container(self) -> None:
        """Test NumberContainer."""
        int_container = NumberContainer(42)
        float_container = NumberContainer(3.14)

        assert int_container.get_value() == 42
        assert float_container.get_value() == 3.14

    def test_string_container(self) -> None:
        """Test StringContainer."""
        str_container = StringContainer("Hello")
        assert str_container.get_value() == "Hello"

#!/usr/bin/env python3
"""Main entry point for testing generic types."""

from python_gen.generics import (
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


def test_container() -> None:
    """Test the generic Container class."""
    print("=== Test Container ===")

    # Container with int
    int_container = Container(42)
    print(f"Int container value: {int_container.get_value()}")

    # Container with string
    str_container = Container("Hello, Generics!")
    print(f"String container value: {str_container.get_value()}")

    # Container with list
    list_container = Container([1, 2, 3, 4, 5])
    print(f"List container value: {list_container.get_value()}")


def test_pair() -> None:
    """Test the generic Pair class."""
    print("\n=== Test Pair ===")

    # Int/string pair
    int_str_pair = Pair(42, "forty-two")
    print(f"Pair: ({int_str_pair.get_first()}, {int_str_pair.get_second()})")

    # String/float pair
    str_float_pair = Pair("pi", 3.14159)
    print(f"Pair: ({str_float_pair.get_first()}, {str_float_pair.get_second()})")

    # Test swap
    swapped = int_str_pair.swap()
    print(f"Swapped pair: ({swapped.get_first()}, {swapped.get_second()})")


def test_stack() -> None:
    """Test the generic Stack class."""
    print("\n=== Test Stack ===")

    # Integer stack
    int_stack = Stack[int]()
    int_stack.push(1)
    int_stack.push(2)
    int_stack.push(3)

    print(f"Stack size: {int_stack.size()}")
    print(f"Top element: {int_stack.peek()}")
    print(f"Popped element: {int_stack.pop()}")
    print(f"Stack size after pop: {int_stack.size()}")

    # String stack
    str_stack = Stack[str]()
    str_stack.push("first")
    str_stack.push("second")
    str_stack.push("third")

    print(f"String stack: {[str_stack.pop() for _ in range(str_stack.size())]}")


def test_sorted_list() -> None:
    """Test the generic SortedList class."""
    print("\n=== Test SortedList ===")

    # Sorted list of integers
    int_list = SortedList[int]()
    int_list.add(5)
    int_list.add(2)
    int_list.add(8)
    int_list.add(1)
    int_list.add(9)

    print(f"Sorted integers: {int_list.get_items()}")
    print(f"Min: {int_list.get_min()}")
    print(f"Max: {int_list.get_max()}")

    # Sorted list of strings
    str_list = SortedList[str]()
    str_list.add("zebra")
    str_list.add("apple")
    str_list.add("banana")
    str_list.add("cherry")

    print(f"Sorted strings: {str_list.get_items()}")


def test_functions() -> None:
    """Test generic functions."""
    print("\n=== Test Functions ===")

    # Test identity function
    result1 = identity("test")
    result2 = identity(123)
    print(f"Identity string: {result1}")
    print(f"Identity int: {result2}")

    # Test swap_pair function
    original_pair = Pair("hello", 42)
    swapped_pair = swap_pair(original_pair)
    print(f"Original: ({original_pair.get_first()}, {original_pair.get_second()})")
    print(f"Swapped: ({swapped_pair.get_first()}, {swapped_pair.get_second()})")

    # Test merge_containers function
    container1 = Container("test")
    container2 = Container(123)
    merged = merge_containers(container1, container2)
    print(f"Merged: ({merged.get_first()}, {merged.get_second()})")


def test_type_aliases() -> None:
    """Test generic type aliases."""
    print("\n=== Test Type Aliases ===")

    # NumberContainer
    num_container = NumberContainer(3.14)
    print(f"Number container: {num_container.get_value()}")

    # StringContainer
    str_container = StringContainer("Hello")
    print(f"String container: {str_container.get_value()}")


def main() -> None:
    """Main function that executes all tests."""
    print("🚀 Python Generic Types Test")
    print("=" * 50)

    try:
        test_container()
        test_pair()
        test_stack()
        test_sorted_list()
        test_functions()
        test_type_aliases()

        print("\n✅ All tests executed successfully!")

    except Exception as e:
        print(f"\n❌ Error during execution: {e}")
        raise


if __name__ == "__main__":
    main()

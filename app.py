def add_numbers(left, right):
    """Складывает только два целых числа."""
    if not isinstance(left, int) or isinstance(left, bool):
        raise ValueError("left must be an integer")
    if not isinstance(right, int) or isinstance(right, bool):
        raise ValueError("right must be an integer")
    return left + right

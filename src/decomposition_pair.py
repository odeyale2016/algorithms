
def decomposition_pair(numbers, total):  # O(n)
    """Decomposition pair

    Given a list of numbers and a number k, return whether any two numbers from the
    list add up to k.

    >>> decomposition_pair([10, 15, 3, 7], 17)
    True

    >>> decomposition_pair([10, 15, 3, 7], 19)
    False
    """

    seen = set()
    for number in numbers:
        if total - number in seen:
            return True
        seen.add(number)
    return False

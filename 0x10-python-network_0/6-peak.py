#!/usr/bin/python3
def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.

    Args:
        list_of_integers (list): A list of unsorted integers.

    Returns:
        int: A peak value in the list.

    Complexity:
        The algorithm has a time complexity of O(log n), where n is the length
        of the list. This is achieved by using a binary search algorithm to
        locate the peak value.
    """
    # Check for edge cases
    if not list_of_integers:
        return None

    # Binary search algorithm to find a peak
    left, right = 0, len(list_of_integers) - 1
    while left < right:
        mid = (left + right) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return list_of_integers[left]

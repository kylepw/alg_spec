from random import randrange

"""
    rselect.py
    ~~~~~~~~~~
    Implementation of RSelect.
"""

def _choose_pivot(array, low, high):
    """Choose random pivot and move to front."""
    # Choose pivot and move to front
    p = randrange(low, high)
    array[low], array[p] = array[p], array[low]

def _partition(array, low, high):
    """
        Sort values lower < pivot index < higher.

        Args:
            array (list): unsorted list with pivot in [0]
            low (int): lowest index
            high (int): highest index

        Returns (int): index of sorted value
    """
    pivot = array[low]
    i = low + 1
    for j in range(low + 1, high):
        if array[j] < pivot:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[low], array[i - 1] = array[i - 1], array[low]

    return i - 1

def rs(array, i, low=None, high=None):
    """
    Returns ith minimum value of array.

    Args:
        array (list): unsorted integers
        i (int): index of ith smallest value

    >>> rs([5, 4, 100, 0], 2)
    4

    Returns: (int) ith smallest value
    """
    if low is None:
        low = 0
    if high is None:
        high = len(array)
    if low < high:
        _choose_pivot(array, low, high)
        j = _partition(array, low, high)
        if j == i - 1:
            return array[j]
        if j > i - 1:
            return rs(array, i, low=low, high=j)
        else:
            return rs(array, i, low=j + 1, high=high)

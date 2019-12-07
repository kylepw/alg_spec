from random import randrange

"""
    rselect.py
    ~~~~~~~~~~
    Implementation of RSelect.
"""


def _partition(array, low, high, pindex):
    """Sort values lower < pivot index < higher."""
    return


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
    if low < high:
        p = randrange(low, high)
        # partition
        j = _partition(array, low, high)
        if j == i:
            return array[j]
        if j > i:
            partition(array, i, low=low, high=j)
        else:
            partition(array, j - i, low=j + 1, high=high)
    return

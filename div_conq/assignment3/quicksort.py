"""Randomized quicksort implementation."""
import argparse
import math
from random import randrange
from statistics import median


def _rand_pivot(low, high, array=None):
    """Return random pivot index."""
    return randrange(low, high)


def _left_pivot(low, high, array=None):
    """Return leftmost index."""
    return low


def _right_pivot(low, high, array=None):
    """Return rightmost index."""
    return high - 1


def _mid_pivot(low, high, array):
    """Return 'median of three' values."""
    if (high - low) % 2 == 0:
        mid = low + (high - low) // 2 - 1
    else:
        mid = low + (high - low) // 2

    if (array[mid] <= array[low] <= array[high - 1]) or (
        array[high - 1] <= array[low] <= array[mid]
    ):
        mindex = low
    elif (array[low] <= array[mid] <= array[high - 1]) or (
        array[high - 1] <= array[mid] <= array[low]
    ):
        mindex = mid
    else:
        mindex = high - 1

    return mindex


def _partition(array, low, high, pindex):
    """Sort values lower < pivot index < higher."""

    # Place pivot in front
    array[low], array[pindex] = array[pindex], array[low]

    i = low + 1
    for j in range(low + 1, high):
        if array[j] < array[low]:
            array[i], array[j] = array[j], array[i]
            i += 1

    # Place pivot in right place
    pindex = i - 1
    array[low], array[pindex] = array[pindex], array[low]

    return pindex


def qsort(array, low=None, high=None, choose_pivot=None):
    """Apply quicksort on array.
        ::array::   list of unsorted values
        ::low::     leftmost index
        ::high::    rightmost index
        ::choose_pivot:: _rand_pivot, _left_pivot, _right_pivot, _mid_pivot

        Return: number of comparisons
    """
    if not isinstance(array, list):
        raise ValueError
    if low is None:
        low = 0
    if high is None:
        high = len(array)
    if choose_pivot is None:
        choose_pivot = _rand_pivot
    if low < high:
        pindex = _partition(array, low, high, choose_pivot(low, high, array))
        return (
            high
            - low
            - 1
            + qsort(array, low, pindex, choose_pivot)
            + qsort(array, pindex + 1, high, choose_pivot)
        )
    return 0


def get_parser():
    parser = argparse.ArgumentParser(
        description='Apply quicksort on unsorted integers in file, one integer per line'
    )
    parser.add_argument('filename', metavar='file', help='file of integers')
    return parser


def main():
    parser = get_parser()
    args = vars(parser.parse_args())
    try:
        with open(args['filename']) as f:
            values = [int(line) for line in f.readlines() if line.strip() != '']
        for title, pivot in (
            ('left:', _left_pivot),
            ('right:', _right_pivot),
            ('random:', _rand_pivot),
            ('mid:', _mid_pivot),
        ):
            copy = values[:]
            print(title, qsort(copy, choose_pivot=pivot))
    except IOError:
        print(f"Failed to open {args['file']}")
        exit(1)


if __name__ == '__main__':
    main()

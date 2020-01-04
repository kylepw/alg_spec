"""Median maintenance algorithm implementation.

The goal of this problem is to implement the "Median Maintenance" algorithm
(covered in the Week 3 lecture on heap applications). The text file contains a
list of the integers from 1 to 10000 in unsorted order; you should treat this
as a stream of numbers, arriving one by one. Letting Xi denote the i-th number
of the file, the k-th median Mk is defined as the median of the numbers
X1,...,Xk. (So, if k is odd, then Mk is ((k+1)/2)th smallest number among
X1,...,Xk; if k is even, then Mk is the (k/2)th smallest number among X1,...,Xk.)

Return the sum of these 10000 medians, modulo 10000 (i.e., only the last 4 digits).
That is, you should compute (M1 + M2 + M3 + ... + M10000) mod 10000.

Optional: compare the performance achieved by heap-based and search-tree-based
implementations of the algorithm.

"""
import argparse
from heapq import heapify, heappop, heappush, nlargest, nsmallest


def get_medians(nums):
    """Return medians from X0 to Xi for each i-th number."""

    if len(nums) < 2:
        return nums

    # max heap
    smaller = []

    # min heap
    bigger = []

    medians = []

    for x in nums:
        if len(smaller) == 0 and len(bigger) == 0:
            heappush(smaller, x)
            medians.append(x)
            continue

        s = nlargest(1, smaller)[0]

        # Insert into heap
        if x <= s:
            heappush(smaller, x)
            s = nlargest(1, smaller)[0]
        else:
            heappush(bigger, x)

        # Rebalance
        if len(smaller) > len(bigger) + 1:
            diff = len(smaller) - len(bigger)
            for _ in range(diff - 1):
                smaller.remove(s)
                heappush(bigger, s)
                s = nlargest(1, smaller)[0]
        elif len(bigger) > len(smaller) + 1:
            diff = len(bigger) - len(smaller)
            for _ in range(diff - 1):
                heappush(smaller, heappop(bigger))

        # Append median
        if len(smaller) >= len(bigger):
            medians.extend(nlargest(1, smaller))
        else:
            medians.extend(nsmallest(1, bigger))

    return medians


def read_nums(filename):
    try:
        with open(filename) as f:
            nums = f.readlines()
    except IOError:
        raise f'Failed to read data from {filename}'

    return [int(n) for n in nums if not n.startswith('#')]


def get_parser():
    parser = argparse.ArgumentParser(
        description='''
            Median maintenance algorithm implementation. Return sum of X medians
            from file with X number of integers, one per line. For example, the
            median at the i-th number is median of X1,...,Xi numbers.
        '''
    )
    parser.add_argument(
        'filename', metavar='file', help='file with X number of integers, one per line'
    )
    return parser


def main():
    parser = get_parser()
    args = vars(parser.parse_args())

    filename = args['filename']
    nums = read_nums(filename)

    total = sum(get_medians(nums))

    print(total % 10000)


if __name__ == '__main__':
    main()

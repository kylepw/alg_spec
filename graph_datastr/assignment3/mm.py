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
    print(filename)


if __name__ == '__main__':
    main()

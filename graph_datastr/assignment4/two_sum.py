"""2-SUM algorithm implementation.

    Compute the number of target values t in the interval
    [-10000,10000] (inclusive) such that there are distinct numbers
    x, y in the input file that satisfy x + y = t.

"""
import argparse
from bisect import bisect_left as bl


def find_tsums(nums: set):
    """Return number of discinct x, y pairs that add up to a number -10000 to 10000."""
    found = {}
    for i in range(-10000, 10001):
        found[i] = False

    for x in nums:
        for y in [
            y
            for y in nums[bl(nums, -10000 - x) : bl(nums, 10000 - x) + 1]
            if x + y in found and not found[x + y]
        ]:
            print(f'{x} + {y} = {x + y}')
            found[x + y] = True

    return sum([1 for t in found if found[t]])


def load_nums(filename):
    """Load sorted list of distinct numbers into list"""
    nums = set()
    try:
        with open(filename) as f:
            for line in f:
                nums.add(int(line.strip()))
    except IOError:
        print('Failed to read data from {filename}')
        raise

    nums = list(nums)

    return sorted(nums)


def get_parser():
    parser = argparse.ArgumentParser(
        description='''
        2-SUM: Computes the number of target values t in the interval
        [-10000,10000] (inclusive) such that there are distinct numbers
        x, y in the input file that satisfy x + y = t.'''
    )
    parser.add_argument(
        'filename', metavar='file', help='file with one integer per line'
    )
    return parser


def main():
    parser = get_parser()
    args = vars(parser.parse_args())
    filename = args['filename']

    print(find_tsums(load_nums(filename)))


if __name__ == '__main__':
    main()

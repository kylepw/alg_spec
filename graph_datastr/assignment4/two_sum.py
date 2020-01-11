"""2-SUM algorithm implementation.

    Compute the number of target values t in the interval
    [-10000,10000] (inclusive) such that there are distinct numbers
    x, y in the input file that satisfy x + y = t.

"""
import argparse

def load_nums(filename):
    nums = {}
    try:
        with open(filename) as f:
            for i, line in enumerate(f):
                nums[int(line.strip())] = i
    except IOError:
        print('Failed to read data from {filename}')
        raise

    return nums



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

    nums = load_nums(filename)
    print(nums)


if __name__ == '__main__':
    main()

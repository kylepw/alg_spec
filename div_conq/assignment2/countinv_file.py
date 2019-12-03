"""Count inversions of unsorted integers in file, one per line.

    Usage:
        $ python countinv-file.py file.txt
        10001
"""
import argparse


def _merge_and_count_split_inv(left, right):
    """Return merged, sorted array and number of split inversions."""

    max_left, max_right = len(left), len(right)
    if max_left == 0 or max_right == 0:
        return left + right, 0
    merged = []
    inv_count = 0

    i = j = 0
    while i < max_left and j < max_right:
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            # Count inversions
            inv_count += max_left - i

    while i < max_left:
        merged.append(left[i])
        i += 1

    while j < max_right:
        merged.append(right[j])
        j += 1

    return merged, inv_count


def count_inversions(array):
    """Return sorted int array and number of inversions."""
    if not isinstance(array, list) or not all([isinstance(x, int) for x in array]):
        return None, None
    size = len(array)

    # Base case
    if size < 2:
        return array, 0

    left_sorted, left_inv = count_inversions(array[: size // 2])
    right_sorted, right_inv = count_inversions(array[size // 2 :])
    all_sorted, split_inv = _merge_and_count_split_inv(left_sorted, right_sorted)

    return (all_sorted, left_inv + right_inv + split_inv)


def get_parser():
    parser = argparse.ArgumentParser(
        description='Count inversions of unsorted integers in file, one integer per line'
    )
    parser.add_argument('filename', metavar='file', help='file of integers')
    return parser


def main():
    parser = get_parser()
    args = vars(parser.parse_args())
    try:
        with open(args['filename']) as f:
            values = [int(line) for line in f.readlines()]
        _, inversions = count_inversions(values)
        print(inversions)
    except IOError:
        print(f"Failed to open {args['file']}")
        exit(1)


if __name__ == '__main__':
    main()

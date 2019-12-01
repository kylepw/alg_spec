"""Count inversions of unsorted array of integers."""


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


if __name__ == '__main__':
    print('Enter integers separated by a space (^C to exit):')
    print('Ex) 1 3 30 -2 11 23\n([-2, 1, 3, 11, 23, 30], 15)')
    while True:
        try:
            array = [int(x) for x in input().split()]
            srted, inversions = count_inversions(array)
            if (srted, inversions) == (None, None):
                continue
            print(srted, inversions)
        except ValueError:
            print('\nInvalid!')
        except KeyboardInterrupt:
            print('\nSee you!')
            exit(0)

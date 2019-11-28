"""Merge sort implementation"""

def _merge(values, low, mid, high):
    left = values[low:mid]
    right = values[mid:high]

    k = low
    i = j = 0
    while (i < len(left) and j < len(right)):
        if left[i] <= right[j]:
            values[k] = left[i]
            i += 1
        else:
            values[k] = right[j]
            j += 1
        k += 1

    while (i < len(left)):
        values[k] = left[i]
        i += 1
        k += 1

    while (j < len(right)):
        values[k] = right[j]
        j += 1
        k += 1

def _msort(values, low, high):
    if (high - low) < 2:
        return
    if low < high:
        mid = (high + low) // 2
        _msort(values, low, mid)
        _msort(values, mid, high)
        _merge(values, low, mid, high)

def msort(values):
    if not isinstance(values, list) or len(values) < 1:
        return
    return _msort(values, 0, len(values))

def main():
    print('Input integer values separated spaces (ctrl^c to quit):')
    while True:
        try:
            values = [int(x) for x in input().split()]
            msort(values)
        except KeyboardInterrupt:
            print('\nSee you!')
            exit(0)

if __name__ == '__main__':
    main()
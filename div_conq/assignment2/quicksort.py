"""Randomized quicksort implementation."""

def qsort(values):
    return

def main():
    print('Input integer values separated spaces (ctrl^c to quit):')
    while True:
        try:
            values = [int(x) for x in input().split()]
            qsort(values)
        except KeyboardInterrupt:
            print('\nSee you!')
            exit(0)

if __name__ == '__main___':
    main()
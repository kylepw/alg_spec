"""Karatsuba implementation"""


def kmult(x, y):
    """ Returns recursive Karatsuba solution to x * y
        where both x and y have n-digits.

        Where x (ab) and y (cd):
        x * y = 10**nac + 10**n/2(ad + bc)
    """
    if x < 0 or y < 0:
        print('Numbers must be positive!')
        return -1

    if x < 10 or y < 10:
        return x * y

    # Halve it to take care of even and odd digits
    n = max(len(str(x)), len(str(y))) // 2

    a, b = (x // 10 ** n, x % 10 ** n)
    c, d = (y // 10 ** n, y % 10 ** n)
    ac = kmult(a, c)
    bd = kmult(b, d)
    ab_plus_bc = kmult(a + b, c + d) - ac - bd

    return ac * 10 ** (2 * n) + ab_plus_bc * 10 ** n + bd


def main():
    print('Enter two positive integers separated by a space (^C to exit):')
    print('Ex) 1234 1234\n1522756')
    while True:
        try:
            x, y = [int(x) for x in input().split()]
            result = kmult(x, y)
            if result == -1:
                continue
            print(kmult(x, y))

        except ValueError as e:
            print('\nInvalid!')
            raise e
        except KeyboardInterrupt:
            print('\nSee you!')
            exit(0)


if __name__ == '__main__':
    main()

"""
    Programming Assigment #1
    ~~~~~~~~~~~~~~~~~~~~~~~~
    In this programming assignment you will implement one or more of the
    integer multiplication algorithms described in lecture.

    To get the most out of this assignment, your program should restrict
    itself to multiplying only pairs of single-digit numbers. You can
    implement the grade-school algorithm if you want, but to get the most
    out of the assignment you'll want to implement recursive integer
    multiplication and/or Karatsuba's algorithm.

    So: what's the product of the following two 64-digit numbers?

    3141592653589793238462643383279502884197169399375105820974944592

    2718281828459045235360287471352662497757247093699959574966967627
"""

def kmult(x, y):
    """Return product of x * y with Karatsuba magic."""
    if x < 0 or y < 0:
        print('Numbers must be positive!')
        return -1

    # Base case
    if x < 10 or y < 10:
        return x * y

    # Divide by 2 to handle odd and even digit numbers
    n = max(len(str(x)), len(str(y))) // 2
    n1 = max(len(str(x)), len(str(y)))

    a, b = (x // 10 ** n, x % 10 ** n)
    c, d = (y // 10 ** n, y % 10 ** n)

    A = kmult(a, c)
    D = kmult(b, d)
    E = kmult(a + b, c + d) - A - D
    
    return A * 10**(n*2) + E * 10**(n) + D


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
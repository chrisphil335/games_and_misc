import argparse
import math


PI = math.pi


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        # TODO: look up ValueError
        return "Can't divide by 0!"
    return a / b


def power(a, b):
    return a ** b


def square(a):
    return a ** 2


def sqrt(a):
    return math.sqrt(a)


def sin(theta):
    return math.sin(theta)


def cos(theta):
    return math.cos(theta)


def tan(theta):
    return math.tan(theta)
    

def test():
    print(f"2 + 2 = {add(2, 2)}")
    print(f"5 - 2 = {subtract(5, 2)}")
    print(f"3 * 3 = {multiply(3, 3)}")
    print(f"9 / 3 = {divide(9, 3)}")
    print(f"10 / 0 = {divide(10, 0)}")
    print(f"2 ** 4 = {power(2, 4)}")
    print(f"square(4) = {square(4)}")
    print(f"sqrt(16) = {sqrt(16)}")
    print(f"sin(PI / 2) = {sin(PI / 2)}")
    print(f"cos(PI) = {cos(PI)}")
    print(f"tan(PI / 4) = {tan(PI / 4)}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("square", type = int,
                        help = "display a square of a given number")
    parser.add_argument("-v", "--verbosity", type = int, choices = [0, 1, 2],
                        help = "increase output verbosity")
    args = parser.parse_args()
    answer = args.square ** 2
    if args.verbosity == 2:
        print(f"the square of {args.square} equals {answer}")
    elif args.verbosity == 1:
        print(f"{args.square}^2 == {answer}")
    else:
        print(answer)

if __name__ == "__main__":
    main()
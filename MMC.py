import sys
from math import gcd


def main():
    a, b = map(int, sys.stdin.read().split()[:2])

    mdc = gcd(a, b)  # algoritmo de Euclides

    if mdc == 0:  # a e b iguais a 0
        print(0)
        return

    mmc = abs((a // mdc) * b)
    print(mmc)


if __name__ == "__main__":
    main()

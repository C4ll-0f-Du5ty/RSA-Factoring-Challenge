import sys
import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def pollards_rho(n):
    x = 2
    y = 2
    d = 1
    f = lambda x: (x**2 + 1) % n

    while d == 1:
        x = f(x)
        y = f(f(y))
        d = gcd(abs(x - y), n)

    return d

def factorize_rsa_number(n):
    factors = []
    while n > 1:
        factor = pollards_rho(n)
        while n % factor == 0:
            factors.append(factor)
            n //= factor

    return factors

def main():
    try:
        filename = sys.argv[1]
        with open(filename) as file:
            for line in file:
                n = int(line.strip())
                factors = factorize_rsa_number(n)
                print(f"{n}={'*'.join(map(str, factors))}")
    except (IndexError, FileNotFoundError):
        print("Usage: python rsa.py <filename>")

if __name__ == "__main__":
    main()

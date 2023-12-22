import sys
import math

def factorize(n):
    # Check if the number is even
    if n % 2 == 0:
        return 2, n // 2

    # If the number is not even, start checking odd numbers
    for i in range(3, math.isqrt(n) + 1, 2):
        if n % i == 0:
            return i, n // i

    # If no factor found, the number is a prime
    return n, 1

def main():
    # Open the file
    with open(sys.argv[1], 'r') as file:
        for line in file:
            # Read each line (number)
            n = int(line.strip())
            # Factorize the number
            p, q = factorize(n)
            # Print the result
            print(f"{n}={p}*{q}")

if __name__ == "__main__":
    main()

#!/usr/bin/python3
import math
import sys

def factorize(num):
    factors = set()

    # Handle divisibility by 2 separately
    while num % 2 == 0:
        factors.add(2)
        num //= 2

    # Iterate over odd numbers starting from 3
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        while num % i == 0:
            factors.add(i)
            num //= i

    # If num is a prime number greater than 2
    if num > 2:
        factors.add(num)

    return factors

def main():
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    input_file = sys.argv[1]

    with open(input_file, 'r') as file:
        for line in file:
            num = int(line.strip())
            factors = factorize(num)
            print(f"{num}={'*'.join(map(str, factors))}")

if __name__ == "__main__":
    main()

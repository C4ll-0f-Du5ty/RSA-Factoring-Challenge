import os
import time

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def factor_rsa_files(directory):
    start_time = time.time()
    for filename in os.listdir(directory):
        if filename.startswith("rsa-"):
            with open(os.path.join(directory, filename), 'r') as file:
                n = int(file.read())
                factors = prime_factors(n)
                print(f"{filename}: {n} = {factors[0]}*{factors[1]}")
                if time.time() - start_time > 5:
                    print("5 seconds have passed. Stopping...")
                    break

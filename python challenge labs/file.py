#!/usr/bin/env python3

# Script: primes_1_to_250.py
# Purpose: Find and store all prime numbers between 1 and 250

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def main():
    # Find primes between 1 and 250
    primes = [num for num in range(1, 251) if is_prime(num)]

    # Display primes in the terminal
    print("Prime numbers between 1 and 250:")
    print(primes)

    # Save results into results.txt
    with open("results.txt", "w") as f:
        f.write("Prime numbers between 1 and 250:\n")
        f.write(", ".join(map(str, primes)))

    print("\nResults have been saved to results.txt")


if __name__ == "__main__":
    main()

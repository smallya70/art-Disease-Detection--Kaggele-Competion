"""
Singapore Toto number generator.
Each set: 6 unique numbers from 1 to 49.
Generates 6 sets.
"""

import random


def generate_toto_set():
    """Return one Toto set: 6 unique numbers from 1 to 49, sorted."""
    return sorted(random.sample(range(1, 50), 6))



def main():
    print("Singapore Toto - 6 sets of 6 numbers (1-49)\n")
    print("-" * 45)

    for i in range(6):
        numbers = generate_toto_set()
        print(f"Set {i + 1}:  {numbers}")

    print("-" * 45)
    print("Good luck!")


if __name__ == "__main__":
    main()

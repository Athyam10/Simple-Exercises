import random


def generate_trigger_numbers():
    """Return a list of 6 random trigger numbers between 1 and 6 inclusive."""
    return [random.randint(1, 6) for _ in range(6)]


def LLN(func, N):
    """Call func N times and count occurrences of numbers 1 through 6."""
    counts = {i: 0 for i in range(1, 7)}

    for _ in range(N):
        result = func()
        for value in result:
            if 1 <= value <= 6:
                counts[value] += 1

    return counts


if __name__ == "__main__":
    N = 10000
    counts = LLN(generate_trigger_numbers, N)
    print(f"Counts after {N} calls:")
    for number in range(1, 7):
        print(f"{number}: {counts[number]}")

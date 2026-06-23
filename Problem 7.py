"""Print a histogram of the values in a numeric list."""

def print_histogram(numbers):
    """Print a histogram showing the frequency of each number in the list."""
    counts = {}
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1

    for num in sorted(counts):
        print(f"{num}: {'*' * counts[num]}")


if __name__ == '__main__':
    input_values = input('Enter numbers separated by spaces: ').strip()
    if input_values:
        numbers = [int(value) for value in input_values.split()]
        print_histogram(numbers)
    else:
        print('No numbers provided.')

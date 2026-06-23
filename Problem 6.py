def count_digit_occurrences(text):
    """Return a list of counts for digits 0-9 in the given string."""
    counts = [0] * 10
    for ch in text:
        if ch.isdigit():
            counts[ord(ch) - ord('0')] += 1
    return counts

if __name__ == '__main__':
    example = input('Enter a string: ')
    print(count_digit_occurrences(example))

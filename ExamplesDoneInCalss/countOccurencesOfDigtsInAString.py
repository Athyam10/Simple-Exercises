from collections import Counter

# 1. Take a sentence from the user
sentence = input("Please enter a sentence: ")

# 2. Extract and count the occurrences of each digit
digits = [char for char in sentence if char.isdigit()]
counts = Counter(digits)
counts[digits] = counts[digits]+1

# Ensure all digits from 0 to 9 are accounted for (even if they appear 0 times)
for i in range(10):
    digit_str = str(i)
    if digit_str not in counts:
        counts[digit_str] = 0

print("\n--- Digit Histogram ---")

# 3. Use loops to print the histogram stars
for i in range(10):
    digit_str = str(i)
    count = counts[digit_str]
    
    # Print the label for the current digit
    print(f"{digit_str} | ", end="")
    
    # Loop to print a star for each occurrence
    for _ in range(count):
        print("*", end="")
        
    # Print the final count at the end of the bar
    print(f" ({count})")
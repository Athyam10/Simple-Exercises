# Write a function that finds the alpha character used the most in a given string.
def most_frequent_alpha_char(input_string):
    # Create a dictionary to count the frequency of each alpha character
    character_count = {}
    
    # Iterate through each character in the input string
    for word in input_string:
        # Check if the character is an alphabet letter
        if word.isalpha():
            # Convert to lowercase to make the count case-insensitive
            word = word.lower()
            # Update the count in the dictionary
            if word in character_count:
                character_count[word] += 1
            else:
                character_count[word] = 1
    
    # Find the character with the maximum frequency
    most_frequent_char = None
    max_count = 0
    
    for char, count in character_count.items():
        if count > max_count:
            max_count = count
            most_frequent_char = char 
    return most_frequent_char

# Example
input_string = "Hello World! This is a test string to find the most frequent alpha character."
result = most_frequent_alpha_char(input_string)
print(f"The most frequent alpha character is: '{result}'")

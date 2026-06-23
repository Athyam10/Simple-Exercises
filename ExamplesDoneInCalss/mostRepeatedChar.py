# write a function that finds out which alpha-character 
# is repeated the most.

def find_most_repeated_letter(text):
    # Step 1: Clean the text so we only look at lowercase letters
    cleaned_letters = []
    for character in text:
        # Check if it's a letter (ignores spaces, exclamation points, numbers, etc.)
        if character.isalpha():
            # Convert to lowercase so 'A' and 'a' are treated as the same letter
            lowercase_letter = character.lower()
            cleaned_letters.append(lowercase_letter)

    # Step 2: Count how many times each letter appears
    # We will use a dictionary, which is like a real-life dictionary where 
    # the "word" is the letter, and the "definition" is its count.
    letter_counts = {}
    for letter in cleaned_letters:
        if letter in letter_counts:
            # If the letter is already in our dictionary, add 1 to its count
            letter_counts[letter] = letter_counts[letter] + 1
        else:
            # If it's the first time we are seeing this letter, start its count at 1
            letter_counts[letter] = 1

    # Step 3: Find the letter with the highest count
    highest_count = 0
    most_repeated_letter = None

    # We look at each letter and its count one by one
    for letter, count in letter_counts.items():
        if count > highest_count:
            highest_count = count
            most_repeated_letter = letter

    return most_repeated_letter


# --- Let's test the function! ---
sample_text = "Hello World! Success is sweet.HASAAAAAAAAN"
winner = find_most_repeated_letter(sample_text)

print("The most repeated letter is:")
print(winner)

"""
1. Step-by-Step Breakdown
Let's look under the hood at the three major 
parts of this function.1. Cleaning the TextIf a user types "Hello 123!!", 
we don't care about the spaces, the numbers, or the exclamation points.
We create an empty list called cleaned_letters.We look at every single 
character one by one.character.isalpha() is a built-in Python trick that 
asks: "Is this a letter in the alphabet?" If it is True, Python moves 
inside the if statement.We use .lower() because if we didn't, Python 
would think uppercase 'S' and lowercase 's' are two completely different 
letters. We want them to count together!

2. The Counting Machine (Dictionaries)To count the letters, we use a 
Python Dictionary ({}). Think of a dictionary as a checklist of pairs: 
{"letter": count}.Imagine we are processing the word "bee":First 
letter is 'b'. It is not in letter_counts yet. So, Python goes to 
the else block and sets letter_counts['b'] = 1.Second letter is 
'e'. Not in the dictionary yet. Python sets 
letter_counts['e'] = 1.Third letter is 'e'. This time, 'e' is 
already in the dictionary! Python goes to the if block, grabs 
the old count ($1$), adds $1$ to it, and updates it: 
letter_counts['e'] = 2.By the end of this step, our dictionary 
for "Hello World!" would look something like this:
{'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}

3. Finding the WinnerNow that we have our scoreboard, we need 
to find the highest score.We set a tracker called highest_count 
to 0.We use .items() to let us look at both the letter and its 
count at the same time.As we loop through, Python asks: 
"Is this letter's count higher than the highest count 
I've seen so far?"If it is, we update highest_count to 
this new bigger number, and remember this letter as our current winner.
Once the loop finishes checking every letter, whatever letter is 
left in most_repeated_letter is the official champion, and the 
function returns it!
"""
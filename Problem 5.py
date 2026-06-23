def getsentence():
    """Prompt the user for a sentence and return it."""
    return input("Enter a sentence: ")


if __name__ == "__main__":
    sentence = getsentence()
    print(f"You entered: {sentence}")


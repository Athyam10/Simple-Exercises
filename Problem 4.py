def main():
    statement = input("Enter any statement: ")

    counts = {str(digit): 0 for digit in range(1, 9)}
    for num in statement:
        if num in counts:
            counts[num] += 1

    for digit in range(1, 9):
        crosses = "x" * counts[str(digit)]
        print(f"{digit} = {crosses}")


if __name__ == "__main__":
    main()

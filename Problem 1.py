def main():
    try:
        value = int(input("Enter a number: ").strip())
    except ValueError:
        print("Please enter a valid integer.")
        return

    if value >= 0:
        sign = "positive"
    else:
        sign = "negative"

    if value % 2 == 0:
        parity = "even"
    else:
        parity = "odd"

    print(f"The number is {sign} and {parity}.")


if __name__ == "__main__":
    main()

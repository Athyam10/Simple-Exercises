import sys


if len(sys.argv) < 1:
    print("No number provided. Please provide at least one number as a command-line argument.")
    sys.exit(1)

else:
    total = 0.0
    count = 0
    for i in range(1, len(sys.argv)):
        try:
            number = float(sys.argv[i])
            total += number
            count += 1
        except ValueError:
            print(f"Invalid input: {sys.argv[i]} is not a number.")
            sys.exit(1)
    if count == 0:
        print("No valid numbers provided.")
        sys.exit(1)
    average = total / count
    print(f"The average of the provided numbers is: {average}")



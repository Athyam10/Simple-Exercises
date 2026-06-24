def fibonacci(n):
    """Return the nth Fibonacci number."""
    if n <= 0:
        raise ValueError("Input should be a positive integer.")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b
    
# Example usage:
if __name__ == "__main__":
    n = 5
    print(f"The {n}th Fibonacci number is: {fibonacci(n)}")

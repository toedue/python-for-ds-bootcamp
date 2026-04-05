def fibonacci(n):
    a = 0
    b = 1
    sequence = []

    for i in range(n):
        sequence.append(a)

        # update values
        a, b = b, a + b

    return sequence


print("Fibonacci sequence:", fibonacci(10))

# Output:
# Fibonacci sequence: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
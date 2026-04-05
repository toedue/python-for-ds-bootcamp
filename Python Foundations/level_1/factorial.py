def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result = result * i

    return result


number = 4
print("Factorial of", number, "is", factorial(number))

# Output:
# Factorial of 4 is 24

# Example:
#     4! = 4 × 3 × 2 × 1 = 24


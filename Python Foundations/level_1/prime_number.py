def is_prime(num):
    # numbers that are less than or equal to 1 are not prime
    if num <= 1:
        return False
    
    # check the divisibility from 2 up to the number -1
    for i in range(2, num):
        # if number divides evenly, it is not prime
        if num % i == 0:
            return False
        
    # if no divisors found, it is prime
    return True

# Example 
num = 7

if is_prime(num):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")

# Output:
# 7 is a prime number

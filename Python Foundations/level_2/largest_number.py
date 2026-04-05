def largest_number(nums):
    # assume the first number is the largest
    largest = nums[0]

    for num in nums:

        # if current number is bigger than stored largest
        if num > largest:
            largest = num

    return largest


nums = [11, 26, 3, 89, 44]

print("Largest number:", largest_number(nums))

# Output:
# Largest number: 89
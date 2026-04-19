def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0

    for char in text:

        # check if the character is a vowel
        if char in vowels:
            count += 1

    return count


text = "Abdulkadir"
print("Number of vowels:", count_vowels(text))

# Output:
# Number of vowels: 4
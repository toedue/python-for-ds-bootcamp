
# Python Foundations – Daily Assignment

This repository contains solutions for the **Python Foundations Daily Assignment**.  

---

# Level 1 – Basic Python Tasks
### 1. Factorial of a Number


Calculates the factorial of a number `n`.

- Factorial means multiplying a number by all numbers below it.
- Example: `4! = 4 × 3 × 2 × 1 = 24`

```python
number = 4
print("Factorial of", number, "is", factorial(number))
# Output: Factorial of 4 is 24
````

---

### 2. Prime Number Checker

Checks whether a number is a **prime number**.

* A prime number is greater than 1 and divisible only by 1 and itself.

```python
num = 7
if is_prime(num):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")
# Output: 7 is a prime number
```

---

### 3. Reverse a String

Reverses a given string.

```python
word = "abdulkadir"
print("Original:", word)
print("Reversed:", reverse(word))
# Output:
# Original: abdulkadir
# Reversed: ridakludba
```

---

# Level 2 – Working with Strings, Lists, and Sequences

### 1. Count Vowels in a String

Counts the number of vowels (a, e, i, o, u) in a text.

```python
text = "Abdulkadir"
print("Number of vowels:", count_vowels(text))
# Output: Number of vowels: 4
```

---

### 2. Fibonacci Sequence

Generates the Fibonacci sequence up to `n` numbers.

```python
print("Fibonacci sequence:", fibonacci(10))
# Output: Fibonacci sequence: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

---

### 3. Largest Number in a List

Finds the largest number in a list of numbers.

```python
nums = [11, 26, 3, 89, 44]
print("Largest number:", largest_number(nums))
# Output: Largest number: 89
```

---

# Level 3 – CLI Applications

### 1. Simple Calculator

A command-line calculator that supports addition, subtraction, multiplication, and division.

```python
calculator()
```

* Users select an operation (1-4) and input two numbers.
* The program prints the result.
* Division by zero is handled with a message: “Cannot divide by zero”.

---

### 2. Tic Tac Toe Game

A command-line Tic Tac Toe game for two players (X and O).

* Shows the board with **positions (0–8)**.
* Players take turns choosing positions.
* Checks for a winner after every move.
* Declares a draw if all positions are filled without a winner.

```python
tic_tac_toe()
```

* Example board display:

```
Current Board:
X |   | O
--+---+--
  | O |  
--+---+--
X |   |  
```

* Messages guide the players:

  * Whose turn it is
  * Invalid input
  * Position already taken
  * Winner or draw

---


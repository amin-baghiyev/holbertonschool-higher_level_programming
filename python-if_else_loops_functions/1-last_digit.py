#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print(f"Last digit of {number} is ", end="")
last_digit = number % -10 if number < 0 else number % 10
if (number % 10 > 5):
    print(f"{last_digit} and is greater than 5")
elif (number % 10 == 0):
    print("0 and is 0")
elif (number % 10 < 6 and number % 10 != 0):
    print(f"{last_digit} and is less than 6 and not 0")

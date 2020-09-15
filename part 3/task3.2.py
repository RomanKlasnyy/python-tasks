"""Implement 2 functions for calculation Factorial number (Method retrieves number, returns it Factorial).
  First function uses while loop for calculation
  Second function uses for loop for calculation
  For avoid stack overflow do not calculate Factorial number
  more than 100500. Use default function argument for limit.
  Negative, fractional, not a number argument forbidden."""


def while_factorial(num):
    if type(num) != int or 0 > num or num > 100500:
        print('num should not be negative, not an integer or bigger than 100500')
        return False
    factorial = 1
    step = 0
    while step != num:
        step += 1
        factorial *= step
    print(factorial)


def for_factorial(num):
    if type(num) != int or 0 > num or num > 100500:
        print('num should not be negative, not an integer or bigger than 100500')
        return False
    factorial = 1
    for i in range(num):
        factorial *= i+1
    print(factorial)


while_factorial(5)
for_factorial(6)
while_factorial(123456789)
for_factorial('five')
while_factorial(-3)

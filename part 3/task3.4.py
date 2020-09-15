"""Implement printDiagonal function which wrap convertCmToInches function and print result.
  (call convertCmToInches and print result of evaluation)."""


def cm_to_inches(num):
    return num * 0.3937007874


def print_diagonal(x):
    print(cm_to_inches(x))


print_diagonal(4)

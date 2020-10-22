class FibonacciSave:
    saved_fib = 0
    exit_fib = False


def fibonacci():
    fib_input_check()
    if not FibonacciSave.exit_fib:
        fib_continue()


def fib_continue():
    while True:
        if FibonacciSave.exit_fib:
            break
        print("Do you want to continue? (Y/N)")
        cont = input()
        if cont == 'n' or cont == 'N':
            break
        elif cont == 'y' or cont == 'Y':
            fib_input_check()
        else:
            print("Error. Please, enter Y or N.")


def fib_input_check():
    while True:
        if FibonacciSave.saved_fib == 0:
            print("Type fibonacci number or 'exit'.")
        else:
            print("How much do you want to add?")
        num = input()
        if num == 'exit':
            FibonacciSave.exit_fib = True
            break
        elif num.isdigit() and int(num) > 0:
            print(fibonacci_check(int(num) + FibonacciSave.saved_fib))
            FibonacciSave.saved_fib += int(num)
            break
        else:
            print("Error. Please, input a positive number or 'exit'.")
            continue


def fibonacci_check(x):
    x = int(x)
    if x == 1:
        return 0
    elif x == 2:
        return 1
    else:
        return fibonacci_check(x-1)+fibonacci_check(x-2)


if __name__ == '__main__':
    fibonacci()

def fibonacci(x):
    if x <= 0:
        print("Incorrect input.")
    elif x == 1:
        return 0
    elif x == 2:
        return 1
    else:
        return fibonacci(x-1)+fibonacci(x-2)


saved_fib = 0
start = True
cont_error = False

while True:
    if start:
        print("Type Fibonacci number or 'exit'.")
        n = input()
        if n == 'exit':
            break
        elif n.isdigit():
            print(fibonacci(int(n)))
            saved_fib = int(n)
            start = False
        else:
            print("Error. Please, input a positive number or 'exit'.")
            continue
    elif not cont_error:
        print("How much do you want to add?")
        n = input()
        if n == 'exit':
            break
        elif n.isdigit():
            saved_fib += int(n)
            print(fibonacci(saved_fib))
        else:
            print("Error. Please, input a positive number or 'exit'.")
            continue
    cont_error = False
    print("Do you want to continue? (Y/N)")
    cont = input()
    if cont == 'n' or cont == 'N':
        break
    elif cont == 'y' or cont == 'Y':
        continue
    else:
        cont_error = True
        print("Error. Please, enter Y or N.")

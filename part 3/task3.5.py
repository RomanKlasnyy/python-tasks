"""Implement processArgs function which retrieves callback as a first argument,
remaining args has various length. Default value for callback is a standard print function.
Call this function with printDiagonal function and remaining args as cm or inches.
  processArgs(printDiagonal, 50, True)
  processArgs(print, 'test')
  processArgs(len, [])"""


def cm_to_inches(num):
    return num * 0.3937007874


def print_diagonal(x):
    print(cm_to_inches(x))


def process_args(arg=print, val=None, debug=False):
    if debug:
        print(arg)
    if arg == len:
        print(len(val))
    return arg(val)


process_args(print_diagonal, 50, True)
process_args(print, 'test')
process_args(len, [])

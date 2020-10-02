"""Create iterator from tuple which created using comprehension
  print values using: next, loop"""

from itertools import cycle


def double_chars(phrase):
    chars = cycle((x for x in phrase))
    for i in chars:
        yield i*2


y = double_chars('Python')
for k in range(12):
    print(next(y))

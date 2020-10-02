"""Implement your own _unique function using:
1)  dictionary comprehension.
2)  set comprehension
first arg is collection.
"""


def _unique(collection):
    if type(collection) == list:
        return [x for x in collection if x % 3 == 0]
    elif type(collection) == set:
        return {x for x in collection if type(x) == str}


lst = [1, 2, 3, 9, 8, 6, 9]
st = {9, 5, 7, 'foo', 'bar'}
print(_unique(lst))
print(_unique(st))

"""Implement your own _unique function using:
1)  dictionary comprehension.
2)  set comprehension
first arg is collection.
"""


def _unique(collection):
    if type(collection) == list:
        return [x for x in collection]
    elif type(collection) == set:
        return {x for x in collection}


lst = [1, 2, 3, 9, 8, 7, 9]
st = {9, 5, 7, 'foo', 'bar'}
print(_unique(lst))
print(_unique(st))

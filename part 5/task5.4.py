"""Implement _print decorator. Decorator should print result
  of the decorated function evaluation
  Decorate _unique fn with this decorator.
  unique items should be print automatically"""


def _print(func):
    """Decorate function with logs before and after call"""
    def wrapper(*args, **kwargs):
        print("Before call:", *args, **kwargs)
        result = func(*args, **kwargs)
        print("After call:", *args, **kwargs)
        return result

    return wrapper


@_print
def _unique(collection):
    if type(collection) == list:
        return list(set(collection))
    elif type(collection) == set:
        return collection


_unique({1, 1, 2, 2, 'foo', 'bar', 'foo'})

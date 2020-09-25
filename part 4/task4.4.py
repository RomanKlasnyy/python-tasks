"""Implement your own _find function.
  first arg is callback, second arg - collection.
  function returns first item from collection for which callback function call return true
  Usage of standard filter function or yor own _filter is forbidden.

  _find([1,2,3], lambda x: x == 2) -> None
  _find([{'a': 0, 'b': 1}, {'a': 1, 'b': 2}], lambda item: item.get('a', 0) > 0) -> {'a': 1, 'b': 2}
"""


def _find(collection, callback):
    first_item = None
    for i in collection:
        if callback(i) and not first_item:
            first_item = i
    print(first_item)


_find([1, 2, 3], lambda x: x == 2)  # 2
_find([1, 2, 3, 4, 5], lambda x: x % 2 == 0)  # 2
_find([1, 2, 3], lambda x: x == 5)  # None
_find([{'a': 0, 'b': 1}, {'a': 1, 'b': 2}], lambda item: item.get('a', 0) > 0)

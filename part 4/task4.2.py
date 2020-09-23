"""Implement your own _filter function.
  first arg is callback, second arg - collection.
  function returns new collection of items for which callback function call return true
  Usage of standard filter function is forbidden.

  list(filter(lambda x: x, [0,1,2,3])) -> [1,2,3]
  _filter(lambda x: x, [0,1,2,3]) -> [1,2,3]
"""


def _filter(callback, lst):
    processed_list = []
    for i in lst:
        if callback(i):
            processed_list.append(i)
    print(processed_list)


_filter(lambda x: x, [0, 1, 2, 3])

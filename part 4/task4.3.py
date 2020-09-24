"""Implement your own _map function.
  first arg is collection, second arg - callback (mapper)
  function returns new collection of mapped items.
  Usage of standard map functionality is forbidden.

  list(map(lambda x: x, [1,2,3])) -> [1,2,3]
  _map([1,2,3], lambda x: x) -> [1,2,3]
"""


def _map(collection, callback):
    mapped_collection = []
    for i in collection:
        if callback(i):
            mapped_collection.append(i)
    print(mapped_collection)


_map([1, 2, 3], lambda x: x)

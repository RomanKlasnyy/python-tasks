""" Implement your own _map as a generator function
  first arg is collection, second arg - callback (mapper)
  function returns new collection of mapped items (lazy, by request).
  Usage of standard map functionality is forbidden.
  print values using: next, loop"""


def _map(collection, callback):
    mapped_collection = []
    for i in collection:
        if callback(i):
            mapped_collection.append(i)
            # print(mapped_collection)
            yield i


even_check = _map([1, 2, 4, 8, 16, 17, 23, 34], lambda x: x % 2 == 0)

print(next(even_check))  # 2
print(next(even_check))  # 4
print(next(even_check))  # 8
print(next(even_check))  # 16
print(next(even_check))  # 34

"""Implement your own _unique function.
  first arg is collection.
  function returns new collection of unique items
  Usage of Set, Counter data structures is forbidden.
"""

example_list = ['foo', 'bar', 14, 79, 'foo', 14, 123]
processed_list = []


def _unique(lst):
    for i in lst:
        if i not in processed_list:
            processed_list.append(i)


_unique(example_list)
print(processed_list)

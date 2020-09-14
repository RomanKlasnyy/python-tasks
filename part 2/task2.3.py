"""Create set with any elements. Create dictionary from this enumerated set."""

set_example = {'foo', 'bar', 'lol', 'kek', 'cheburek'}
dict_example = dict((enumerate(set_example)))
print(dict_example)

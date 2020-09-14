"""Create tuple with chars from a long string (1). Slice last 20 chars
in reversed order beginning from 5th (5th from end) (2). Create dictionary
from sliced chars. Print sorted keys of this dictionary (3)."""

long_string = '1234567890qwertyuiopasdfghjkl;'
char_tuple = tuple(long_string)
print(char_tuple)  # (1)
sliced_chars = long_string[-5:-25:-1]
print(sliced_chars)  # (2)
sliced_chars_dict = dict(enumerate(sliced_chars))
print(sliced_chars_dict.keys())  # (3)

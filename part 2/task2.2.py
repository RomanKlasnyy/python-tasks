"""Create list of chars from a long string. Extend list by chars from
another string (1). Remove duplicated items form list (2).
Delete middle element using slice functionality (important) (3)."""

long_string = '1234567890qwertyuiopasdfghjkl;'
another_string = 'foobar'
chars_list = list(long_string)
chars_list.extend(another_string)
print(chars_list)  # (1)

unique_char_list = []
for i in range(len(chars_list)):
    if chars_list[i] not in unique_char_list:
        unique_char_list.append(chars_list[i])
    else:
        continue

print(unique_char_list)  # (2)

half_str_length = len(unique_char_list) // 2
print(unique_char_list[:half_str_length]
      + unique_char_list[half_str_length+1:])  # (3)



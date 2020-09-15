"""Create two Sets with numbers and chars. Find intersection, union,
difference between them. Use difference_update to update one set by other."""

set_x = {1, 2, 3, 'f', 'o'}
set_y = {'f', 'o', 'b', 'a', 'r'}

print(set_x & set_y, '- intersection')
print(set_x | set_y, '- union')
print(set_x - set_y, set_y - set_x, '- separated difference')
print(set_x ^ set_y, '- symmetric difference')


def difference_update(a, b):
    a.update(b)
    print(a)


difference_update(set_x, set_y)

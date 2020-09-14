"""Create 'AddressBook' dictionary {}. Key should be a tuple
(<street_name>, <building_number>)- building address, where the people leave
value should be a dictionary {}. (key - (<floor_number>, <flat_number>),
value - list ['citizen 1', 'citizen 2'])"""

data_example_1 = 'Makarenka Str., 32, floor 4, flat 51'
data_list_1 = data_example_1.split(', ')
AddressBook_1 = {(data_list_1[0], data_list_1[1]): [data_list_1[2], data_list_1[3]]}

data_example_2 = 'Walter Str., 14, 3, 49'
data_list_2 = data_example_2.split(', ')
AddressBook_2 = {(data_list_2[0], int(data_list_2[1])): [int(data_list_2[2]), int(data_list_2[3])]}

AddressBook_1.update(AddressBook_2)
print(AddressBook_1)

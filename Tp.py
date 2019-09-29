my_list = [1, -2, 16, -13, 20, 0, 3, 77]
pozitive_list = list()
negative_list = list()
for item in my_list:
	if item < 0:
		negative_list.append(item)
	elif item > 0:
		pozitive_list.append(item)
	else:
		pozitive_list.append(item)
print(my_list)
print(pozitive_list)
print(negative_list)
print(max(pozitive_list))
print(min(pozitive_list))
print(max(negative_list))
print(min(negative_list))

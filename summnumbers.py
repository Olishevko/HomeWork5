number = list(map(int, input('enter number 12345: ')))
print(type(number))
some_numbers = 0
for i in number:
	some_numbers += i
print(some_numbers, type(some_numbers))
result = list(map(int,str(some_numbers)))
print(result, type(result))
result1 = 0
for i in result:
	result1 += i
print(result1, type(result1))
# во время решения этой задачи затупил с условием. переделать нужно.

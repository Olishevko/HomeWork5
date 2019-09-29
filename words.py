print('Введите слова через пробел: ')
words_list = [e for e in input().split()] # преобразованая строка в список 
print(words_list)
l = max(words_list, key=len) #print(max(words_list, key=len))
s = min(words_list, key=len)
print(l, s)
l, s = s, l
print(l,s)

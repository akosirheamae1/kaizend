def func(word = 'hello'):
    return word
temp = ''
for i in range(3):
    temp += func()
print(temp)

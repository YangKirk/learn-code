name = ['Kirk', '23', 'love']
print(name)
name[1] = '22'
print(name)
name.append('VV')
print(name)
del name[1]
print(name)
if 'love' in name:
    print("Yes,love在列表里!")
print([1, 2, 3] + [2, 3, 4])
print(['H!!'] * 4)
for x in name:
    print(x, end='')
print()
print(len(name))
print(max(name))
print(min(name))
print(tuple(name))
print(name.count('VV'))
list(name)
name.extend(['1', '2', '3'])
print(name)
print(len(name))
name.insert(1, '23')
print(name)
name.pop(6)
print(name)
new_name = [name, 1111, 2222, 3333, 88.88]
print(new_name)

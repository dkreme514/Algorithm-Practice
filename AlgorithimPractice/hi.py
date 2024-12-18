def f(x, items=None):
    if items is None:
        items = []
    items.append(x)
    return items
'''
for i in range(10):
    if i % 2 == 0:
        continue;
    print(i)
    if i > 7:
        break
        '''
r = f(7)
print(r)
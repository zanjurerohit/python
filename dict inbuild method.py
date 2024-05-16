a={'name':'rohit','age':23,'city':'kalyan'}
print(a.keys())
print(a.values())
print(a.items())

a.pop('city')
print(a)
del a['age']
print(a)

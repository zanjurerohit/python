#tuple with constructor:

a=tuple((1,2,3,4,5))
print(type(a))

# tuple without constructor:

b=(1,2,3,4,5,6)
print(type(b))
c=(1)
print(type(c))

#a[0] ="rohit"
print(a[-1])
print(b[0])
print(a)

#can not add and remove values from tuple:
#but you can add two tuples together:
d=(11,22)
print(a+b+d)

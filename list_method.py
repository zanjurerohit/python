#append
a =[1,4,8,87,5,65,5,45]
a.append(12)
print(a)

#insert:

b=[12,45,78,96,36,14]
b.insert(5,"rohit")
print(b)

#extend:

c=[1,5,8,9,3,7,5]
c.extend(b)
print(c)

#remove:

d=[4,3,4,2,22,55,98,89]
d.remove(89)
print(d)

#pop:
d.pop()
d.pop(5)
print(d)

#del:
del a
del b[5]
print(b)

#clear:
c.clear()
print(c)


'''a=['rahul','rohit','sai killa','omker','prabudha','kajol']
b=[]
for i in a:
    if 'k' in i:
        b.append(i)
    print(b)'''


a=['rahul','rohit','sai killa','omker','prabudha','kajol']
b=[]
for i in a:
    if 'a' in i[1]:
        b.append(i)
    print(b)

a=[153,11,22,24,140,556]
b=[]
for i in i<len(a):
    if a%2==0:
        print(a)




















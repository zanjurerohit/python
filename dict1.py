data=['name','age','city']
data1=['rohit',30,'thane']
c={}
'''for i in range(len(data)):
    c[data[i]]=data1[i]
print(c)'''

'''for i in range (len(data)):
    for j in range(len(data1)):
        if i==j:
            c[data[i]] = data1[i]
        elif i>j:
            c[data[i]]="default"
        elif j>i:
            c["defaultkey"]= data1[i]
print(c)'''

if len(data)==len(data1):
    for i in range(len(data)):
        c[data[i]]=data1[i]
    print(c)
else:
    print("key list and value list length should be same")


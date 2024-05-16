'''a=[1,'fjfi',54,855,55]
print(type(a))
print(a)
print(len(a))
print(id(a))


#accessing list element:

print(a[2])
print(a[-5])

a[4]="rahul"
print(a)


a=[1,'fjfi',54,855,55]
i=0
while i<len(a):
    print(a[i])
    i+=1

for i in range(len(a)):
    print(a[i])'''

'''a=[11,22,101,2,5,8,542,442,441]
i=0
while i<len(a):
    if a[i]%2==0:
        print(a[i])
    i=i+1'''


'''a=[11,22,101,2,5,8,542,442,441]
for i in range(len(a)):
    if a[i]%2==0:
        print(a[i])
        i=i+1'''


a=[1,2,1,2,33,44,55,3]
i=0
while i<len(a):
    if a[i]==a[i]:
        print(a[i])
    i=i+1

a=[1,2,1,2,33,44,55,3]
for i in range(len(a)):
    for j in range(i+1,len(a),1):
        if a[i]==a[j]:
            print(a[i])
    i=i+1
    
#home work:    
#maximum number find in list:

#find minimun number:
#find second maximum number in list:
#* * * * *
#  *
#    *
#      *
#        *


#  b
#a   a
#a b a
#a   a








       






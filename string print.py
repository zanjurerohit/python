'''stdata='ABCDEF'
cols=1
for row in range(0,len(stdata),1):
    for col in range(0,len(stdata),1):
        if col< len(stdata)-cols:
            print(" ",end=" ")
        else:
            print(stdata[row],end=" ")
    cols+=1
    print()'''


for row in range(1,6,1):
    for col in range(1,6,1):
        if row==1 and col==1:
            print("c",end=" ")
        if row==1:
            print("a",end=" ")
        elif col==1:
            print("b",end=" ")
    print()

#for loop:
'''for row in range(1,6,1):
    for col in range(1,6,1):
        if row==1:
            print("a",end=" ")
        elif col==1:
            print("b",end=" ")
    print()'''

#while loop:
'''row=1
while row<=5:
    col=1
    while col<=5:
        if row==1:
            print("a",end=" ")
        elif col==1:
            print("b",end=" ")
        col+=1
    row+=1
    print()'''




a="my name is rohit"

i=-1
s=" "
l=-(len(a))
while i>=l:
    s=s+a[i]
    i=i-1
print(s)

#slice of print:
#default string is 0 and default step is 1:
a="welcome to india"
b=a[0:7:1]
print(b)

#default end is last index value:

f="welcome to india"
e=f[11::1]
print(e)

#printing reverse welcome using negative index value:

c="welcome to india"
d=c[-9::-1]
print(d)

#printing reverse welcome using positive index value:

m="welcome to india"
n=m[6::-1]
print(n)

#without using start and end print positive or negative index value string:

p="welcome to india"
s=p[::-1]
r=p[::1]
print(s)
print(r)


    


    

                


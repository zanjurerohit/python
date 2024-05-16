row=1
while row<=5:
    col=1
    while col<=5:
        if row==1 or col==row==2 or col==row==3 or col==row==4 or col==row==5:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col+=1
    print()
    row+=1


row=1
while row<=4:
    col=1
    while col<=3:
        if col==1 or col==3:
            print("a",end=" ")
        elif row==1 or row==3:
            print("b",end=" ")
        else:
            print(" ",end=" ")
        col+=1
    print()
    row+=1
    

a=[1,2,1,2,33,44,55,3]
mx=[0]
for i in range(1,len(a),1):
    if mx<a[i]:
        mx=a[i]
        print(mx)


for i in range(len(a)):
    print(max(a))
    break

for i in range(len(a)):
    print(min(a))
    break













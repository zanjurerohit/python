"""a=0
b=10
c=20
if (a>b and a>c):
    print("a is greter")
elif(b>c and b>a):
    print("b is greter")
else:
    print("c is greter")"""
    
"""i=int(input("enter number:"))
if(40>=60):
      print ("c")
elif(61>=80):
    print("b")
elif(81>=100):
    print("a")
else:
    print("fail")"""


amount=float(input("enter amount:"))
if amount%10==0:
    if amount>=500:
        notes=amount//500
        print("500 notes",notes)
        amount=amount%500
    if amount>=200:
        notes=amount//200
        print("200 notes",notes)
        amount=amount%200
    if amount>=100:
        notes=amount//100
        print("100 notes",notes)
        amount=amount%100
    if amount>=50:
        notes=amount//50
        print("50 notes",notes)
        amount=amount%50
    if amount>=20:
        notes=amount//20
        print("20 notes",notes)
        amount=amount%20
    if amount>=10:
        notes=amount//10
        print("10 notes",notes)
        amount=amount%10    
else:
    print("amount should be multiple of 10")


    
    





















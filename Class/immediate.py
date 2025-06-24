'''x=int(input("Enter a Number:- "))
a=1
for i in range(2,x):
    if x%i==0:
        a+=i
if a==x:
    print("Perfect Number")
else:
    print("Not Perfect")'''

'''for i in range(5,0,-1):
    print("*"*i)'''
'''x=eval(input("Enter a List:- "))
i,t=0,0
while t<len(x):
    if x[i]%2==0:
        x.append(x.pop(i))
        i-=1
    i+=1
    t+=1
print(x)'''

'''x=int(input("Enter Number:- "))
t,h=x,x
a,b=0,0
while x>0:
    a+=1
    x//=10
while t>0:
    b+=(t%10)**a
    t//=10
if h==b:
    print("Armstrong")
else:
    print("Not Armstrong")'''

'''def title_without_title(x):
    a=x.split()
    t=""
    for i in a:
        t+=i[0].upper()+i[1:].lower()+" "
    return t'''

'''x=eval(input("Enter a List:- "))
m1=0
for i in x:
    if i>m1:
        m1=i
m2=m1
for i in x:
    if i<m2:
        m2=i
print("max number=",m1)
print("min number=",m2)'''

'''x=input("Enter a String:- ")
a=""
for i in x:
    if i.lower() not in ["a","e","i","o","u"]:
        a+=i
print(a)'''

def x(a):
    a[0]=20
    a.append(6)
    print(a)
l=[1,2,3,4,5]
print(l)
x(l)
print(l)
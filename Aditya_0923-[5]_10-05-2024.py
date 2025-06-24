x=int(input("enter a number:- "))
v=0
while x!=0:
    v+=x%10
    x=x//10
print(v)

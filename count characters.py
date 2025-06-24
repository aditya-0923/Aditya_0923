x=input()
l,u,d,s=0
for i in x:
    if i.islower():
        l+=1
    elif i.isupper():
        u+=1
    elif i.isdigit():
        d+=1
    else:
        s+=1
print("lowercase = ",l)
print("upper = ",u)
print("digit = ",d)
print("special =",s)

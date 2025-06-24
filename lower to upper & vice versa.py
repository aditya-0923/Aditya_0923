x=input()
a=""
for  i in x:
    if i.islower():
        a+=i.upper()
    elif i.isupper():
        a+=i.lower()
    else:
        a+=i
print(a)

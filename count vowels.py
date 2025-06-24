'''a=input("Enter a String:- ")
v=0
for i in a:
    if i.lower() in ["a","e","i","o","u"]:
        v=v+1
print(v)'''

a=input("Enter a String:- ")
x=a.split()
v=0
t=""
for i in x:
    t=i
    for j in i:
        if j.lower() in ["a","e","i","o","u"]:
            v=v+1
    print(t,v)
    v=0
    t=""
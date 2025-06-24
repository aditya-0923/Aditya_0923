#move positive to right in list
'''a=eval(input("Enter a list:- "))
s=[]
for i in a:
    if i<0:
        s.append(i)
for i in a:
    if i==0:
        s.append(i)
for i in a:
    if i>0:
        s.append(i)
print(s)'''

a=eval(input("Enter a list: "))
i=0
k=0
while i<len(a)-k:
    if a[i]>0:
        a.append(a.pop(i))
        k+=1
    else:
        i+=1
print(a)

'''a = eval(input("Enter a list: "))
for num in a[:]:
    if num > 0:
        a.remove(num)
        a.append(num)
print(a)'''

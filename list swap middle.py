l=[]
s=0
while s==0:
  z=input("Enter list elements(enter any alphabet to end):- ")
  if z.isnumeric():
    l.append(z)
  else:
    break
print("Your entered list:- ",l)
x=0
a=len(l)
b=a//2
for i in range(b,a):
  c=l[i]
  l[i]=l[x]
  l[x]=c
  x+=1
if a%2!=0:
  c=l.pop(b)
  l.append(c)
  l.insert(b,l.pop())
  l.insert(b+1,l.pop())
print("Swapped List:- ",l)

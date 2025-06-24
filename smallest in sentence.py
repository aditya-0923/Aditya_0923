#smallest word in a sentence
x=input()
a=""
b=x.split()
c=len(b[0])
for i in b:
  if len(i)<c:
    c=len(i)
    a=i
print(a)
print(c)

x=input()
a=""
b=x.split()
for i in b:
  a+=i[0].upper()+i[1:].lower()+" "
print(a)    

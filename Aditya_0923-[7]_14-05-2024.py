x=int(input("enter the number:- "))
z=0
for i in range(2, x+1):
  w=True
  for a in range(2, i+1):
    if i%a==0:
      w=False
      break
    if w:
      z+=i
print(z)

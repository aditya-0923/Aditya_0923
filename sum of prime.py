x=int(input())
a=0
for i in range(2,x):
  for m in range(2,i):
    if i%m==0:
       break
    else:
        a+=i
    print(a)
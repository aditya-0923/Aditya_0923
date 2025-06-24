''' Write a program to print of fibonnaci series 
upto n. for example if n is 50 then output 
will be : 
0 
1 
1 
2 
3 
5 
8 
13 
21 
34'''

n=int(input("Value for n:- "))
f=[0,1]
for i in range(n):
  if i==0 or i==1:
    print(f[i])
  else:
    f.append(f[i-1]+f[i-2])
    print(f[i])
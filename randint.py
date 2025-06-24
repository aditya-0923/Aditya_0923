import random as r
while True:
  x=int(input("enter 0 to continue or any digit to exit:- "))
  if x==0:
    print(r.randint(0,100))
  else:
    break

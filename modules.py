import random as r
p=r.randint(0,3)
c=['Delhi','Mumbai','Chennai','Kolkata']
for i in c:
    for j in range(1,p):
        print(i,end='')
    print()
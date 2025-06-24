while True:
    try:
        n=int(input("Number of Teams:- "))
        if n<3:
            print("Value less than 3 is not acceptable".center(80,"-"))
            continue
        break
    except:
        print("Enter a valid integer value".center(80,"-"))
        continue
d1,d2={},{}
l1,l2=[],[]
if n%2!=0:
    for i in range(1,((n-1)//2)+1):
        d1[i]="-"
        l1.append(i)
    for i in range(((n+1)//2),n+1):
        d2[i]="-"
        l2.append(i)
else:
    for i in range(1,n//2):
        d1[i]="-"
        l1.append(i)
    for i in range(n//2+1,n+1):
        d2[i]="-"
        l2.append(i)
p=0
while 2**p<n:
    p+=1
b=2**p-n
i1,i2=[0],[1]
for i in range(b):
    if i%2==0:
        i1.append(i)
        if i-i1[-2]==2:
            d2[l2[0]]="bye"
            l2.remove(l2[0])
            i1=[0]
        else:
            d2[l2[-1]]="bye"
            l2.remove(l2[-1])
    elif i%2!=0:
        i2.append(i)
        if i-i2[-2]==2:
            d1[l1[-1]]="bye"
            l1.remove(l1[-1])
            i2=[1]
        else:
            d1[l1[0]]="bye"
            l1.remove(l1[0])
print("Upper half: ",d1,"\nLower half: ",d2,sep='')
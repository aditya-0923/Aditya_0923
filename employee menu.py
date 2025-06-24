d={}
n=int(input("Numbers of entries:- "))
for i in range(n):
    j=(input("Name:- "))
    k=int(input("Basic Salary:- "))
    l=int(input("House Rent Allowance:- "))
    m=int(input("Convence Allowance:- "))
    d[j.lower()]=[k,l,m]
while True:
    print("1: Total Salary")
    print("2: Total Allowance")
    print("3: Search")
    print("4: Exit")
    ch=int(input("Your Choice:- "))
    if ch==1:
        x=input("Name:- ")
        s=0
        for a,b in d.items():
            if a==x.lower():
                s+=b[0]
                print(s)
            else:
                break
        else:
            print("Not Found")
    elif ch==2:
        x=input("Name:- ")
        s=0
        for a,b in d.items():
            if a==x.lower():
                s+=b[1]+b[2]
                print(s)
            else:
                break
        else:
            print("Not Found")
    elif ch==3:
        s=(input("Name:- "))
        for i in d.keys():
            if i==s.lower():
                print(d[i])
        else:
          print("Not Found")
        elif ch==4:
          break
        else:
          5print("Wrong Choice")

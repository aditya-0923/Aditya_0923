'''l = eval(input("Enter list: "))
p_n = 0
for num in l:
    d = []  
    for i in range(1, num + 1):
        if num % i == 0:
            d.append(i)
    if len(d) == 2:
        p_n += 1
print("Frequency of prime no.",p_n)'''

'''x=[1,2,3,7,13,17,0,19,29,30]
def count_prime(l):
    xd=0
    for i in l:
        if i==0 or i==1:
            continue
        for j in range(2,i):
            if i%j==0:
                break
        else:
            xd+=1
    return xd
print("Prime Count=",count_prime(x))'''

'''def is_as(x):
    a=x.split()
    j,k=0,0
    for i in a:
        if i.lower()=="is":
            j+=1
        elif i.lower()=="as":
            k+=1
    return j,k
s=input("Input:-")
print("is_count=",is_as(s)[0],"\nas_count=",is_as(s)[1])'''

a=eval(input("Enter a list:- "))
s=[]
for i in a:
    if i<0:
        s.append(i)
for i in a:
    if i==0:
        s.append(i)
for i in a:
    if i>0:
        s.append(i)
print(s)

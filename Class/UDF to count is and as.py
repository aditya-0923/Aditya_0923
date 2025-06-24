#UDF to count is and as
def is_as(x):
    a=x.split()
    j,k=0,0
    for i in a:
        if i.lower()=="is":
            j+=1
        elif i.lower()=="as":
            k+=1
    return j,k
s=input("Input:-")
print("is_count=",is_as(s)[0],"\nas_count=",is_as(s)[1])
''' Write a function in Python, which accepts a list Lst of numbers and n is a numeric 
value by which all elements of the list are shifted to left.Sample Input Data of the 
list : 
Lst= [ 10,20,30,40,12,11], n=2 Output Lst = 30,40,12,11,10,20] '''

def LShift(Lst,n):
  for i in range(n):
    Lst.append(Lst.pop(0))
  return Lst
print(LShift([10,20,30,40,12,11],2))
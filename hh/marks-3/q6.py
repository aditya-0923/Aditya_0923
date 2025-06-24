'''Write a Python program to find the maximum and minimum elements in the list 
entered by the user'''

l=eval(input("Enter List:- "))
min,max=l[0],l[0]
for i in l:
  if i<=min:
    min=i
  if i>=max:
    max=i
print("Max=",max,"\nMin=",min)
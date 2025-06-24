''' Write a program to replaces elements having even values with its half and elements 
having odd values with twice its value in a list. 
eg: if the list contains 3, 4, 5, 16, 9 then rearranged list as 6, 2,10,8, 18'''

l=[3,4,5,16,9]
for i in range(len(l)):
  if l[i]%2==0:
    l[i]//=2
  else:
    l[i]*=2
print(l)
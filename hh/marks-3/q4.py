'''Write program to add those values in the list of NUMBERS, which are odd. Sample 
Input Data of the List NUMBERS=[20,40,10,5,12,11] OUTPUT is 16'''

NUMBERS=[20,40,10,5,12,11]
s=0
for i in NUMBERS:
  if i%2!=0:
    s+=i
print(s)
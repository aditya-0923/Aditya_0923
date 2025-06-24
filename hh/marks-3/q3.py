'''Write a function in Python, which accepts a list Arr of numbers as parameters , the 
function will replace the even number by value 10 and multiply odd number by 5 . 
Sample Input Data of the list is: arr=[10,20,23,45] output : [10, 10, 115, 225]'''

def function(Arr):
  for i in range(len(Arr)):
    if Arr[i]%2==0:
      Arr[i]=10
    else:
      Arr[i]=Arr[i]*5
  return Arr
print(function([10,20,23,45]))
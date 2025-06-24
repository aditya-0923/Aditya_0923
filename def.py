d={}
def add_employee():
  n=int(input("Number of employees to be added:- "))
  while n>0:
    e_id=int(input("Employee ID:- "))
    if e_id in d:
      print(f"Employee ID {e_id} already exists")
      s=input("Enter a different ID (y/n):- ").lower()
      if s=="y":
        continue
      else:
        break
    e_name=input("Employee name:- ")
    basic_salary=int(input("Basic salary:- "))
    allowance=int(input("Allowance:- "))
    d[e_id]=[e_name,basic_salary,allowance]
    n-=1
def search_employee():
  x=int(input("ID of the employee:- "))
  if x in d.keys():
    print("-ID: ",x,'\n'"-Name: ",d[x][0],'\n',"-Basic Salary: ",d[x][1],'\n',"-Allowance: ",d[x][2],sep="")
  else:
    print("--No record found--")
def total_salary():
  x=int(input("ID of the employee:- "))
  if x in d.keys():
    print("Total salry of",d[x][0],"= ",d[x][1]+d[x][2])
  else:
    print("--No record found--")
while True:
  print("1; Add Employee\n","2; Search Employee\n","3; Total Salary\n","4; Exit",sep='')
  choice=input("Your choice:- ")
  if choice.isdigit():
    if int(choice)==1:
      add_employee()
    elif int(choice)==2:
      search_employee()
    elif int(choice)==3:
      total_salary()
    elif int(choice)==4:
      print("--Program has ended--")
      break
  else:
    print("--Please enter a valid choice--")
    continue

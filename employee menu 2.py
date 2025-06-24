d = {}
def add():
    while True:
        e_id=int(input("Employee ID:"))
        if e_id not in d:
            name=input("Name: ").lower()
            basic_salary=int(input("Basic Salary: "))
            house_rent_allowance=int(input("House Rent Allowance: "))
            conveyance_allowance=int(input("Conveyance Allowance: "))
            d[e_id]=[name,basic_salary,house_rent_allowance,conveyance_allowance]
            print("Added".center(80,"-"))
            choice=input("Continue?[Y/N]:- ").lower()
            if choice=="y":
                continue
            else:
                break
        else:
            print("This Employee already exists".center(80,"-"))
            choice=input("Continue with a different Id?[Y/N]:- ").lower()
            if choice=="y":
                continue
            else:
                break
def total_salary():
    e_id=int(input("Employee ID: "))
    if e_id in d:
        total_salary=d[e_id][1]+d[e_id][2]+d[e_id][3]
        print("Total Salary=",total_salary)
    else:
        print("Not Found".center(80,"-"))
def total_allowance():
    e_id=int(input("Employee ID: "))
    if e_id in d:
        total_allowance=d[e_id][2]+d[e_id][3]
        print("Total Allowance=",total_allowance)
    else:
        print("Not Found".center(80,"-"))
def search():
    e_id=int(input("Employee ID: "))
    if e_id in d:
        print('\n',"Details for employee ID: ",e_id,":",'\n',"Name= ",d[e_id][0],'\n',"Basic Salary= ",d[e_id][1],'\n',"House Rent Allowance= ",d[e_id][2],'\n',"Conveyance Allowance= ",d[e_id][3],sep="")
    else:
        print("Not Found".center(80,"-"))
while True:
    print('\n',"Main Menu".center(80,"-"),"\n","1: Add Employee\n","2: Total Salary\n","3: Total Allowance\n","4: Search\n","5: Exit\n",sep="")
    choice=int(input("Your Choice: "))
    if choice==1:
        add()
    elif choice==2:
        total_salary()
    elif choice==3:
        total_allowance()
    elif choice==4:
        search()
    elif choice==5:
        print("Program has ended".center(80,"-"))
        break
    else:
        print("Wrong Choice".center(80,"-"))

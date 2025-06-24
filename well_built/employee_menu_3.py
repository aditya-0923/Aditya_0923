from time import sleep
d={}
def add():
    while True:
        print("-".center(120,"-"))
        e_id=input("Employee_ID: ")
        if e_id not in d:
            name=input("Name: ").lower()
            basic_salary=input("Basic_Salary: ")
            house_rent_allowance=input("House-Rent_Allowance: ")
            conveyance_allowance=input("Conveyance_Allowance: ")
            d[e_id]=[name,int(basic_salary),int(house_rent_allowance),int(conveyance_allowance)]
            print('\n',"<Added>".center(120,"-"),sep="")
            choice=input("Continue?[Y/N]:- ").lower()
            if choice=="y":
                continue
            else:
                break
        else:
            print("<This Employee ID already exists>".center(120,"-"))
            choice=input("Continue with a different Id?[Y/N]:- ").lower()
            if choice=="y":
                continue
            else:
                break
def total_salary():
    print("-".center(120,"-"))
    e_id=input("Employee_ID: ")
    if e_id in d:
        total_salary=d[e_id][1]+d[e_id][2]+d[e_id][3]
        print("Total_Salary=",total_salary)
    else:
        print("<This Employee ID does not exists>".center(120,"-"))
def total_allowance():
    print("-".center(120,"-"))
    e_id=input("Employee_ID: ")
    if e_id in d:
        total_allowance=d[e_id][2]+d[e_id][3]
        print("Total_Allowance=",total_allowance)
    else:
        print("<This Employee ID does not exists>".center(120,"-"))
def search():
    print("-".center(120,"-"))
    e_id=input("Employee_ID: ")
    if e_id in d:
        print("Name= ",d[e_id][0].title(),'\n',"Basic_Salary= ",d[e_id][1],'\n',"House-Rent_Allowance= ",d[e_id][2],'\n',"Conveyance_Allowance= ",d[e_id][3],sep="")
    else:
        print("<This Employee ID does not exists>".center(120,"-"))
while True:
    print('',"Main Menu".center(120,"-"),"","1: Add Employee","2: Total Salary","3: Total Allowance","4: Search","5: Exit",sep="\n")
    choice=input("Your_Choice: ")
    if choice=="1":
        add()
    elif choice=="2":
        total_salary()
    elif choice=="3":
        total_allowance()
    elif choice=="4":
        search()
    elif choice=="5":
        print('\n',"<Program has ended>".center(120,"-"),sep="")
        sleep(2)
        break
    else:
        print("<Invalid Choice>".center(120,"-"))
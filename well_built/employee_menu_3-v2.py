from time import sleep
d={}
def add():
    while True:
        try:
            e_id=int(input("Employee_ID: "))
            if e_id not in d:
                while True:
                    try:
                        name=input("Name: ").lower()
                        break
                    except:
                        print("<Name cannot be left empty>".center(80,"-"))
                        continue
                while True:
                    try:
                        basic_salary=int(input("Basic_Salary: "))
                        break
                    except:
                        print("<Basic_Salary must be numeric and cannot be left empty>".center(80,"-"))
                        continue
                while True:
                    try:
                        house_rent_allowance=int(input("House-Rent_Allowance: "))
                        break
                    except:
                        print("<House-Rent_Allowance must be numeric and cannot be left empty>".center(80,"-"))
                        continue
                while True:
                    try:
                        conveyance_allowance=int(input("Conveyance_Allowance: "))
                        break
                    except:
                        print("<Conveyance_Allowance must be numeric and cannot be left empty>".center(80,"-"))
                        continue
                d[e_id]=[name,basic_salary,house_rent_allowance,conveyance_allowance]
                print('\n',"<Added>".center(80,"-"),sep="")
                while True:
                    choice=input("More Employees? [Y/N]:- ").lower()
                    if choice=="y":
                        xd=1
                        break
                    elif choice=="n":
                        xd=0
                        break
                    else:
                        print("<Invalid Choice>".center(80,"-"))
                        continue
                if xd==1:
                    continue
            else:
                print("<This Employee_ID already exists>".center(80,"-"))
                while True:
                    choice=input("Continue with a different Id?[Y/N]:- ").lower()
                    if choice=="y":
                        xd=1
                        break
                    elif choice=="n":
                        xd=0
                        break
                    else:
                        print("<Invalid Choice>".center(80,"-"))
                        continue
                if xd==0:
                    break
                elif xd==1:
                    continue
        except:
            print("<Employee_ID must be numeric and cannot be left empty>".center(80,"-"))
def total_salary():
    while True:
        try:
            e_id=int(input("Employee_ID: "))
            break
        except:
            print("<Employee_ID must be numeric and cannot be left empty>".center(80,"-"))
            continue
    if e_id in d:
        total_salary=d[e_id][1]+d[e_id][2]+d[e_id][3]
        print("Total_Salary=",total_salary)
    else:
        print("<This Employee ID does not exists>".center(80,"-"))
def total_allowance():
    while True:
        try:
            e_id=int(input("Employee_ID: "))
            break
        except:
            print("<Employee_ID must be numeric and cannot be left empty>".center(80,"-"))
    if e_id in d:
        total_allowance=d[e_id][2]+d[e_id][3]
        print("Total_Allowance=",total_allowance)
    else:
        print("<This Employee ID does not exists>".center(80,"-"))
def search():
    while True:
        try:
            e_id=int(input("Employee_ID: "))
            break
        except:
            print("<Employee_ID must be numeric and cannot be left empty>".center(80,"-"))
            continue
    if e_id in d:
        print("Name= ",d[e_id][0].title(),'\n',"Basic_Salary= ",d[e_id][1],'\n',"House-Rent_Allowance= ",d[e_id][2],'\n',"Conveyance_Allowance= ",d[e_id][3],sep="")
    else:
        print("<This Employee ID does not exists>".center(80,"-"))
while True:
    print('',"Main Menu".center(80,"-"),"1: Add Employee","2: Total Salary","3: Total Allowance","4: Search","5: Exit",sep="\n")
    while True:
        try:
            choice=int(input("Your_Choice: "))
            if choice>5:
                print("<Invalid Choice>".center(80,"-"))
                continue
            break
        except:
            print("<Invalid Choice>".center(80,"-"))
            continue
    if choice==1:
        add()
    elif choice==2:
        total_salary()
    elif choice==3:
        total_allowance()
    elif choice==4:
        search()
    elif choice==5:
        print('\n',"<Program has ended>".center(80,"-"),sep="")
        sleep(1)
        break
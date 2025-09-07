import mysql.connector as m
from time import sleep
con=m.connect(user="root",password="258000",host="localhost")
cur=con.cursor()
cur.execute('show databases like "employee";')
if cur.fetchall()==[]:
    cur.execute("create database employee;use employee;create table details(id int primary key,name varchar(50) not null,basic_salary int default 0,HRA int default 0,CA int default 0);")
else:
    con=m.connect(user="root",password="258000",host="localhost",database="employee")
    cur=con.cursor()
def validate_id():
    while True:
        try:
            e_id=int(input("Employee_ID: "))
            cur.execute(f"select id from details where id={e_id};")
            if cur.fetchall()==[]:
                return False,e_id
            else:
                return True,e_id
        except:
            print("<Employee_ID must be numeric and cannot be left empty>".center(80,"-"))
def add():
    while True:
        f,e_id=validate_id()
        if f:
            print("<This Employee_ID already exists>".center(80,"-"))
            while True:
                choice=input("Continue with a different Id?[Y/N]:- ").lower()
                if choice=="y":
                    xd=0
                    break
                elif choice=="n":
                    xd=1
                    break
                else:
                    print("<Invalid Choice>".center(80,"-"))
                    continue
            if xd==1:
                break
        else:
            while True:
                name=input("Name: ").title()
                if not name=="":
                    break
                else:
                    print("<Name cannot be left empty>".center(80,"-"))
            while True:
                try:
                    basic_salary=int(input("Basic_Salary: "))
                    break
                except:
                    print("<Basic_Salary must be numeric and cannot be left empty>".center(80,"-"))
            while True:
                try:
                    HRA=int(input("House-Rent_Allowance: "))
                    break
                except:
                    print("<House-Rent_Allowance must be numeric and cannot be left empty>".center(80,"-"))
            while True:
                try:
                    CA=int(input("Conveyance_Allowance: "))
                    break
                except:
                    print("<Conveyance_Allowance must be numeric and cannot be left empty>".center(80,"-"))
            cur.execute(f"insert into details values({e_id},'{name}',{basic_salary},{HRA},{CA});")
            con.commit()
            print('\n',"<Added>".center(80,"-"),sep="")
            while True:
                choice=input("More Employees? [Y/N]:- ").lower()
                if choice=="y":
                    xd=0
                    break
                elif choice=="n":
                    xd=1
                    break
                else:
                    print("<Invalid Choice>".center(80,"-"))
                    continue
            if xd==1:
                break
def search_id():
    f,e_id=validate_id()
    if f:
        cur.execute(f"select * from details where id={e_id}")
        t=cur.fetchone()
        print("ID:-",t[0],"\nName:-",t[1],"\nBasic Salary:-",t[2],"\nHouse Rent Allowance:-",t[3],"\nConveyance Allowance:-",t[-1],sep="")
    else:
        print("<This Employee ID does not exists>".center(80,"-"))
def search_name():
    name=input("Name: ").title()
    cur.execute(f"select * from details where name like '{name}';")
    t=cur.fetchall()
    if not t==[]:
        print(f"Potential Matches:-")
        print(f"{'ID':<6}{'Name':<20}{'Basic Salary':<20}{'HRA':<10}{'CA':<10}","-".center(65,"-"),sep="\n")
        t1=0
        for i in t:
            print(f"{t[t1][0]:<6}{t[t1][1]:<20}{t[t1][2]:<20}{t[t1][3]:<10}{t[t1][4]:<10}")
            t1+=1
    else:
        print("<No matches found>".center(80,"-"))
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
while True:
    print('',"Main Menu".center(80,"-"),"1: Add Employee","2: Search with ID","3: Search with Name","4: Total Salary","5: Total Allowance","6: Exit",sep="\n")
    while True:
        try:
            choice=int(input("Your_Choice: "))
            if choice>6:
                print("<Invalid Choice>".center(80,"-"))
                continue
            break
        except:
            print("<Invalid Choice>".center(80,"-"))
            continue
    if choice==1:
        add()
    elif choice==2:
        search_id()
    elif choice==3:
        search_name()
    elif choice==4:
        total_allowance()
    elif choice==5:
        total_salary()
    elif choice==6:
        print('\n',"<Program has ended>".center(80,"-"),sep="")
        sleep(1)
        break
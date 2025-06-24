d={}
def add():
    while True:
        p_id=input("Patient ID: ")
        if p_id not in d:
            name=input("Name: ").lower()
            age=int(input("Age: "))
            ward=int(input("Ward no.: "))
            d[p_id]=[name,age,ward]
            print('\n',"<Added Successfully>".center(80,"-"))
            choice=input("Continue?[Y/N]:- ").lower()
            if choice=="y":
                continue
            else:
                break
        else:
            print("<This Patient ID already exists>".center(80,"-"))
            choice=input("Continue with a different Id?[Y/N]:- ").lower()
            if choice=="y":
                continue
            else:
                break
def search():
    p_id=input("Patient ID: ")
    if p_id in d:
        print("Name= ",d[p_id][0].title(),"\nAge= ",d[p_id][1],"\nWard no.= ",d[p_id][2],sep="")
    else:
        print("<This Patient ID does not exists>".center(80,"-"))
def delete():
    p_id=input("Patient ID: ")
    if p_id in d:
        d.pop(p_id)
        print("<Successfully deleted>".center(80,"-"))
    else:
        print("<This Patient ID does not exists>".center(80,"-"))
while True:
    print('\n',"Main Menu".center(80,"-"),"\n1: Add Patient","2: Search","3: Delete","4: Exit",sep="\n")
    choice=input("Your_Choice: ")
    if choice=="1":
        add()
    elif choice=="2":
        search()
    elif choice=="3":
        delete()
    elif choice=="4":
        print("<Program has ended>".center(80,"-"))
        break
    else:
        print("<Invalid Choice>".center(80,"-"))
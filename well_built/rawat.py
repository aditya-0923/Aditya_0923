d={}
def validate_id():
    while True:
        try:
            id1=int(input("ID: "))
            if len(str(id1))!=5:
                print("<ID must be numeric with exactly 5 digits>".center(80, "-"))
                continue
            return id1
            break
        except:
            print("<IF must be numeric>".center(80, "-"))
def add():
    while True:
        id1=validate_id()
        if id1 not in d:
            while True:
                name=input("Name: ").lower()
                if len(name)==0:
                    print("<Name cannot be left empty>".center(80,"-"))
                    continue
                else:
                    break
            while True:
                try:
                    batch=int(input("Batch no.: "))
                    break
                except:
                    print("<Batch number must be numeric and cannot be left empty>".center(80,"-"))
                    continue
            while True:
                try:
                    aadhaar=int(input("Aadhaar Number: "))
                    if len(str(aadhaar))!=16:
                        print("Aadhaar number must be of 16 digits".center(80,"-"))
                        continue
                    break
                except:
                    print("<Aadhaar number must be of 16 digits and cannot be left empty>".center(80,"-"))
                    continue
            d[id1]=[name,aadhaar,batch]
            print('\n',"<Added>".center(80,"-"),sep="")
            while True:
                choice=input("More enteries to be added? [Y/N]:- ").lower()
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
        else:
            print("<This ID already exists>".center(80,"-"))
            while True:
                choice=input("Continue with a different ID?[Y/N]:- ").lower()
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
def search():
    id1=validate_id()
    if id1 in d:
        print("-".center(80,"-"),'\n',"Name= ",d[id1][0].title(),'\n',"Aadhaar Number= ",d[id1][1],'\n',"Batch no.= ",d[id1][2],'\n',sep="")
    else:
        print("<This ID does not exists>".center(80,"-"))
def delete():
    id1=validate_id()
    if id1 in d:
        del d[id1]
        print("Record deleted successfully")
    else:
        print("This ID does not exists>".center(80,"-"))
while True:
    print('',"Main Menu".center(80,"-"),"1: Add ID","2: Search Details","3: Delete record","4: Exit",sep="\n")
    while True:
        try:
            choice=int(input("Your_Choice: "))
            break
        except:
            print("<Invalid Choice>".center(80,"-"))
            continue
    if choice==1:
        add()
    elif choice==2:
        search()
    elif choice==3:
        delete()
    elif choice==4:
        print('\n',"<Program has ended>".center(80,"-"),sep="")
        break
    else:
        print("<Invalid Choice>".center(80,"-"))
        continue
a=input()
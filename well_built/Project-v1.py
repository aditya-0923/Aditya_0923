while True:
    password=input("Password:- ")
    if password=="ADMIN420":
        print("Access Granted".center(80,"-"))
        break
    else:
        print("Access Denied".center(80,"-"))
        continue
d={}
def account_number():
    while True:
        try:
            acc_num=int(input("Account Number: "))
            if len(str(acc_num))!=10:
                print("<Account Number must be numeric with exactly 10 digits>".center(80, "-"))
                continue
            return acc_num
            break
        except:
            print("<Account Number must be numeric>".center(80, "-"))
def add():
    while True:
        acc_num=account_number()
        if acc_num not in d:
            while True:
                name=input("Name: ").lower()
                if len(name)==0:
                    print("<Name cannot be left empty>".center(80,"-"))
                    continue
                else:
                    break
            while True:
                try:
                    opening_deposit=int(input("Opening Deposit: "))
                    break
                except:
                    print("<Opening Deposit must be numeric and cannot be left empty>".center(80,"-"))
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
            current_balance=opening_deposit
            d[acc_num]=[name,aadhaar,opening_deposit,current_balance]
            print('\n',"<Added>".center(80,"-"),sep="")
            while True:
                choice=input("More accounts to be added? [Y/N]:- ").lower()
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
            print("<This Account number already exists>".center(80,"-"))
            while True:
                choice=input("Continue with a different Account Number?[Y/N]:- ").lower()
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
    acc_num=account_number()
    if acc_num in d:
        print("-".center(80,"-"),'\n',"Name= ",d[acc_num][0].title(),'\n',"Aadhaar Number= ",d[acc_num][1],'\n',"Opening Deposit= ",d[acc_num][2],'\n',"Current Balance= ",d[acc_num][3],sep="")
    else:
        print("<This Account Number does not exists>".center(80,"-"))
def current_balance_fn():
    acc_num=account_number()
    if acc_num in d:
        print("Current Balance=",d[acc_num][3],)
    else:
        print("<This Account Number does not exists>".center(80,"-"))
def update_fn():
    acc_num=account_number()
    if acc_num in d:
        while True:
            print("1: Credit\n2: Debit")
            try:
                choice=int(input("Your_Choice: "))
                if choice==1:
                    while True:
                        try:
                            cr=int(input("Amount to be credited: "))
                            d[acc_num][3]+=cr
                            print("<Amount Credited Successfully>".center(80, "-"))
                            break
                        except:
                            print("<Enter the Amount to be credited>".center(80,"-"))
                            continue
                    break
                elif choice==2:
                    while True:
                        try:
                            debit=int(input("Amount to be debited: "))
                            if d[acc_num][3]>debit:
                                d[acc_num][3]-=debit
                                print("<Amount Debited Successfully>".center(80, "-"))
                            else:
                                print("<Insufficient Balance>".center(80,"-"))
                            break
                        except:
                            print("<Enter the Amount to be Debited>".center(80,"-"))
                            continue
                    break
                else:
                    print("<Invalid Choice>".center(80,"-"))
            except:
                print("<Invalid Choice>".center(80,"-"))
                continue
    else:
        print("<This Account Number does not exists>".center(80,"-"))
while True:
    print('',"Main Menu".center(80,"-"),"1: Add Account","2: Search Details","3: Current Balance","4: Update","5: Exit",sep="\n")
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
        current_balance_fn()
    elif choice==4:
        update_fn()
    elif choice==5:
        print('\n',"<Program has ended>".center(80,"-"),sep="")
        break
    else:
        print("<Invalid Choice>".center(80,"-"))
        continue
zaza=input()

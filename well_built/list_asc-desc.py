while True:
    l=[1,2,3,4,5,6]
    while True:
        try:
            choice=int(input("default list[0] or custom list[1]? [0/1]:- "))
        except:
            print("Invalid Entry".center(80,"-"))
            continue
        if choice==0:
            break
        elif choice==1:
            l.clear()
            while True:
                try:
                    l=eval(input("Enter a list using this format- [x,y,z]:- "))
                    if type(l)!=list:
                        print("Only list is allowed and Follow the Format- [x,y,z]".center(80,"-"))
                        continue
                except:
                    print("Follow the Format- [x,y,z]".center(80,"-"))
                    continue
                break
            break
        else:
            print("Invalid Entry".center(80,"-"))
            continue
    a=l[0]
    b,c=0,0
    for i in l:
        if i>a:
            a=i
            if c==0:
                b=1
                continue
            else:
                b,c=0,0
                break
        elif i<a:
            a=i
            if b==0:
                c=1
                continue
            else:
                b,c=0,0
                break
    print(l,end="-- ")
    if b==1 and c==0:
        print("Ascending")
    elif b==0 and c==1:
        print("Descending")
    else:
        print("Unordered")
    while True:
        try:
            again=int(input("Again? [0/1]:- "))
            if again>1:
                print("Invalid Entry".center(80,"-"))
                continue
            break
        except:
            print("Invalid Entry".center(80,"-"))
            continue
    if again==0:
        break
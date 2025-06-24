while True:
    l=[2,1,2,1,2,1,3,4,3,2,4,3,1,4]
    while True:
        choice=input("default list[0] or custom list[1]? [0/1]:- ")
        if choice=="0":
            break
        elif choice=="1":
            l.clear()
            while True:
                x=input("Element to be added:- ")
                if not x.isdigit():
                    print("Invalid Entry".center(80,"-"))
                    continue
                l.append(int(x))
                while True:
                    choice=input("Add more elements? [0/1]:-")
                    if choice=="0":
                        xd=0
                        break
                    elif choice=="1":
                        xd=1
                        break
                    else:
                        print("Invalid Entry".center(80,"-"))
                        continue
                if xd==0:
                    break
                else:
                    continue
            break
        else:
            print("Invalid Entry".center(80,"-"))
            continue
    print("Original List:-",l)
    l1=[]
    l2=[]
    for i in l:
        if l.count(i)>1:
            l1.append(i)
            l.remove(i)
    for i in l1:
        if i not in l2:
            l2.append(i)
    print("Extra elements:-",l1)
    l3=[]
    b=0
    for i in l1:
        if i not in l3:
            b=l1.count(i)
            l3.append(i)
            print("Frequency of ",i,":- ",b,sep="")
        else:
            continue
    print("Final List:-",l)
    z=""
    while True:
      exit=input("Exit[0] or Continue[1]? [0/1]:-")
      if exit=="0" or exit=="1":
          z=exit
          break
      else:
          print("Invalid Entry".center(80,"-"))
          continue
    if z=="0":
      break
    else:
      continue
def l_swap(l):
    a=0
    while a<len(l)//2:
        l.append(l.pop(0))
        a+=1
    return l

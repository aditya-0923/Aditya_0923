a= int(input("C.S." ))
b= int(input("Maths " ))
c= int(input("Chemistry"  ))
d= int(input("Physics"  ))
e= int(input("English"  ))
f= (a+b+c+d+e)/5
if f >90 and f<=100 :
    print("Grade A")
elif f>80 and f<=90 :
    print("Grade B")
elif f>70 and f<=80 :
    print("Grade C")
elif f>60 and f<=70 :
    print("Grade D")
elif f<60 :
    print("Grade E")
else :
    print("number above than 100 is invalid")

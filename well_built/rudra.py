d = {}
del_rec = {}

def a():
    k = int(input("Enter roll number: "))
    n = input("Enter name: ")
    subs = ['Math', 'Sci', 'Eng', 'Hist', 'Geo']
    mks = []
    for sub in subs:
        mk = int(input(f"Enter marks for {sub}: "))
        mks.append(mk)
    f = int(input("Enter fee: "))
    d[k] = {'name': n, 'marks': mks, 'fee': f}

def b():
    rno = int(input("Enter student roll number: "))
    if rno in d:
        del_rec[rno] = d.pop(rno)
        print("Record deleted.")
    else:
        print("Roll number doesn't exist.")

def c():
    rno = int(input("Enter roll number: "))
    if rno in d:
        details = d[rno]
        total = sum(details['marks'])
        pct = (total / 500) * 100
        res = 'Pass' if pct >= 33 else 'Fail'
        print(f"Roll Number: {rno}, Name: {details['name']}, Marks: {details['marks']}, Fee: {details['fee']}, Percentage: {pct:.2f}%, Result: {res}")
    else:
        print("Roll number doesn't exist.")

def d1():
    rno = int(input("Enter student roll number to modify: "))
    if rno in d:
        subs = ['Math', 'Sci', 'Eng', 'Hist', 'Geo']
        mks = []
        for sub in subs:
            mk = int(input(f"Enter new marks for {sub}: "))
            mks.append(mk)
        f = int(input("Enter new fee: "))
        d[rno]['marks'] = mks
        d[rno]['fee'] = f
        print("Record modified.")
    else:
        print("Roll number doesn't exist.")

def e():
    if not d:
        print("No records found.")
    else:
        print("Student Details:")
        for rno, details in d.items():
            total = sum(details['marks'])
            pct = (total / 500) * 100
            res = 'Pass' if pct >= 33 else 'Fail'
            print(f"Roll Number: {rno}, Name: {details['name']}, Marks: {details['marks']}, Fee: {details['fee']}, Percentage: {pct:.2f}%, Result: {res}")

def f():
    if not del_rec:
        print("No deleted records found.")
    else:
        print("Deleted Records:")
        for rno, details in del_rec.items():
            total = sum(details['marks'])
            pct = (total / 500) * 100
            res = 'Pass' if pct >= 33 else 'Fail'
            print(f"Roll Number: {rno}, Name: {details['name']}, Marks: {details['marks']}, Fee: {details['fee']}, Percentage: {pct:.2f}%, Result: {res}")

def g():
    if not d:
        print("No records found.")
    else:
        total_students = len(d)
        total_marks = 0
        highest = -1
        lowest = float('inf')
        pass_count = 0
        fail_count = 0
        
        for details in d.values():
            sum_mks = sum(details['marks'])
            total_marks += sum_mks
            pct = (sum_mks / 500) * 100
            if pct >= 33:
                pass_count += 1
            else:
                fail_count += 1
            if sum_mks > highest:
                highest = sum_mks
            if sum_mks < lowest:
                lowest = sum_mks
        
        avg_marks = total_marks / total_students
        print("Class Summary:")
        print(f"Total Students: {total_students}")
        print(f"Average Marks: {avg_marks:.2f}")
        print(f"Highest Marks: {highest}")
        print(f"Lowest Marks: {lowest}")
        print(f"Pass Count: {pass_count}")
        print(f"Fail Count: {fail_count}")

while True:
    print("\n1. Add a record")
    print("2. Delete")
    print("3. Search")
    print("4. Modify")
    print("5. Display all records")
    print("6. Display deleted records")
    print("7. Display class summary")
    print("8. Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        a()
    elif ch == 2:
        b()
    elif ch == 3:
        c()
    elif ch == 4:
        d1()
    elif ch == 5:
        e()
    elif ch == 6:
        f()
    elif ch == 7:
        g()
    elif ch == 8:
        break
    else:
        print("Enter a value between 1 to 8")
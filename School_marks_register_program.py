import csv

classno = input("Enter class and section- ")

f = open(f"{classno}_Student_List.csv", "a+", newline='')
wr = csv.writer(f)

f.seek(0)
if list(csv.reader(f)) == []:
    wr.writerow(['Roll_no', 'Name', "English", "Maths", "Physics", "Chemistry", "Computer"])

def get_rowelements(rownum):
    # This function returns a list having all elements in a row when we mention the row's index number
    data = list(csv.reader(f))[1:]
    rowlst = []
    for row in data:
        rowlst.append(row[rownum])
    return rowlst

def unique_rollno(prompt):
    rno = 0
    rnolst = get_rowelements(0)
    while rno in rnolst or rno <=0:
        rno = int(input(prompt))
    return rno

def get_mark(prompt):
    mark = -1
    while mark > 100 or mark < 0:
        mark = int(input(prompt))
    return mark

def add_student():
    no = int(input("Number of students to be added- "))

    for i in range(no):
        name = input(f"Enter name of Student {i+1}- ")
        roll = unique_rollno(f'Enter Roll number of Student {i+1}- ')
        eng = get_mark(f'Enter English Mark of Student {i+1}- ')
        math = get_mark(f'Enter Maths Mark of Student {i+1}- ')
        phy = get_mark(f'Enter Physics Mark of Student {i+1}- ')
        chem = get_mark(f'Enter Chemistry Mark of Student {i+1}- ')
        cs = get_mark(f'Enter CS Mark of Student {i+1}- ')
        print()
        wr.writerow([roll, name, eng, math, phy, chem, cs])
    f.flush()

def print_data():
    f.seek(0)
    data = list(csv.reader(f))
    #print(data, type(data), list(data))
    print('Roll_no', 'Name', "English", "Maths", "Physics", "Chemistry", "Computer", end="\t\t")
    print()
    for ls in data[1:]:
        #print(i)
        for j in ls:
            print(j, end="\t")
        print()
    print()
    
def rem_student(rele):
    f.seek(0)
    data = list(csv.reader(f))
    for i in range(len(data))[1:]:
        if int(data[i][0]) == rele:
            print('Data of student removed from list-', data.pop(i))
            break
    else:
        print("Roll number not found!")

    global classno
    with open(f"{classno}_Student_List.csv", "w+", newline='') as rwf:
        csv.writer(rwf).writerows(data)
    print()

def instruction():
    print('''Welcome to Student Register!
Press respective option number to use service.
    0. Instructions
    1. Add student to list.
    2. Display data in list.
    3. Remove a student from list.
    4. Exit''')
    print()

instruction()
n = int(input("Enter option- "))

while True:
    if n == 1:
        add_student()
    elif n == 2:
        print_data()
    elif n == 3:
        rem_student(int(input("Enter roll number of student to be removed- ")))
    elif n == 4:
        print("Thank you!")
        break
    elif n == 0:
        instruction()
    else:
        print("Enter a valid option number.\n")
    n = int(input("Enter option- "))

f.close()

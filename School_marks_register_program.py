import csv

classno = input("Enter class and section- ")

f = open(f"{classno}_Student_List.csv", "a+", newline='')
f.seek(0)
rowcount = len(list(csv.reader(f))) - 2
wr = csv.writer(f)

f.seek(0)
if list(csv.reader(f)) == []:
    wr.writerow(['Roll_no', 'Name', "English", "Maths", "Physics", "Chemistry", "Computer"])
    rowcount += 1
    f.flush()

def get_rowelements(rownum):
    # This function returns a list having all elements in a row when we mention the row's index number
    f.seek(0)
    data = list(csv.reader(f))[1:]
    rowlst = []
    for row in data:
        rowlst.append(row[rownum])
    return rowlst

def get_mark(prompt):
    while True:
        try:
            mark = -1
            while mark > 100 or mark < 0:
                mark = int(input(prompt))
        except:
            continue
        else:
            return mark

def add_student():
    no = get_mark("Number of students to be added- ")
    global rowcount

    for i in range(no):
        rowcount += 1
        name = input(f"Enter name of Student {i+1}- ")
        roll = rowcount + 1
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
    print('Roll_no ', 'Name  ', "English ", "Maths ", "Physics ", "Chemistry", "Computer", "Total", sep="  ")
    for ls in data[1:]:
        #print(i)
        for j in ls:
            print(j, end="        ")
        s = 0
        for x in range(2, 7):
            s += int(ls[x])
        print(s)
    print()
    
def rem_student(rele):
    f.seek(0)
    global rowcount
    data = list(csv.reader(f))
    for i in range(len(data))[1:]:
        if int(data[i][0]) == rele:
            print('Data of student removed from list-', data.pop(i))
            rowcount -= 1
            break
    else:
        print("Roll number not found!")

    global classno
    with open(f"{classno}_Student_List.csv", "w+", newline='') as rwf:
        csv.writer(rwf).writerows(data)
    print()

def mark_statistic():
    f.seek(0)
    global rowcount
    SubjectMarkDict = {}
    SubjectNames = ["English  ", "Maths    ", "Physics  ", "Chemistry", "Computer "]
    for i in range(2, 7):
        SubjectMarkDict[SubjectNames[i-2]] = get_rowelements(i)
    try:
        print("Subject", "  Max. mark", "Min. mark", sep="\t\t")
        for subject, markls in SubjectMarkDict.items():
            print(subject, max(markls), min(markls), sep='\t\t')
    except ValueError:
            print("File is Empty!")
    print()

def instruction():
    print('''Welcome to Student Register!
Press respective option number to use service.
    0. Instructions
    1. Add student to list.
    2. Display data in list.
    3. Remove a student from list.
    4. Display Highest mark and Lowest Mark in each subject.
    5. Exit''')
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
        mark_statistic()
    elif n == 5:
        print("Thank you!")
        break
    elif n == 0:
        instruction()
    else:
        print("Enter a valid option number.\n")
    n = int(input("Enter option- "))

f.close()

classno = input("Enter class and section- ")

f = open(f"{classno}_Student_List.csv", "a+", newline='')
import csv
wr = csv.writer(f)

f.seek(0)
if list(csv.reader(f)) == []:
    wr.writerow(['name', 'roll_no', "English", "Maths", "Physics", "Chemistry", "Computer"])

def add_student():
    no = int(input("Number of students to be added- "))

    for i in range(no):
        name = input("Enter name of Student- ")
        roll = int(input('Enter Roll number of Student- '))
        eng = int(input('Enter English Mark of Student- '))
        math = int(input('Enter Maths Mark of Student- '))
        phy = int(input('Enter Physics Mark of Student- '))
        chem = int(input('Enter Chemistry Mark of Student- '))
        cs = int(input('Enter CS Mark of Student- '))
        print()
        wr.writerow([name, roll, eng, math, phy, chem, cs])
    f.flush()

def print_data():
    f.seek(0)
    data = list(csv.reader(f))
    #print(data, type(data), list(data))
    print('name', 'roll_no', "English", "Maths", "Physics", "Chemistry", "Computer", end="\t\t")
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
        if int(data[i][1]) == rele:
            print('Data of student removed from list-', data.pop(i))
            break
    else:
        print("Roll number not found!")
        
    return data

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
        newls = rem_student(int(input("Enter roll number of student to be removed- ")))
        with open(f"{classno}_Student_List.csv", "w+", newline='') as rwf:
            wr.writerows(newls)
        print()
    elif n == 4:
        print("Thank you!")
        break
    elif n == 0:
        instruction()
    else:
        print("Enter a valid option number.\n")
    n = int(input("Enter option- "))

f.close()

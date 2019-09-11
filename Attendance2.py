import pandas as pd
import csv



def addParticipant():
    f = open('On the Spot.csv', "a")
    more='y'
    while more=='y':
        print("Enter Name:")
        name = str(input())
        print("Enter Branch:")
        branch = str(input())
        print("Enter Year:  (1,2,3 or 4)")
        year = int(input())
        print("For or Against:")
        side = str(input())
        print("Enter Phone Number:")
        phone = input()
        print("Enter Email Address:")
        email = str(input())
        row = [name, branch, year, side, phone, email, '1']
        file1 = csv.writer(f)
        file1.writerow(row)
        print("Record Added!")
        more=input("Add more?")
    f.close()

def attendance():
    more='y'
    flag=1
    while more=='y':
        df = pd.read_csv('Registrations.csv')
        df2 = pd.read_csv('Final Attendance.csv')
        attendees1=[]
        df.dropna(inplace=True)
        print("Enter Name:")
        name = str(input())
        df2= df[df["Name"].str.contains(name)]
        print(df2)
        if(flag==1):
            export_csv=df2.to_csv ('Final Attendance.csv', index = None, header=True)
            flag=0
        else:
            attendees1=df2.values.tolist()
            f2=open('Final Attendance.csv',"a")
            file2=csv.writer(f2)
            file2.writerow(attendees1)
        more=input("Mark Attendance of more Students?")

def extract():
    df = pd.read_csv('Registrations.csv')
    df1 = df[df['Attendance'] == 1]
    df1.reset_index()
    df1.to_csv("Final Attendance.csv", index=False)


if __name__ == '__main__':
    running = True
    print("Debsos DITU\n")
    ch = 'y'
    while running:
        p = int(input("1. Add a Participant\n2. Mark Attendance\n3. Extract CSV\nInput:"))
        if p == 1:
            addParticipant()
        elif p == 2:
            attendance()
        elif p == 3:
            extract()
        else:
            print("Invalid Input. ")
        print("Press y to continue")
        ch = input()
        if not (ch == 'y' or ch == 'Y'):
            running = False

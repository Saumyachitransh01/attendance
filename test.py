f = open(r"C:\Users\ansh\Desktop\Python\Attendance2\Final Attendance.csv",'r')
f1 = f.read()
for i in f1:
    name,branch,year,part,phone,email,attendance = i.split(",")
    print(name)
    print(branch)
    print(year)
    print(part)
    print(phone)
    print(email)
    print(attendance)


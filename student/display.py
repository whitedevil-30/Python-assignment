import student.newstu as ns
def display():
    print("Students Details")
    for i in range(0,len(ns.rollno)):
            print("Student Roll No = "+ns.rollno[i])
            print("Student Name = "+ns.name[i])
            print("Student Year = "+ns.year[i])
            print("Student Branch = "+ns.branch[i])
            i+=1
import student.newstu as ns
def search():   
    rn=input("Enter The Roll NO. To See Details: ")
    i=ns.rollno.index(rn)
    print("Student Roll No = "+ns.rollno[i])
    print("Student Name = "+ns.name[i])
    print("Student Year = "+ns.year[i])
    print("Student Branch = "+ns.branch[i])
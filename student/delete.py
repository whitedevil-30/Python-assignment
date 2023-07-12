import student.newstu as ns
def dele():
    rn=input("Enter The Roll NO. To Delete Details: ")
    i=ns.rollno.index(rn)
    ns.name.pop(i)
    ns.rollno.pop(i)
    ns.year.pop(i)
    ns.branch.pop(i)
    print("Record Deleted Successfully!!")
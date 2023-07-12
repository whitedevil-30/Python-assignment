name=[]
rollno=[]
year=[]
branch=[]

def add():
    i=0
    f=open("Studentrec.txt","+a")
    try:
        print("Enter Students Details: ")
        name.append(input("Enter Name Of The Student: "))
        rollno.append(input("Enter Roll No. Of Student: "))
        year.append(input("Enter Year Of Student:"))
        branch.append(input("Enter Branch Of Student: "))

        f.writelines(["Student Roll No = "+rollno[i]+"\n"])
        f.writelines(["Student Name = "+name[i]+"\n"])
        f.writelines(["Student Year = "+year[i]+"\n"])
        f.writelines(["Student Branch = "+branch[i]+"\n"])    
        i+=1
    except:
        if(IOError):
            print("Error In Storing Data")
        elif(IndexError):
            print("Error In Accessing Index")
        else:
            print("Record Added Successfully")
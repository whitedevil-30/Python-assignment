
#Assignment 1
a=int(input("Enter 1 num : "))
b=int(input("Enter 2 num : "))
c=int(input("Enter 3 num : "))
d = ((a+b+c)/3)
print(d)

#Assignment 2
a=10
b=5
print("floor division: ",a//b)
print("exponent: ",a**b)
print("mod: ",a%b)

a=10
a**=1
print("**=",a)
a=10
a//=1
print("//=",a)
a=10
a%=1
print("%=",a)

print("<",a<b)
print("==",a==b)
print("!=",a!=b)

a=True
b=False
print("and",a and b)
print("or",a or b)
print("not",not b)

print("bitwise ^",a^b)
print("bitwise >>",a>>b)
print("bitwise <<",a<<b)

print("is",a is b)
print("is not",a is not b)

a="hello"
print('h' in a)
print("j" not in a)

#Assignment 3
n1=1
while n1==1:
    a = (float(input("Enter the first num : ")))
    b = (float(input("Enter the second num : ")))
    d = input("Enter the following \n+ for Adddition or \n- for Subtraction or\n* for Multiplication or\n/ for Division : ")
    if d=="+":
        c=a+b
        print("Addition = ",c)
    elif d=="-":
        c=a-b
        print("Subtraction = ",c)
    elif d=="*":
        c=a*b
        print("Multiplication = ",c)
    elif d=="/":
        c=a/b
        print("Division = ",c)
    else:
        print("Invalid ")
    n = (int(input("Press 1 for continue or 0 for exit : ")))
    if n!=1:
        print("Thank You!! \3")
        exit()
    n1=n

#Assignment 4
a = "hello"
for i in a:
    if i=="l":
        break  
    else:
        print(i)
else:
    print("Ite has break")

a = "hello"
for i in a:
    if i=="l":
        continue 
    else:
        print(i)
else:
    print("Ite has continue")

a = "hello"
for i in a:
    if i=="l": 
        pass 
    else:
        print(i)
else:
    print("Ite has pass")

i = 1
while i<=10:
    if i==5:
        i+=1
        continue
    else:
        print(i)
    i+=1
else:
    print("it has break")

#Assignment 5
l=[]
print("Enter 5 num")
for i in range(1,6):
    a=int(input())
    l.append(a)

print("Sum : ",sum(l))
print("Min : ",min(l))
print("Max : ",max(l))
l.sort()
print("Ascending : ",l)
l.sort(reverse=True)
print("Descending : ",l)
print(tuple(l))
del l
print(l)

#Assignment 6
def ds(rollno,name):
    ls = [rollno,name]
    tp = (rollno,name)
    dt = {"rollno":rollno,"name":name}
    st = {rollno,name}
    print("\n\nBefore changes=\n")
    print(ls)
    print(tp)
    print(dt)
    print(st)
    ls[0] = 20
    ls[1] = "xyz"
    tp = (20,"xyz")
    dt.update({"rollno":20,"name":"xyz"})
    st = {20,"xyz"}
    print("\nAfter changes=\n")
    print(ls)
    print(tp)
    print(dt)
    print(st)
    
    del ls
    del tp
    del dt
    del st
nm = input("Enter name : ")
rol = int(input("Enter rollno : "))
ds(rol,nm)

#Assignment 7
def fn(file="abc.txt"):
    f = open(file,'a')
    rollno = input("Enter your roll number : ")
    name = input("Enter your name : ")
    div = input("Enter your div : ")
    f.writelines([rollno,"\n",name,"\n",div])

    f = open(file,'r')
    data =f.readlines()
    for i in data:
        print(i)

fn()

#Assignment 8
class A:
    def __init__(self,a,b,c):
        self.__A = a
        self._B = b
        self.C = c
    def display(self):
        print("A=",self.__A)
        print("B=",self._b)
        print("C=",self.C)
class B(A):
    def __init__(self,a,b,c):
        super().__init__(a,b,c)
    def display(self):
        try:
            print("A is private")
            raise Exception
        except Exception:
            print("Exception occured")
        finally:
            print("B=",self._B)
            print("C=",self.C)
obj = B(10, 20, 30)
obj.display()

# Assignment 9
from operation9 import MathOperations, ZeroDivisionException

math_ops = MathOperations(10, 2)

print("Addition:", math_ops.add())
print("Subtraction:", math_ops.subtract())
print("Multiplication:", math_ops.multiply())

try:
    print("Division:", math_ops.divide())
except ZeroDivisionException as e:
    print("Error:", str(e))

print("Square Root:", math_ops.square_root())

# Assignment 10
import tkinter as tk 
import webbrowser as wb 
obj=tk.Tk()
e=tk.Entry(obj,font=("TImes new Roman",20),width=20)
e.grid()
def search():
    query=str(e.get())
    query = query.replace(' ', '+')
    print(f'Navigting to {query}')
    wb.open(f'https://bing.com/search?q={query}')

    
    
b=tk.Button(obj,text="Close",font=("Times New Roman",20),command=obj.destroy)
b1=tk.Button(obj,text="Search",font=("Times New Roman",20),command=search)
b.grid(row=3)
b1.grid(row=2)
obj.mainloop()

# Assignment 11
import tkinter as tk
import webbrowser as wb
root=tk.Tk()
root.title("Flipkart Form")
l1=tk.Label(root,text="Enter Your Name",
           font=("Times New Roman",20))
l1.grid()
e1=tk.Entry(root,font=("Times New Roman",20),width=25)
e1.grid()
l2=tk.Label(root,text="Phone-No.",
           font=("Times New Roman",20))
l2.grid()
e2=tk.Entry(root,font=("Times New Roman",20),width=25)
e2.grid()
l3=tk.Label(root,text="Enter Your username",
           font=("Times New Roman",20))
l3.grid()
e3=tk.Entry(root,font=("Times New Roman",20),width=25)
e3.grid()
l4=tk.Label(root,text="Enter Your password",
           font=("Times New Roman",20))
l4.grid()
e4=tk.Entry(root,font=("Times New Roman",20),width=25,)
e4.grid()
clicked= tk.StringVar()
l5=tk.Label(root,text="",
           font=("Times New Roman",30))
l5.grid()

def submit():

    if(e1.get()=="" and e2.get()==""):
        l5["text"]="* Please Enter The Information"
    elif(e3.get()=="" and e4.get()==""):
        l5["text"]="* Please Enter The Information"
    else:
        try:
            f=open("data.txt","+w")
            f.writelines(["Name="+e1.get()+"\n"])
            f.writelines(["MobileNo="+e2.get()+"\n"])
            f.writelines(["Username="+e3.get()+"\n"])
            f.writelines(["Password="+e4.get()+"\n"])
            f.writelines(["Site Name ="+clicked.get()])
            f.close()
        except IOError:
            print("Form Data Storage Failed")
        wb.open("https://affiliate.flipkart.com/login")
    
b=tk.Button(root,text="Login",font=("TIMES NEW ROMAN",15),
            command=submit,bg="blue",
            activebackground="purple")
b.grid()
tk.mainloop()

# Assignment 12
import student.delete as sdel
import student.newstu as sadd
import student.search as ssear
import student.display as sdis
import student.count as scount
class inavlidOption(Exception):
    def __init__(self, *msg):
        super().__init__(*msg)
        
i=1
while i==1:
    try:
        print("Enter 1 To Add Student Record\n"\
              "Enter 2 To Display All Student Record\n"\
              "Enter 3 To Delete a Student Record\n"\
              "Enter 4 To Search a Student Record\n"\
              "Enter 5 To Count Number Of Record"  )
        c=int(input('Enter number: '))
        if(c==1):
            sadd.add()
        elif(c==2):
            sdis.display()
        elif(c==3):
            sdel.dele()
        elif(c==4):
            ssear.search()
        elif(c==5):
            scount.counted()
        else:
            raise inavlidOption("Invalid choice")
    except inavlidOption as io:
        print(io.args[0])
    a=int(input('Enter 1 to continue else any key exit: '))
    if a!=1:
        exit()
    else:
        i=a
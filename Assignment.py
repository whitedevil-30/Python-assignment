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
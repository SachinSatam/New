a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
print("Before swapping a & b are:",a,b)
temp=a
a=b
b=temp
print("After swapping a & b are:",a,b)
if(a==0):
    print("a is zero")
elif(a>0):
    print("a is positive")
else:
    print("a is negative")
if(b==0):
    print("b is zero")
elif(b>0):
    print("b is positive")
else:
    print("b is negative")             
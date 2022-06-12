from array import *
num=array('i',[])
size=int(input("Enter the size of the array:"))
for i in range(0,size):
    n=int(input("Enter the array element:"))
    num.append(n)
sum=0
for i in num:
    sum=sum+i
print("Sum of the array is:",sum)
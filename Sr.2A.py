def even_odd():
   list = []
   n = int(input("Enter number of elements : "))
   for i in range(0, n):
    ele = int(input("Enter the element"))
    list.append(ele)
    even=sorted([e for e in list if e % 2==0])
    odd=sorted([e for e in list if e % 2 !=0])
    print(even)
    print(odd)
even_odd()   



list=[1,2,3,4,5,6]
y=int(input("Enter the index of element to be changed:"))
z=int(input("Enter the updated element"))
for x in range(0,len(list)-3):
   if(list[x]==y):
      list[x]=z
print(list)


def MaxMin():
   list = []
   n = int(input("Enter number of elements : "))
   for i in range(0, n):
    ele = int(input("Enter the element"))
    list.append(ele)
    print("Maximum element is:",max(list))
    print("Mnimum element is: ",min(list))
MaxMin()

def check():
   list=[]
   n=int(input("Enter the number of strings in list:"))
   for i in range(0,n):
    str1=str(input("Enter the string:"))
    list.append(str1)
    print(list)
   for x in range(0,len(list)):
      if(list[x]=='python'):
         print("Matching String'python' found")
check()  
       

  
        


def Pattern1():
 for i in range(n):
    for j in range(n - i - 1):
        print(" ", end='')
    for k in range( 2*i + 1):
        print("*", end="")
    print("")

def Pattern2():
 for i in range(n):
    for j in range(i+1):
        print("* ", end="")
    print("\n") 

def Pattern3():  
 for i in range(n,0,-1):
    for k in range(0,n-i):    
        print("  ",end="")
    for j in range(1, i + 1):  
        print("*", end=" ")       
    print("\n")
while True:    
    print("1.Pattern 1 ")  
    print("2.Pattern 2 ")  
    print("3.Pattern 3 ")  
    users_choice = int(input("\nEnter your Choice: "))

    if users_choice == 1:  
        n = int(input("Enter number of rows: ")) 
        Pattern1()
    elif users_choice==2:
        n = int(input("Enter number of rows: ")) 
        Pattern2()
    elif users_choice==3:
        n = int(input("Enter number of rows: "))
        Pattern3()
    else:
         print("Wrong choice")                              
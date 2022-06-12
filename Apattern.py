result_str="";    
for row in range(0,7):    
    for column in range(0,7):     
        if (((column == 1 or column == 5) and row != 0)or((row==0 or row == 3)and (column > 1 and column <5))):
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str)
    
for i in range(0, 7):
    for j in range(0, 7):
        if(i == j or j == 7 - 1 - i):
            print('*', end = '')
        else:
            print(' ', end = '')
    print()
result_str="";    
for row in range(0,7):    
    for column in range(0,7):     
        if (((row == 0 or row == 6) and column >=0 and column <=6) or row+column==6): 
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str)

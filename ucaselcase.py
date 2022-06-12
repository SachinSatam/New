str=input("Enter a string:")
uppercase=0
lowercase=0
for i in range(len(str)):
    if(str[i]>='a' and str[i]<='z'):
        lowercase += 1
    else:
        uppercase +=1
print("Lowercase letters are",lowercase)
print("Uppercase letters are",uppercase)

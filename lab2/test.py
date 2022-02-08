import sys 
s=input() 

for i in range(len(s)):
    if s[i]!='(' or s[i]!='{' or s[i]!='[': 
        print("No") 
        sys.exit() 
    if s[i]=='(' and s[i+1]!=')': 
        print("No") 
        sys.exit() 
    elif s[i]=='{' and s[i+1]!='}': 
        print("No") 
        sys.exit() 
    elif s[i]=='[' and s[i+1]!=']': 
        print("No") 
        sys.exit()         
print("Yes")
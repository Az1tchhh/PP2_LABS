number = int(input())
set_of_strong_passwords = {''}
for i in range(number):
    letter_count = 0
    upper_count = 0
    lower_count = 0
    number_count = 0
    password = input()
    for j in range(len(password)):
        if(password[j]>='a' and password[j]<='z' or password[j]>='A' and password[j]<='Z'):
            letter_count+=1
            
        if(password[j]==password[j].upper() and (password[j]<'0' or password[j]>'9')):
            upper_count+=1
            
        if(password[j]==password[j].lower() and (password[j]<'0' or password[j]>'9')):
            lower_count+=1
            
        if(password[j]>='0' and password[j]<='9'):
            number_count+=1
    if(letter_count>0 and upper_count>0 and lower_count>0 and number_count>0):
        set_of_strong_passwords.add(password)

list_of_strong_passwords = [] # :)

for i in set_of_strong_passwords:
    list_of_strong_passwords.append(i)
print(len(list_of_strong_passwords)-1) #Because we have ' '(space) in our set
list_of_strong_passwords.sort()
for i in range(len(list_of_strong_passwords)):
    if i>0:
        print(list_of_strong_passwords[i])
def rev(str):
    len2 = len(str)
    str2 =""
    for i in range(len(str)):
        str2+=str[len2-1]
        len2-=1
    print(str2)
str = input()
rev(str)
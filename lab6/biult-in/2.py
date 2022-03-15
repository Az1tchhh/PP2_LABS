def LowerUpper(str):
    Ut=0
    Lt=0
    for i in range(len(str)):
        
        if str[i].islower():
            Lt+=1
        elif str[i].isupper():
            Ut+=1
    return Ut,Lt
print(LowerUpper("Azamat Bazarbai"))
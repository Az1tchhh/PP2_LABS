def filter_prime(str):
    a = str.split()
    primes_list = []
    for i in range(len(a)):
        n=2
        cnt=1
        while(n<int(a[i])):
            if(int(a[i])%n==0):
                cnt=0
                break
            n+=1
        if cnt==1:
            primes_list.append(a[i])  
    for i in primes_list:
        print(*i)
str = input()
filter_prime(str)
def is_prime(myNumber):
    for i in range(2,myNumber):
        if(myNumber%i==0):
            return 0
        
    return 1
numbers = str(input())
list_of_numbers = numbers.split()
for i in range(len(list_of_numbers)):
    firstNumber=int(list_of_numbers[0])
    secondNumber=int(list_of_numbers[1])
if(firstNumber<500 and is_prime(firstNumber)==1 and secondNumber%2==0):
    print("Good job!")
else:
    print("Try next time!")
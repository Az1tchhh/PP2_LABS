import random
print("Hello! What is your name?")
name = input()
print("Well, {0}, I am thinking of a number between 1 and 20.".format(name))
guess_number = random.randint(1, 20)
print("Take a guess.")
cnt=0
number = int(input())
cnt+=1
if(number==guess_number):
    print("Good job, {0} You guessed my number in {1} guesses!".format(name,cnt))
else:
    while(number!=guess_number):
        
        if(number < guess_number):
            print("Your guess is too low.")
        elif(number > guess_number):
            print("Your guess is too big.")
        print("Take a guess.")
        number = int(input())
        cnt+=1
        if(number==guess_number):
            print("Good job, {0} You guessed my number in {1} guesses!".format(name,cnt))
            break
    

import random
print("GUESS THE GAME")
print("What's your name?")

#name input from user
my_name=input()

print("Hello!",my_name,"welcome to this game!!")
print("Only 6 attempts to guess the number is allowed")

#no.of attempts done by user
attempts=0

print("I will guess number from 1-60")

number=random.randint(1,60)

while (attempts<=6):
    print("Make a guess")

    #number input from user
    guess=int(input())

    #incrementing no.of attempts
    attempts=attempts+1

    a=str(attempts)

    if(guess<number):
        print("Your guess is too small")

    elif(guess>number):
        print("Your guess is too big")

    elif(guess==number):
       break
        
if(guess==number):
    print("Great work!! :)")
    print("You guessed the number in",a,"attempts")

if(guess!=number):
    print("Sorry you lost! :(")
    print("My number was",number)

    


        
    
    

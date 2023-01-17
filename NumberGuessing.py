import random 

secretNumber=random.randint(1,20)

print('You have 5 tries to guess the secret number between 1 and 20. Good Luck!')

for guessesTaken in range(1,6):
    
    guess=int(input())

    if guess<secretNumber:
        print('Too low. Go higher.')
    elif guess>secretNumber:
        print('Too high. Go lower.')
    else:
        break

if guess==secretNumber:
    print('Nice! You got it in ' + str(guessesTaken)+' tries!')
else:
    print('Sorry. You ran out of tries. The number was ' + str(secretNumber))                
    
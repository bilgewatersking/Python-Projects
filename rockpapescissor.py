import random,sys

wins=0
losses=0
ties=0

while True: #main game loop
    print('%s wins ,%slosses ,%sties'%(wins,losses,ties))
    while True: #player input loop
        print('Make your move or press q to quit. r for rock. p for paper. s for scissor.')
        player=input()
        if player=='q':
            sys.exit()
        if player=='r'or player=='p'or player=='s':
            break
        print('Invalid response. Type p,s or r to play.')    

    if player=='r':
        print('ROCK versus....')
    elif player=='s':
        print('SCISSAR versus....')
    elif player=='p':
        print('PAPAR versus....')

    computer=random.randint(1,3)

    if computer==1:
        computer='r'
        print('ROCK')
    elif computer==2:
        computer='s'
        print('SCISSAR')
    elif computer==3:
        computer='p'
        print('PAPAR')

    if player==computer:
        print('Its a tie!')
        ties=ties + 1

    elif player=='r' and computer=='p':
        print('You lost to an AI.')
        losses=losses + 1
        #losses+=1 abu's fun fact shortcut
    elif player=='r' and computer=='s':
        print('You win!')
        wins+=1
    elif player=='p' and computer=='s':
        print('You lost to an AI.')
        losses+=1
    elif player=='p' and computer=='r':
        print('ggiziai')
        wins+=1
    elif player=='s' and computer=='r':
        print('You lost to an AI!')
        losses+=1
    elif player=='s' and computer=='p':
        print('AI game izi asf.')
        wins+=1                   
                        
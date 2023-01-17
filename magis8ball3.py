#import libraries
import sys,random
# Define magis list

name=input('What is your name? ')
    
quit=['q','Q','quit','Quit']
play=['play','P','Play','p']    
#Create magis function
def magis8ball():
    #Get a random index for our list 
    #randomnumber=random.randint(0,(len(magislist)-1))
    #Access random number in magislist
    return magislist[random.randint(0,(len(magislist)-1))]
    # return magislist[22]
# Create loop
while True:
    # Welcome message. Choose to play or quit
    print(f'Welcome to Magic 8 ball, {name}. To play | {play} To quit | {quit}')
    #Asking user for input
    player=input()
    #If user input is to quit
    if player in quit:
        print(f'Thank you, {name} for playing.')
        sys.exit()
    #If user input  is to play
    elif player in play:
    #User asks question 
        print('Ask a question to find your density. ')
        playerQuestion=str(input())
        magislist=['Definitely my word is....yes',
            'Wink wink',
            'No never',
            'InshaAllah... SIUUUUUU',
            f'I dont know, {name}. You will have to ask Osama',
            'Maybe after an ARAM game you will find the answer you seek',
            'Why you are asking me men mad fellow.',
            'Swipe right on Nicky. You will have everything you could ever ask for.',
            'Are you actually putting your faith in a black ball? Bruh..',
            'If the shoe fits',
            'Does the sun rise in the morning and set in the evening?',
            'Yes because E=mass x acceleration',
            'No because Capitalism is a social construct created by the government in order to marginalize smaller businesses on the pretext of industrialization.',
            'This numba 1 bullshit bratha.',
            'There is a 50 percent chance of you being happy with the answer. So yes go for it',
            'YOLO. Just do it.',
            'Nanananananana BATMAAAAAN',
            'Think about what you in 5 years would do. There is your answer.',
            'Kinda capped man ngl.',
            f'As {name} said, Inevitability is the pillar of success',
            f'As {name} said, yes and no is also an answer',
            f'Look at {name}\'s transformational weight loss. There is always hope.',
            f'I would ask you the same thing, {name}. {playerQuestion}']
        #Answer is given
        #Get a random index for our list 
        #randomnumber=random.randint(0,(len(magislist)-1))
        #Magis8ball is the function which gets values from magic
        print(magis8ball())
    #End the loop if player quits. If invalid response, show error message.
    else:
        print('Invalid response.Please read instructions properly as its in plain English.')





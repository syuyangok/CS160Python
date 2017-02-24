'''
Design a hangman game.
Random select a word from a list. And ask user to guess the word with limit chances.

'''
import random

def openDatafile():
    fileName = 'word.txt'
    dataFile = open(fileName, 'r')
    theList=[]
    for value in dataFile:
        value = value.rstrip()
        theList.append(value)
    dataFile.close()
    return theList

wordList = openDatafile()

nextGame = 'y'
while nextGame == 'y':  
    level = int(input('Enter a difficulty level (1 for tough; 2 for medium; 3 for easy):'))
    if level ==3:
        maxCount = 9
        print('You selected the easy level. You will be allowed up to 9 misses.')
    elif level ==2:
        maxCount = 7
        print('You selected the medium level. You will be allowed up to 7 misses.')
    elif level ==1:
        maxCount = 5
        print('You selected the tough level. You will be allowed up to 5 misses.')

    print()
    n = random.randint(0,19)
    word = wordList[n]
    targetList=[]
    starList =[]
    for char in word:
        targetList.append(char)
        starList.append('*')

    
    print('The word is', len(word)*'*')


    count = 0
    missGuess = []
    

  
    while  count < maxCount and starList != targetList:
        print()
        if count==0:        
            print('Incorrect letters:')
            guess = str(input('Your guess? '))
            guess = guess.lower()
            print()
        else:
            print('Incorrect letters:',end='')
            for value in missGuess:
                print(value,'', end='')
            print()
            guess = str(input('Next guess? '))
            guess = guess.lower()
            print()
        
        if guess in targetList:
            for index in range(len(targetList)):
                if guess == targetList[index]:
                    starList[index] = guess
            if starList == targetList:
                print(word)
                print('You got it - the word is', word)
            else:
                print(guess, 'is in the word.')         
                for value in starList:
                    print(value, end='')
                print()
                print('You have', count, 'incorrect guess(es)')
            
        else:
            count = count + 1
            missGuess.append(guess)
            print(guess, 'is not in the word.')
            if count == maxCount:
                for value in starList:
                    print(value, end='')
                print()
                print('You have', count, 'incorrect guess(es) - you lost this game')
            else:
                for value in starList:
                    print(value, end='')
                print()                
                print('You have', count, 'incorrect guess(es)')
    
    print()
    nextGame = input('Would you like to play another game ? Y for yes Or anything else to quit:')
    nextGame = nextGame.lower()
    print()


































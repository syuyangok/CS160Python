'''
Ask user for golf scores and store to file;
'''


def numberOfStroke(theList):
    total = 0
    for value in theList:
        value = int(value)
        total = value +total
    return total
    

# Ask user for name and scores and write to list
name = str(input('Enter your name: '))
score = int(input('Enter the scores(Between 1 and 10): '))
scoreList = []
count = 1
 
while count <10:
    if score >=1 and score <=10:
        count = count+1
        scoreList.append (score)
        if count !=10:            
            score = int(input('Enter the scores(Between 1 and 10): '))
    else:
        score = int(input('Wrong Enter. Please enter the scores(Between 1 and 10): '))

print()



# Compare user socres with par
total = numberOfStroke(scoreList)
if total < 36:
    vsPar = 36 - total
    print('Your score is :', total, '; Below the par(36) of',vsPar, 'for the round.')
elif total == 36:
    vsPar = 36 - total
    print('Your score is :', total, '; It is excalty the par(36) for the round.')
else:
    vsPar = total -36
    print('Your score is :', total, '; Above the par(36) of',vsPar, 'for the round.')
print()
    

# Write score to the file  

fileName = str(input('Enter a data file name: '))
dataFile = open (fileName, 'w')

dataFile.write('Score for '+ name +'\n')
dataFile.write('Hole Score' +'\n')

n=0
for value in scoreList:
    n=n+1
    dataFile.write(format(n, '4d')+format(value, '6d')+'\n')
    
dataFile.write('\n')
dataFile.write('Total for the round:'+ format(total, '4d')  +'\n')

dataFile.close()




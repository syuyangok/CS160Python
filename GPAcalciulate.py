'''
Calculate GPA for classes.
'''

gradePoints ={'A':4, 'B':3, 'C':2, 'D':1, 'F':0}

'''
 Function addClass:  Add classname to dictionary of classes
'''
def addClass(classes, className, grade, credits):
    if takenClass(classes, className):
        return False
    else:
        #classes[className] = [grade, credits]
        classes[className] = {}
        classes[className]['grade'] = grade
        classes[className]['credits'] = credits
        return True

'''
Function importReportCard: # Import datafile to dictionary of classes
'''
def importReportCard(classes, filename='reportcard.txt'):
    dataFile = open(filename, 'r')
    for line in dataFile:
        line = line.strip()
        (className, grade, credits) = line.split(':')
        credits= int(credits)
        addClass(classes, className, grade, credits)
    dataFile.close()

'''
 Function dropClass:  Rmove a class from dictionary of classes
'''
def dropClass(classes, className):
    if takenClass(classes, className):
        #classes.pop(className)
        del classes[className]
        return True
    else:
        return False


'''
 Function attemptedCredits:  Return the number of attempted credits.
'''
def attemptedCredits(classes):
    aCredits = 0
    for value in classes:
        aCredits += classes[value]['credits']
    return aCredits

'''
 Function passedCredits:  Return the number of passed credits(A-D).
'''
def passedCredits(classes):
    pCredits = 0
    for value in classes:
        if classes[value]['grade'] != 'F':
            pCredits += classes[value]['credits']
    return pCredits

'''
 Function takenClass:  If a class is in dictionary of classes, return True.
'''
def takenClass(classes, className):
    if className in classes:
        return True
    else:
        return False

'''
 Function getGPA:  Return the number of GPA.
'''
def getGPA(classes):
    totalPoints = 0
    for value in classes:
        points = classes[value]['grade']
        totalPoints += classes[value]['credits'] * gradePoints[points]
    gpa = totalPoints/attemptedCredits(classes) # if not include 'F', use next command.
    #gpa = totalPoints/passedCredits(classes)
    return gpa

'''
 Function updateClass:  Update a class with new grade
'''
def updateClass(classes, className, grade):
    if takenClass(classes, className):
        classes[className]['grade'] = grade
        return True
    else:
        return False

'''
 Function printClass:  print classes in a neat talble.
'''
def printClass(classes):
    print(format('   Class', '15s')+format('Grade', '10s')+format('Credits', '10s'))
    n=0
    sortedClass = list(classes.keys())
    sortedClass.sort()

    for value in sortedClass:
        n += 1
        print (str(n)+'. '+format((value+':'), '14s')+format(classes[value]['grade'], '5s')+ format(classes[value]['credits'], '10d'))

    gpa= float(getGPA(classes))
    print()
    print ('Overall GPA:', format(gpa, '5.3f'))

'''
Test above Functions.
'''
def main():
    classes = {}
    addClass(classes, 'CS160', 'A', 4)#test addClass and takenClass
    addClass(classes, 'CS161', 'A', 3)
    addClass(classes, 'Math201', 'F', 3)
    importReportCard(classes, filename='reportcard.txt' ) #test importRportCard
    print(classes)
    print()

    print('After drop classes CS161:')
    dropClass(classes, 'CS161')#test dropClass and takenClass
    print(classes)
    print()

    aC = attemptedCredits(classes)#test attemptedCredits
    print('Attempted Credits:', aC)
    print()

    pC = passedCredits(classes)#test passedCredits
    print('Passed Credits:', pC)
    print()



    print('After update classes Math201:')
    updateClass(classes, 'Math201', 'A')#Test Updateclass and takenClass
    print(classes)
    print()

    printClass(classes)# Test printClass and getGPA


main()

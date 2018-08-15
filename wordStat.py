# read a english file and calucualte word stat counts
# draw five most words bar graph.

#calculate each words of line by countDict
def processLine(line, countDict):
    # replace punctuation with space
    line = replacePunctuations(line)

    #split line to list 
    words = line.split()
    for item in words:
        if item in countDict:
            countDict[item] +=1
        else:
            countDict[item] =1 # add new word to dict
    
#replace punctuation with space
def replacePunctuations(line):
    for ch in line:
        if ch in "@#$&*!+=-_^%/?,<.>[]{}'":
            line = line.replace(ch, " ")
    return line


def main():
    filename = input("enter a file name:")
    infile = open(filename, "r")

    countDict = {}
    for line in infile:
        processLine(line.lower(), countDict)
    
    pairs = list(countDict.items())
    #switch data position and sort data
    items = [[x,y] for (y,x) in pairs]
    items.sort(reverse=True)

    for i in range(5):
        print(items[i][1] + "\t" + str(items[i][0]))


main()
    

# import file to draw with turtle

import turtle

turtle.title('File data draw')
turtle.setup(800, 600, 0, 0)

#set pen
pen = turtle.Turtle()
pen.color("red")
pen.width(5)
pen.shape("turtle")
pen.speed(2)

#read file
result = []
file = open("starData.txt", "r")
for line in file:
    result.append(list(map(float, line.split(','))))
#print(result)

#draw
pen.up()
pen.goto(-150,0)
pen.down()
for i in range(len(result)):
    pen.color(result[i][3], result[i][4], result[i][5])
    pen.fd(result[i][0])
    if result[i][1]:
        pen.rt(result[i][2]) # 1 turn right
    else:
        pen.lt(result[i][2]) # 0 turn left
#Back to zero        
pen.up()
pen.goto(0,0)


file.close()

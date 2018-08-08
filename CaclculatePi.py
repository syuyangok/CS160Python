# calculate pi by Monte Carlo
from random import random
from math import sqrt
from time import clock

n = 12000 # max number of dots, also the area of square
hits = 0 # if inside circle/4
clock()

for i in range(1, n):
    # got random position of dot
    x = random();
    y = random();

    # got distance from center to dot
    dist = sqrt(x**2 + y**2)
    if dist <= 1.0:
        hits = hits +1

pi = 4 * (hits/n)
print("Pi is: %s" % pi)
print("Program running time is: %-5.5ss" % clock())

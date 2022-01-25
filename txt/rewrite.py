import os

with open("bestGabe.txt")as f:
    x = 0
    f2 = open('gabe2.txt','w')
    gabeValue = []
    for line in f:
        f2.write('\"' + line.rstrip() + '\", ')

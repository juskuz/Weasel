#! usr/bin/env python

import random 

alfabet1='ABCDEFGHIJKLMNOPQRSTUVWXYZ '
wzorzec='METHINKS IT IS LIKE A WEASEL'

zbior=[]
for r in range(100):
    ciag=''
    for x in range(28):
        litera=random.choice(alfabet1)
        ciag=ciag+litera
    zbior.append(ciag)

i=0
while(1):
    i=i+1
    punkty=0
    for wyraz in zbior:
        points=0
        for znak in range(28):
            if wyraz[znak]==wzorzec[znak]:
                points=points+1
        if points>punkty:
            word=wyraz
            punkty=points
    #print punkty

    if punkty==28:
        print "Dopasowano do wzorca w {} iteracji.".format(i) 
        break
    else:
        zbior=[]
        for w in range(100):
            pozycja=int(random.randint(0,27))
            litera=random.choice(alfabet1)
            word2=word[:pozycja]+litera+word[pozycja+1:]
            zbior.append(word2)

# python program to shuffle a deck of card

#import random 
import itertools,random

deck = list(itertools.product(range(1,14),["heart", "spade","diamond","club"]))

random.shuffle(deck)

#draw five cards

print("you got")
for i in range(5):
    print(deck[i][0], "of",deck[i][1])
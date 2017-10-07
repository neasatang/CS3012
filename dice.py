import random

playing = True;
while playing:
    print("The dice rolled a {i:0}".format(i=random.randrange(1,7)))
    playing = input("Type 'R' to reroll the dice")== 'R' or 'r'

import random
import score_farkel 
reload(score_farkel )
score = score_farkel.score

def roll(n):
    '''Roll n dice
    returns a sorted list of ints
    '''
    dice = []
    for i in range(n):
        die = random.randint(1,6)
        dice.append(die)
    return sorted(dice)
    
def score6(n):
    '''Return a list of n scores from rolling 6 dice
    '''
    import matplotlib.pyplot as plt
    import numpy as np
    scores=[]
    for i in range(n):
        scores.append(score(roll(6))[0])
    fig, ax = plt.subplots(1,1)
    ax.hist(scores, bins=np.arange(-25,3050,50))
    fig.show()
    
    return scores
    #mean 390, median 250
    
def score_to_fail():
    score = 0
    new_score = -1
    dice_left = 6
    while new_score != 0:
        if dice_left==0:
            dice_left=6
        a = roll(dice_left)
        print a,
        try: 
            new_score, dice_left = score(a)
        except:
            print score
            print a
            print score(a)
        score += new_score
        print new_score, score
    return score
    
def space(n):
    '''return a list of all possible lists of n ints 1-6 
    '''
    fullspace =[]
    item=[]
    for i in range(n):
        pass #This one is challenging!
        
print score
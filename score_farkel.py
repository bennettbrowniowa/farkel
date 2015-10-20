def score(dice):
    '''return additional_score, dice_unscored
    additional_score is an int
    n_dice_unscored is an int
    '''
    additional_score, unscored_dice = six_of_a_kind(dice)
    
    more_score, unscored_dice = five_of_a_kind(unscored_dice)
    additional_score += more_score
    
    more_score, unscored_dice = four_of_a_kind(unscored_dice)
    additional_score += more_score
    
    more_score, unscored_dice = straight(unscored_dice)
    additional_score += more_score
    
    more_score, unscored_dice = three_pairs(unscored_dice)
    additional_score += more_score
    
    more_score, unscored_dice = two_triplets(unscored_dice)
    additional_score += more_score
    
    more_score, unscored_dice = triplet(unscored_dice)
    additional_score += more_score
    
    more_score, unscored_dice = ones_fives(unscored_dice)
    additional_score += more_score
    
    return additional_score, len(unscored_dice)
    
def score_test():
    tests = [([1,1,1,1,1,1],(3000,0)), #six of a kind
             ([1,1,1,1,1,2],(2000,1)), #5 of as kind, stray
             ([2,3,3,3,3,3],(2000,1)), #5 of as kind, stray
             ([1,1,1,1,2,3],(1000,2)), #4 of as kind, stray
             ([2,3,3,3,3,4],(1000,2)), #4 of as kind, stray
             ([2,3,4,4,4,4],(1000,2)), #4 of as kind, stray
             ([2,2,2,2,3,3],(1500,0)), #4 of a kind, pair
             ([2,2,3,3,3,3],(1500,0)), #4 of a kind, pair
             ([1,2,3,4,5,6],(1500,0)), #straight
             ([1,1,2,2,3,3],(1500,0)), #3 pair
             ([1,1,1,2,2,2],(2500,0)), #2 triplets
             ([1,1,1,2,3,4],(300,3)),  #triplet
             ([2,2,2,3,4,6],(200,3)),  #triplet
             ([2,3,3,3,4,6],(300,3)),  #triplet
             ([2,3,4,4,4,6],(400,3)),  #triplet
             ([2,3,4,5,5,5],(500,3)),  #triplet
             ([2,3,4,6,6,6],(600,3)),  #triplet
             ([2,3,4,5,6,6],(50,5)),  #singles
             ([1,3,4,4,6,6],(100,5)),  #singles
             ([1,3,4,5,6,6],(150,4)),  #singles
             ([1,3,4,6,6,6],(700,2)),  #single, triple
             ([1, 2, 2, 2, 5, 5], (400,0)),

             ([1,1,3,4,5,5],(300,2))  #single, triple
            ]
    for test in tests:
        dice, right = test
        returned = score(dice[:])
        if returned != right:
            print("dice("+str(dice) + ") returned " + str(returned) + "\n\tand should have returned " + str(right))

def six_of_a_kind(dice):
    '''dice is a sorted list of int
    return points, remaining_dice where
    points is an int
    remaining_dice is a list of int
    '''
    score, newdice = 0, dice
    if dice == dice[0:1] *6:
        score, newdice = 3000, []
    return score, newdice
        
def five_of_a_kind(dice):
    '''dice is a sorted list of int NOT containing 6 of a kind
    return points, remaining_dice where
    points is an int
    remaining_dice is a list of int
    ''' 
    score, newdice = 0, dice
    if len(dice)>=5:
        if dice[:5] == dice[0:1]*5:
            score, newdice = 2000, dice[5:]
        elif dice[1:]==dice[1:2]*5:
            score, newdice = 2000, dice[0:1]
    return score, newdice
            
def four_of_a_kind(dice):
    '''dice is a sorted list of int NOT containing 5 or 6 of a kind
    return points, remaining_dice where
    points is an int
    remaining_dice is a list of int
    ''' 
    score = 0
    if len(dice)>=4:
        for start in range(3):
            if dice[start:start+4] == dice[start:start+1]*4:
                score = 1000
                for i in range(4):
                    dice.pop(start)
                break
    if score==1000 and len(dice)==2 and dice[0]==dice[1]:
        score, dice = 1500, []
    return score, dice

def straight(dice):
    if dice == [1,2,3,4,5,6]:
        score, dice = 1500, []
    else:
        score = 0
    return score, dice
    
def three_pairs(dice):
    score = 0
    if len(dice)==6 and dice[0]==dice[1] and dice[2]==dice[3] and dice[4]==dice[5]:
        score, dice = 1500, []
    return score, dice
    
def two_triplets(dice):
    score = 0
    if len(dice)==6 and dice[0:3]==dice[0:1]*3 and dice[3:6]==dice[3:4]*3:
        score, dice = 2500, []
    return score, dice
    
def triplet(dice):
    score =0
    for start in range(len(dice)-2):
        if dice[start:start+3]==dice[start:start+1]*3:
            score = 100*dice[start]
            if score==100:
                score=300
            for i in range(3):
                dice.pop(start)
            break
    return score, dice
    
def ones_fives(dice):
    score = 0
    for i in range(len(dice)-1,-1,-1):
        if dice[i]==1:
            score +=100
            dice.pop(i)
        elif dice[i]==5:
            score +=50
            dice.pop(i)    
    return score, dice
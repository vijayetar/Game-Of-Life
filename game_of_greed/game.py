import random
from collections import Counter

# player one starts game logic
# rolls 6 dice
## generates random numbers between 1-6
# logic has to check if all six are scoring dice, then it is all banked
# player can keep playing if all six are scoring dice
# shelves some of the dice
# shelf scores shows the score of dice in shelf
# player has option to bank all the dice rolled and complete turn or continue playing
# player rolls again with remaining dice
# restart from line 6

class GameLogic:
  def __init__(self, name):
    self.name = name

  def calculate_score(self, dice_rolled):
    '''Roll's score'''
    score = 0
    if len(dice_rolled) == 6 and (straight(dice_rolled) or three_pairs(dice_rolled)):
      return 1500
    score = three_or_more(dice_rolled,score)
    score = ones_or_fives(dice_rolled, score)
    return score

  @staticmethod
  def roll_dice(n):
    '''Input n is integer between 1-6 and output is tuple of n random numbers'''
    dice_rolled= [random.randint(1,6) for i in range(n)]
    return dice_rolled


class Banker(GameLogic):  # Banker now a subclass of GameLogic
  def __init__(self):
    pass

  # store unbanked points
  def shelf(self):
    '''Temporarily store score in the shelf before banking '''
    # return temporarily stored points
    pass

  def bank(self):
    '''Add score stored in shelf to the total score and reset shelf as 0 '''
    # return total scored
    pass
  
  def clear_shelf(self):
    '''Clears shelf and removes all unbanked points'''
    pass

def straight(dice_rolled):
  ''' function checks if 1-6 straight is rolled '''
  reference_list = [1,2,3,4,5,6]
  if len(dice_rolled)==6:
    dice_rolled.sort()
    if reference_list == dice_rolled:
      return True
      
def three_pairs(dice_rolled):   
  ''' function checks if 3 pairs of numbers are rolled ''' 
  ctr = Counter(dice_rolled)
  if len(ctr) == 3:
    for num in ctr:
      if ctr[num]!=2:
        return False
    return True

def three_or_more(dice_rolled,value):
  ctr = Counter(dice_rolled)
  for num in ctr:
    if ctr[num] > 2:
      if num == 1:
        value += 1000 * (ctr[num] - 2)
      else:
        value += num * 100 * (ctr[num] - 2)
  return value

def ones_or_fives(dice_rolled, value):
  ctr = Counter(dice_rolled)
  for num in ctr:
    if num == 1 and ctr[num] < 3:
      value += 100 * ctr[num]
    elif num == 5 and ctr[num] < 3:
      value += 50 * ctr[num]
  return value

if __name__ == "__main__":
    thomas = GameLogic("Thomas")
    print(thomas.name)
    print(thomas.calculate_score([6,3,4,5,2,1]))
    print(thomas.calculate_score([6,3,4,5,2,1]))
    print(thomas.calculate_score([4,4,5,5,3,3]))
    print(thomas.calculate_score([4,4,4,5,3,3]))
    print(thomas.calculate_score([4,4,4,3]))
    print(thomas.calculate_score([1,1,5,3]))
    print(thomas.calculate_score([4,4,4,4]))
    print(thomas.calculate_score([1,1,1,1]))
    # print(thomas.calculate_score([1,1,1,1,1,1]))
    # print(thomas.calculate_score([6,6,6,6,6,6]))
    print(thomas.calculate_score([5,5,1,1,3]))




    

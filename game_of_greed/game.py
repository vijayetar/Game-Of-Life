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
    score = three_or_more(dice_rolled, score)
    score = ones_or_fives(dice_rolled, score)
    return score

  @staticmethod
  def roll_dice(n):
    '''Input n is integer between 1-6 and output is tuple of n random numbers'''
    dice_rolled = tuple(random.randint(1,6) for i in range(n))
    return dice_rolled

class Banker(GameLogic):  # Banker now a subclass of GameLogic
  def __init__(self,name):
    self.name = name
    self.shelf = 0
    self.banked = 0

  # store unbanked points
  def shelf(self, dice_rolled):
    '''Temporarily store score in the shelf before banking '''
    self.shelf += self.calculate_score(dice_rolled)
    return self.shelf

  def bank(self):
    '''Add score stored in shelf to the banked score and reset shelf as 0 '''
    print("this is shelved", self.shelf)
    print("this is banked score", self.banked)
    self.banked += shelved_score
    self.clear_shelf()
    return self.banked
  
  def clear_shelf(self):
    '''Clears shelf and removes all unbanked points'''
    print("Calling clear shelf")
    self.shelf = 0
    return self.shelf

# def initial_roll(dice_rolled):
#   # if (straight(dice_rolled) or three_pairs(dice_rolled)):
#   #   return 1500
#   # return 0

def straight(dice_rolled):
  ''' for 6 dice rolled function checks if 1-6 straight is rolled '''
  reference_list = [1,2,3,4,5,6]
  if len(dice_rolled)==6:
    dice_rolled.sort()
    if reference_list == dice_rolled:
      return True
  return False
      
def three_pairs(dice_rolled):   
  ''' for 6 dice rolled, this function checks if 3 pairs of numbers are rolled ''' 
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
    thomas = Banker("Thomas")
    print(thomas.name)
    shelved_score = 2000
    # shelved_score = thomas.shelf([1],0)
    # print(shelved_score)
    # shelved_score = thomas.shelf([1],shelved_score)
    # print(shelved_score)
    # shelved_score= thomas.shelf([1,1,1,1],shelved_score)
    # print(shelved_score)
    print(thomas.bank(shelved_score))
    shelved_score=1000
    print(thomas.bank(shelved_score))



    # # print(thomas.calculate_score([1,1,1,1,1,1]))
    # # print(thomas.calculate_score([6,6,6,6,6,6]))
    # print(thomas.calculate_score([5,5,1,1,3]))




    

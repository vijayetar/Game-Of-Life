import random
from collections import Counter

class GameLogic:
  def __init__(self, name):
    self.name = name

  def calculate_score(self, tuple):
    '''Roll's score'''
    pass

  @staticmethod
  def roll_dice(n):
    '''Input n is integer between 1-6 and output is tuple of n random numbers'''
    dice_rolled= [random.randint(1,6) for i in range(n)]
    return dice_rolled


class Banker:
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


if __name__ == "__main__":
    thomas = GameLogic("Thomas")
    print(thomas.name)
    print(thomas.roll_dice(2))
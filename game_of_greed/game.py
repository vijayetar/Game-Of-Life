import random
from collections import Counter

class GameLogic :
  def __init__(self):
    pass

  def calculate_score(self,(tuple),):
    '''Roll's score'''
    pass

  @staticmethod
  def roll_dice(n):
    '''Input n is integer between 1-6 and output is tuple of n random numbers'''
    # for i in range(n):
    #   print(random.randint(1,6))


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



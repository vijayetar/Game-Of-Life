import random
import sys
from collections import Counter

class Game:

  def __init__(self, roller=None): #roller = dice roll function
    self.roller = roller or GameLogic.roll_dice
    self.round = 0
    self.dice = 6
    self.max_rounds = 20

  def play(self):
    print("Welcome to Game of Greed")
    response = input("Wanna play?")
    if response == "y":
      self.game_round()
    elif response == "n":
      print("OK. Maybe another time")
    else:
      print("Invalid response, try again.")
      self.play()

  def game_round(self):
    self.round += 1
    if self.round > self.max_rounds:
      self.exit()
    print(f"Starting round {self.round}")
    print(f"Rolling {self.dice} dice...")
    dice_roll = self.roller(self.dice)
    self.zilch(dice_roll)
    self.shelve_or_quit(dice_roll)

  def shelve_or_quit(self, dice_roll=None):
    
    str_roll = ""
    for num in dice_roll:
      str_roll += str(num) + ","
    print(str_roll[:-1])
    response = input("Enter dice to keep (no spaces), or (q)uit: ")
    if response == "q":
      self.exit()
    elif isinstance(int(response), int):
      self.check_dice(response, dice_roll)  

  def check_dice(self, response, dice_roll):
    dice_to_be_shelved = []
    dice_to_be_shelved = [int(i) for i in response]
    dice_rolled = list(dice_roll)
    for num in dice_to_be_shelved:
      if num in dice_rolled:
        dice_rolled.remove(num)
      else:
        print("Cheater!!! Or possibly made a typo...")
        self.shelve_or_quit(dice_roll)
    self.shelf(dice_to_be_shelved)
    self.dice = self.dice-len(dice_to_be_shelved)
    print(f"You have {self.shelved} unbanked points and {self.dice} dice remaining")
    if self.dice == 0:
      self.dice = 6
      
    self.roll_bank_quit()

  def roll_bank_quit(self):
    
    response = input("(r)oll again, (b)ank your points or (q)uit ")
    if response == "r":
      print(f'Rolling {self.dice} dice...')
      dice_roll = self.roller(self.dice)
      self.zilch(dice_roll)
      self.shelve_or_quit(dice_roll)
    elif response == "b":
      self.bank()
      
      self.dice = 6
      self.game_round()
    elif response == "q":
      self.exit()
    else:
      print("Invalid input.")
      self.roll_bank_quit

  def exit(self):
    print(f"Total score is {self.banked} points")
    print(f"Thanks for playing. You earned {self.banked} points")
    sys.exit(0)

class GameLogic():

  def __init__(self, roller=None):
    super().__init__(roller=roller)
  
  @staticmethod
  def calculate_score(dice_rolled):
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
  
  @staticmethod
  def get_scorers(dice_rolled):
    total_score = GameLogic.calculate_score(dice_rolled)
    print("this is total score in get_scorers", total_score)
    returned_dice = ''
    # dice_rolled = list(dice_roll)
    #iterate over dice_rolled list and determine which of the numbers is scoring dice
    print(f'dice_rolled: {dice_rolled}')
    for index, num in enumerate(dice_rolled):
      temporary_roll = list(dice_rolled)
      temporary_roll.pop(index)
      if not total_score == GameLogic.calculate_score(temporary_roll):
        returned_dice += str(num)
    return returned_dice
    # return the list of scoring dice

class Banker(Game):  # Banker now a subclass of GameLogic
  def __init__(self, roller=None):
    super().__init__(roller=roller)
    self.shelved = 0
    self.banked = 0

  # store unbanked points
  def shelf(self, dice_rolled):
    '''Temporarily store score in the shelf before banking '''
    self.shelved += GameLogic.calculate_score(dice_rolled)
    return self.shelved

  def bank(self):
    '''Add score stored in shelf to the banked score and reset shelf as 0 '''
    self.banked += self.shelved
    print(f'You banked {self.shelved} points in round {self.round}')
    print(f'Total score is {self.banked} points')
    self.clear_shelf()
    return self.banked
  
  def clear_shelf(self):
    '''Clears shelf and removes all unbanked points'''
    self.shelved = 0
    return self.shelved

  def zilch(self, dice_rolled):
    if GameLogic.calculate_score(dice_rolled) == 0:
      str_roll = ""
      for num in dice_rolled:
        str_roll += str(num) + ","
      print(str_roll[:-1]) 
      self.shelved = 0
      print('Ya busted!')
      print(f"You banked {self.shelved} points in round {self.round}")
      print(f'Total score is {self.banked} points')
      self.dice = 6
      self.game_round()


def straight(dice_rolled):
  ''' for 6 dice rolled function checks if 1-6 straight is rolled '''
  reference_list = [1,2,3,4,5,6]
  dice_rolled = list(dice_rolled)
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
    # thomas = Banker("Thomas")
    # print(thomas.name)
    # thomas.shelf = 2000
    # # shelved_score = thomas.shelf([1],0)
    # # print(shelved_score)
    # # shelved_score = thomas.shelf([1],shelved_score)
    # # print(shelved_score)
    # # shelved_score= thomas.shelf([1,1,1,1],shelved_score)
    # # print(shelved_score)
    # print(thomas.bank())
    # thomas.shelf=1000
    # print(thomas.bank())
  thomas=Banker()
  thomas.play()



    # # print(thomas.calculate_score([1,1,1,1,1,1]))
    # # print(thomas.calculate_score([6,6,6,6,6,6]))
    # print(thomas.calculate_score([5,5,1,1,3]))




    

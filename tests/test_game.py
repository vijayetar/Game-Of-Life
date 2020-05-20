from game_of_greed.game import (
  Game,
  GameLogic, 
  straight, 
  three_pairs,
  three_or_more,
  ones_or_fives,
  Banker,
)
from collections import Counter
import sys

from tests.flo import Flo



def test_gamelogic_exists():
  assert GameLogic

def test_Banker_exists():
  assert Banker

def test_Game_exists():
  assert Game

def test_Flo_exists():
  assert Flo


def test_gamelogic_rolldice_six():
  test = GameLogic("test")
  tuple_created = test.roll_dice(6)
  actual = len(tuple_created)
  expected = 6
  assert actual == expected

def test_gamelogic_rolldice_onetosix():
  test=GameLogic("test")
  tuple_created = test.roll_dice(10)
  actual = True
  for i in tuple_created:
    if i<1 or i>6:
      actual = False
  expected = True
  assert actual == expected

def test_gamelogic_straight_true():
  test=GameLogic("test")
  list_created = [6,4,3,5,2,1]
  actual = test.calculate_score(list_created)
  expected = 1500
  assert actual == expected

def test_gamelogic_three_pairs_true():
  test=GameLogic("test")
  list_created = [5,4,3,5,4,3]
  actual = test.calculate_score(list_created)
  expected = 1500
  assert actual == expected

def test_gamelogic_ones_or_fives():
  test=GameLogic("test")
  list_created = [6,4,3,5,1,1]
  actual = test.calculate_score(list_created)
  expected = 250
  assert actual == expected

def test_gamelogic_three_or_more_1():
  test=GameLogic("test")
  list_created = [1,1,1,1,1,1]
  actual = test.calculate_score(list_created)
  expected = 4000
  assert actual == expected

def test_gamelogic_three_or_more_2():
  test=GameLogic("test")
  list_created = [4,4,4,4,5,6]
  actual = test.calculate_score(list_created)
  expected = 850
  assert actual == expected

def test_gamelogic_zilch_roll():
  test=GameLogic("test")
  list_created = [3,2,2,4,6,6]
  actual = test.calculate_score(list_created)
  expected = 0
  assert actual == expected
  
def test_gamelogic_three_or_more_3():
  test=GameLogic("test")
  list_created = [3,3,3,4,4,4]
  actual = test.calculate_score(list_created)
  expected = 700
  assert actual == expected

def test_gamelogic_three_or_more_4():
  test=GameLogic("test")
  list_created = [5,5,5,5,5,3]
  actual = test.calculate_score(list_created)
  expected = 1500
  assert actual == expected

def test_shelf_return():
  test = Banker('test')
  list_created = [1,2,3,4,5,6]
  actual = test.shelf(list_created)
  expected = 1500
  assert actual == expected

def test_shelf_stored():
  test = Banker('test')
  list_created = [6,5,4,3,2,1]
  test.shelf(list_created)
  actual = test.shelved
  expected = 1500
  assert actual == expected

def test_bank_stored():
  test = Banker('test')
  test.banked = 5000
  test.shelved = 2000
  test.bank()
  bank_actual = test.banked
  bank_expected = 7000
  shelf_actual = test.shelved
  shelf_expected = 0
  assert bank_actual == bank_expected and shelf_actual == shelf_expected

def test_bank_returned():
  test = Banker('test')
  test.banked = 2345
  test.shelved = 7143
  actual = test.bank()
  expected = 9488
  assert actual == expected

def test_flo_wanna_play():
  Flo.test('tests/flow/wanna_play.txt')

def test_flo_do_wanna_play_then_quit():
  Flo.test('tests/flow/do_wanna_play_then_quit.txt')

# def test_flo_cheat_and_fix():
#    Flo.test('tests/flow/cheat_and_fix.txt')

# def test_flo_bank_one_roll_then_quit():
#   Flo.test('tests/flow/bank_one_roll_then_quit.txt')

# def test_flo_bank_first_for_two_rounds():
#   Flo.test('tests/flow/bank_first_for_two_rounds.txt')


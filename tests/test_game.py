from game_of_greed.game import (
  GameLogic, 
  straight, 
  three_pairs,
  three_or_more,
  ones_or_fives,
  Banker
)

def test_gamelogic_exists():
  assert GameLogic

def test_Banker_exists():
  assert Banker

def test_gamelogic_rolldice_six():
  test = GameLogic("test")
  list_created = test.roll_dice(6)
  actual = len(list_created)
  expected = 6
  assert actual == expected

def test_gamelogic_rolldice_onetosix():
  test=GameLogic("test")
  list_created = test.roll_dice(10)
  actual = True
  for i in list_created:
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
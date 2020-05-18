from game_of_greed.game import (
  GameLogic, 
  straight, 
  three_pairs,
)

def test_gamelogic_exists():
  assert GameLogic

def test_gamelogic_rolldice_six():
  test = GameLogic("test")
  list_created = test.roll_dice(6)
  actual = len(list_created)
  expected = 6
  assert actual == expected

def test_gamelogic_rolldice_four():
  test = GameLogic("test")
  list_created = test.roll_dice(4)
  actual = len(list_created)
  expected = 4
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

def test_gamelogic_straight_or_pair_false():
  test=GameLogic("test")
  list_created = [6,4,3,5,2,3]
  actual = test.calculate_score(list_created)
  expected = 0
  assert actual == expected
  
def test_gamelogic_pairs_true():
  test=GameLogic("test")
  list_created = [5,4,3,5,4,3]
  actual = test.calculate_score(list_created)
  expected = 1500
  assert actual == expected

def test_gamelogic_straight_or_pair_false():
  test=GameLogic("test")
  list_created = [4,4,4,4,5,6]
  actual = test.calculate_score(list_created)
  expected = 0
  assert actual == expected
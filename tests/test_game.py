from game_of_greed.game import GameLogic

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

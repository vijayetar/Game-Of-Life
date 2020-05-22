  
""""
Create a Game of Greed Player Bots
ONLY use public methods
- Game class constructor and play method
- DO NOT INJECT CUSTOM ROLL FUNCTION
- GameLogic, all methods available
"""
import builtins
import re

from game import Game, GameLogic, Banker

class BasePlayer:
    def __init__(self):
        self.old_print = print
        self.old_input = input
        builtins.print = self._mock_print
        builtins.input = self._mock_input
        self.total_score = 0
        self.dice = 6
        self.unbanked = 0
        self.running_total = 0
        self.ai_name = ''

    def reset(self):
        builtins.print = self.old_print
        builtins.input = self.old_input

    def _mock_print(self, *args, **kwargs):
        self.old_print(*args, **kwargs)

    def _mock_input(self, *args, **kwargs):
        return self.old_input(*args, **kwargs)

    @classmethod
    def play(cls, num_games=1):

        mega_total = 0

        for i in range(num_games):
            player = cls()
            game = Banker()
            try:
                game.play()
            except SystemExit:
                pass
            mega_total += player.total_score
            player.reset()

        print(
            f"{num_games} games (maybe) played by {player.ai_name} with average score of {mega_total // num_games}"
        )

class Naysayer(BasePlayer):
    def _mock_input(self, *args, **kwargs):
        return "n"


class NervousNellie(BasePlayer):
    def __init__(self):
        super().__init__()
        self.roll = None
        self.ai_name = 'Nervous Nellie'

    def _mock_print(self, *args, **kwargs):
        first_arg = args[0]
        first_char = first_arg[0]
        if first_char.isdigit():
            self.roll = tuple(int(char) for char in first_arg.split(","))
        elif first_arg.startswith("Thanks for playing."):
            self.total_score = int(re.findall(r"\d+", first_arg)[0])

    def _mock_input(self, *args, **kwargs):
        prompt = args[0]
        if prompt.startswith("Wanna play?"):
            return "y"
        elif prompt.startswith("Enter dice to keep (no spaces), or (q)uit:"):
            scorers = GameLogic.get_scorers(self.roll)
            keepers = "".join([str(ch) for ch in scorers])
            return keepers
        elif prompt.startswith("(r)oll again, (b)ank your points or (q)uit "):
            return "b"
        else:
            raise ValueError(f"Unrecognized prompt {prompt}")

class Skynet(BasePlayer):
  def __init__(self):
    super().__init__()
    self.roll = None
    self.ai_name = 'Skynet'

  def _mock_print(self, *args, **kwargs):
    first_arg = args[0]
    first_char = first_arg[0]
    if first_char.isdigit():
      self.roll = tuple(int(char) for char in first_arg.split(','))
    elif first_arg.startswith('Thanks for playing.'):
      self.total_score = int(re.findall(r'\d+', first_arg)[0])

  def _mock_input(self, *args, **kwargs):
    prompt = args[0]
    if prompt.startswith('Wanna play?'):
      self.old_print('Wanna play? y')
      return 'y'
    elif prompt.startswith('Enter dice'):
      self.old_print(f'Rolling {len(self.roll)} dice...')
      self.old_print(self.roll)
      scorers = GameLogic.smarter_get_scorers(self.roll)
      self.old_print(scorers)
      keepers = ''.join([str(ch) for ch in scorers])
      self.unbanked += GameLogic.calculate_score(scorers)
      self.old_print(f"Enter dice to keep (no spaces), or (q)uit: {keepers}")
      self.dice = self.dice - len(keepers)
      self.old_print(f'You have {self.unbanked} unbanked points and {self.dice} dice remaining')
      return keepers
    elif prompt.startswith('(r)oll again'):
      if self.dice < 3:
        self.dice = 6
        self.old_print("(r)oll again, (b)ank your points or (q)uit b")
        self.old_print(f"Skynet banked {self.unbanked} points")
        self.running_total += self.unbanked
        self.unbanked = 0
        self.old_print(f"Total score is {self.running_total} points")
        self.old_print("Starting next round")
        return 'b'
      else:
        self.old_print("(r)oll again, (b)ank your points or (q)uit r")
        return 'r'
    else:
        raise ValueError(f"Unrecognized prompt {prompt}")

if __name__ == "__main__":
    # Naysayer.play()
    Skynet.play(10)
    NervousNellie.play(10)
    
Collaborators:
Eugene Monnier
Thomas Sherer
Vij Rangarajan

# Road Map:
## 1st Milestone
### Features
- Define a `GameLogic` class.
- Handle calculating score for dice roll
  - Add `calculate_score` static method to GameLogic class.
  - The input to `calculate_score` is a tuple of integers that represent a dice roll.
  - The output from `calculate_score` is an integer representing the roll’s score according to rules of game.
- Handle rolling dice
  - Add `roll_dice` static method to GameLogic class.
  - The input to `roll_dice` is an integer between 1 and 6.
  - The output of `roll_dice` is a tuple with random values between 1 and 6.
  - The length of tuple must match the argument given to `roll_dice` method.
- Handle banking points
  - Define a `Banker` class
  - Add a `shelf` instance method
    - Input to `shelf` is the amount of points (integer) to add to shelf.
    - `shelf` should temporarily store unbanked points.
  - Add a `bank` instance method
    - `bank` should add any points on the shelf to total and reset shelf to 0.
    - `bank` output should be the amount of points added to total from shelf.
  - Add a `clear_shelf` instance method
    - `clear_shelf` should remove all unbanked points.
### Pull Request
[PR #3](https://github.com/vijayetar/Game-Of-Life/pull/3)

## 2nd Milestone
### Features
- Application should implement all features from previous version
- Application should simulate rolling between 1 and 6 dice
- Application should allow user to set aside dice each roll
- Application should allow “banking” current score or rolling again.
- Application should keep track of total score
- Application should keep track of current round
- Application should have automated tests to ensure proper operation
### Pull Request
[PR #4](https://github.com/vijayetar/Game-Of-Life/pull/4)

## 3rd Milestone
### Features
- Application should implement features from versions 1 and 2
- Should handle when cheating occurs.
  - Or just typos.
  - E.g. roll = [1,3,5,2] and user selects 1, 1, 1, 1, 1, 1
- Should allow user to continue rolling with 6 new dice when all dice have scored in current turn.
- Handle zilch
  - No points for round, and round is over ensure proper operation
### Pull Request
[PR #5](https://github.com/vijayetar/Game-Of-Life/pull/5)

## 4th Milestone
### Features
- Create an AI Bot to play Game of Greed
  - The only method available for use from `Game` class is `play`.
  - All static methods of `GameLogic` class are available.
  - All other interactions with game can take place **ONLY** via the I/O features of the game.
- Your Bot class should be added to `player_bot.py` file with name of your choosing.
  - `Skynet` is online.
- User should be able to see your bot play by executing `player_bot.py` from terminal.
- Application should implement features from previous classes
- Added Gamelogic static method `only_scoring_dice`.
  - User is only allowed to "shelve" dice that will increase their score.
### Pull Request
[PR #6](https://github.com/vijayetar/Game-Of-Life/pull/6)

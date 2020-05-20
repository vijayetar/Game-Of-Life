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

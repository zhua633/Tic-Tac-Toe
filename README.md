# Tic-Tac-Toe
Welcome to my personal project, Tic-Tac-Toe! Written in Python using the Pygame library, this game brings the classic tic-tac-toe experience to life on your screen. To get started, simply navigate to the `runner.py` file and hit start. Watch as a new window pops up, ready for you to challenge the computer.

In this game, you have the freedom to choose whether you want to play as "X" or "O." The computer will then take on the opposing role. But here's where the magic happens - the computer utilizes an advanced algorithm called Alpha-Beta Pruning to calculate its next move.

Alpha-Beta Pruning is a technique used in game theory and search algorithms to minimize the number of nodes evaluated in the game tree. By intelligently pruning branches that are guaranteed to be worse than previously evaluated moves, the computer can make more efficient decisions.

<p align="center">
  <img src="Images/game_start.png?raw=true"/>
</p>

As you make your moves, the computer analyzes the current game state, considering all possible moves and their potential outcomes. It strategically prunes off branches that are unlikely to lead to a favorable outcome, reducing the search space and speeding up the decision-making process.

With this sophisticated approach, the computer aims to find the optimal move, maximizing its chances of winning or achieving a draw. Prepare for a challenging and strategic game of tic-tac-toe where the computer is a formidable opponent.

<p align="center">
  <img src="Images/Player.png?raw=true"/>
</p>

The game ends if you or the AI wins or the game has ran out of remaining possible steps.

<p align="center">
  <img src="Images/game_over.png?raw=true"/>
</p>

So, dive in, choose your symbol, and experience the thrill of playing against an AI that harnesses the power of Alpha-Beta Pruning to make calculated moves. Good luck and enjoy the game!

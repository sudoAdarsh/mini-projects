# Blackjack Game in Python

A simple command-line Blackjack game where the user plays against the computer. The goal is to get as close to 21 points as possible without exceeding it.

## Features

- **Blackjack**: If you get a hand of 21, you win automatically.
- **Game flow**: The user and the computer are dealt cards. The user can choose to draw more cards. The computer will draw until it has 17 or more points.
- **Bust**: If the sum of the user's or computer's cards exceeds 21, it's a bust and the game ends.
- **Draw**: If both the user and the computer have the same score, it's a draw.

## How to Play

1. The game starts by dealing 2 cards to both the user and the computer.
2. The user is shown their cards and one of the computer’s cards.
3. The user can choose to draw another card or stop.
4. The computer will continue drawing cards until it has a score of 17 or higher.
5. The game ends when either the user or the computer wins, or there’s a draw.


## Running the Game

1. Clone or download the repository
   ```bash
   git clone <repo url>
   ```
3. change current working directory
   
   ```bash
   cd Blackjack
   ```
4. Run the script using Python:

   ```bash
   python blackjack.py
   ```

## Demo

[demo.webm](https://github.com/user-attachments/assets/65f3660d-65de-424f-92a8-50e605efa679)

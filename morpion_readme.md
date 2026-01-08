# ❌⭕ Tic-Tac-Toe (Morpion)

A classic two-player Tic-Tac-Toe game built in Python with score tracking and replay functionality.

## 📋 Features

- **Two-player gameplay** - Play against a friend locally
- **Symbol selection** - Player 1 chooses between X or O
- **Score tracking** - Keeps track of wins across multiple rounds
- **Input validation** - Prevents invalid moves and inputs
- **Replay option** - Play multiple rounds without restarting
- **Draw detection** - Automatically detects tie games
- **Simple ASCII board** - Clean terminal-based interface

## 🎮 How to Play

### Game Rules

1. The game is played on a 3x3 grid (positions 0-8)
2. Players take turns placing their symbol (X or O) on the board
3. First player to get 3 of their symbols in a row (horizontally, vertically, or diagonally) wins
4. If all 9 squares are filled and no player has won, the game is a draw

### Board Layout

```
0  |1  |2
---+---+---
3  |4  |5
---+---+---
6  |7  |8
```

## 🚀 Getting Started

### Prerequisites

- Python 3.6 or higher

### Installation

1. Clone the repository:
```bash
git clone https://github.com/mahira-manico/TicTacToe-v.2.git
cd TicTacToe-v.2
```

2. Run the game:
```bash
python TicTacToe-v.2.py
```

## 💻 Usage

### Starting a Game

1. Run the script
2. Player 1 selects their symbol (X or O)
3. Players alternate turns by entering a position number (0-8)
4. The game announces the winner or a draw
5. Choose whether to play again (y/n)

### Example Gameplay

```
Player 1, choose a symbol X or O: X
Player 1 you are X!

Player 1 choose a position (0-8): 4
   |   |  
---+---+---
   |X  |  
---+---+---
   |   |  

Player 2 choose a position (0-8): 0
O  |   |  
---+---+---
   |X  |  
---+---+---
   |   |  
```

## 🛠️ Code Structure

### Main Functions

- **`morpion_game()`** - Main game controller
- **`print_board()`** - Displays the current board state
- **`winner(player)`** - Checks if a player has won
- **`equal()`** - Checks for a draw
- **`symbols()`** - Handles player symbol selection
- **`play()`** - Main game loop handling turns

### Win Conditions

The game checks for wins in:
- **Rows:** (0,1,2), (3,4,5), (6,7,8)
- **Columns:** (0,3,6), (1,4,7), (2,5,8)
- **Diagonals:** (0,4,8), (2,4,6)


## 🔧 Future Improvements

- [ ] Fix score tracking to only count wins
- [ ] Add single-player mode with AI opponent
- [ ] Implement difficulty levels (Easy, Medium, Hard)
- [ ] Add color support for better visualization
- [ ] Add game statistics (total games, win rate)
- [ ] Implement undo/redo functionality
- [ ] Save game history to file


## 📝 Game Flow

```
Start Game
    ↓
Player 1 selects symbol (X or O)
    ↓
┌─────────────────────┐
│   Player 1 Turn     │
│   (Enter position)  │
└──────────┬──────────┘
           ↓
    Check for Win/Draw
           ↓
    ┌──Yes──→ Display Result → Replay? → Yes ──┐
    │                              ↓            │
    No                            No            │
    ↓                              ↓            │
┌─────────────────────┐         End Game       │
│   Player 2 Turn     │                        │
│   (Enter position)  │                        │
└──────────┬──────────┘                        │
           ↓                                    │
    Check for Win/Draw                         │
           ↓                                    │
    ┌──Yes──→ Display Result → Replay? ────────┘
    │                              ↓
    No                            No
    ↓                              ↓
Back to Player 1              End Game
```

## 👤 Author

**Mahira Manico**

- GitHub: [@mahira-manico](https://github.com/mahira-manico)


## 🎯 Learning Objectives

This project demonstrates:
- Game logic implementation
- Input validation and error handling
- Function organization and modularity
- Loop control and game state management
- Basic Python programming concepts

---

⭐ Enjoy the game! Feel free to contribute improvements or report bugs.
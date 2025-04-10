# Hangman – A Console-Based Word Guessing Game in Python

## 🎮 Hangman – A Console-Based Word Guessing Game

This is a simple implementation of the classic Hangman game using Python. The game randomly selects a word from a predefined list, and the player must guess the word one letter at a time. Each incorrect guess results in a part of the hangman being drawn. The game ends when the player either correctly guesses the word or runs out of lives.

---

### 🛠 Features:
- Random word selection from a predefined list
- Graphical ASCII representation of the hangman
- Real-time display of guessed letters and progress
- User-friendly input and output
- Multiple versions showcasing incremental improvements:
  - `hangman_basic.py`: Basic implementation (only first match revealed)
  - `hangman_with_multiple_letters.py`: Displays all matching letters in one guess
  - `hangman_refined_loop.py`: Cleaner, loop-optimized version for better efficiency
  - `hangman_final_tweaks.py`: Final revision with minor logical improvements

---

### 📁 Version Descriptions:

#### `hangman_basic.py`
This is the **initial version** of the Hangman game. It selects a random word and displays underscores for each letter.

- Only the **first occurrence** of a guessed letter is revealed.
- Simple gameplay with 6 wrong guess attempts.
- ASCII-based hangman visualization.

#### `hangman_with_multiple_letters.py`
Improves the logic to reveal **all occurrences** of the guessed letter in one go.

- Iterates through the word to reveal every match.
- Better user experience than the basic version.
- Code has redundant steps but shows enhanced logic.

#### `hangman_refined_loop.py`
More efficient and readable version.

- Uses a refined loop and indexing strategy.
- All matches shown correctly with less overhead.
- Clean separation of logic for better maintainability.

#### `hangman_final_tweaks.py`
Final version with subtle logic improvements.

- Adds a `break` after each match to control repeated reveals.
- More readable structure, useful as a base for future upgrades.

---

### 🚀 How to Run:
```bash
python hangman_basic.py
# or
python hangman_with_multiple_letters.py
# or
python hangman_refined_loop.py
# or
python hangman_final_tweaks.py
```

---

### 🧠 Concepts Used:
- Loops and conditionals
- Lists and string manipulation
- Random module
- ASCII art for visualization

---

### 📌 Note:
This game is designed for educational purposes and console-based gameplay. Future improvements can include GUI versions using `tkinter` or expanding the word list using a file input.

---

### 👨‍💻 Author:
Your Name Ghanashyam M Dinesh

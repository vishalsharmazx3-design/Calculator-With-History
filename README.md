# Simple Calculator with History

A command-line **calculator** built in Python that performs basic arithmetic operations and keeps a **history** of all calculations saved to a text file — with options to view, clear, or exit.

## Features

- **Basic Calculator Operations** — Addition, subtraction, multiplication, division.
- **History Tracking** — Every calculation is automatically saved to `history.txt`.
- **View History** — See all past calculations, most recent first.
- **Clear History** — Wipe the saved history file clean.
- **Exit Functionality** — Quit the program safely.

## Concepts Used

| Concept | Where it's used |
|---|---|
| **Input** (`input()`) | Getting the user's calculation or command |
| **Functions** | Organizing code into `calculate()`, `show_history()`, `clear_history()`, `save_to_history()` |
| **Conditionals** | Deciding whether to calculate, show history, clear history, or exit |
| **File Handling** | Saving/loading/clearing history using `history.txt` |
| **Loops** (`while`) | Keeps the program running until the user types `exit` |
| **Basic Math** | Performing `+`, `-`, `*`, `/` operations |

## How It Works

1. The program stores calculation history in a text file called `history.txt`.
2. Every time a calculation is done, it's saved in the format:
   ```
   8 + 8 = 16
   ```
3. Typing `history` reads the file and prints all past calculations (newest first).
4. Typing `clear` empties the history file.
5. Typing `exit` ends the program.
6. Anything else is treated as a calculation input.

## Commands

| Command | Action |
|---|---|
| `history` | Show all past calculations |
| `clear` | Clear the saved history |
| `exit` | Quit the program |
| `<num> <op> <num>` | Perform a calculation (e.g. `8 + 8`) |

## Calculation Format

Input must follow the pattern: `number operator number`, separated by spaces.

```
Enter calculation: 10 + 5
Result: 15
```

Supported operators: `+`  `-`  `*`  `/`

- Dividing by zero is blocked with an error message.
- Whole number results (e.g. `10.0`) are automatically shown as integers (`10`).
- Invalid formats or non-numeric input show a friendly error instead of crashing.

## How to Run

1. Make sure Python 3 is installed.
2. Save the code as `calculator.py`.
3. Run it from the terminal:

```bash
python calculator.py
```

4. A `history.txt` file will be created automatically in the same folder the first time you calculate something.

## Requirements

- Python 3.x
- No external libraries needed (uses only built-in Python features)

## Example Usage

```
----- SIMPLE CALCULATOR -----
Type: history | clear | exit

Enter calculation: 8 + 8
Result: 16

Enter calculation: 20 / 4
Result: 5

Enter calculation: history
20.0 / 4.0 = 5
8.0 + 8.0 = 16

Enter calculation: clear
History cleared.

Enter calculation: exit
Goodbye!
```

## Possible Future Improvements

- Support more operations (power, square root, modulus).
- Add timestamps to each history entry.
- Support multi-step / chained expressions (e.g. `2 + 3 * 4`).
- Add a "delete specific entry" option instead of clearing all history.
- Save history in JSON/CSV for easier data processing.

## Author

Built as a beginner Python project to practice functions, file handling, conditionals, and loops.

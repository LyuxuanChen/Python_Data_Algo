# Python Data Structures and Algorithms

Personal Python practice for HKU ENGG1330, including sorting, searching, recursion, Python language experiments, and small interactive projects.

The files are standalone learning scripts rather than a single application. Many contain several examples, hard-coded sample values, and commented-out experiments.

## File guide

| File | Topics and behavior |
| --- | --- |
| [Recursion Algorithms.py](Recursion%20Algorithms.py) | Merge sort, factorial, recursive binary search, Fibonacci numbers, summing nested lists, palindrome checking, and finding the first and last occurrences of a target with recursive binary search. Runs several built-in examples. |
| [Sorting Algorithms.py](Sorting%20Algorithms.py) | Bubble sort, insertion sort, and selection sort. The current examples run bubble sort and insertion sort; the selection-sort example call is commented out. |
| [SlicingString.py](SlicingString.py) | String-slicing notes, function return values, string joining, formatted strings, and constructing a two-dimensional list. Several experiments are commented out. |
| [Tuples.py](Tuples.py) | Tuple notes, mutable lists inside tuples, list comprehensions, and the return value of `list.sort()`. |
| [loop Test.py](loop%20Test.py) | Loop ranges and chained comparisons. |
| [CheckboardTiles Assignment1 Optimal.py](CheckboardTiles%20Assignment1%20Optimal.py) | Prints a checkerboard using nested loops, integer division, and parity. Reads three integers from standard input. |
| [L3Challenge5.py](L3Challenge5.py) | Finds the longest contiguous sequence of names without repetition, using nested loops and a set. Prints its one-based starting position and length. |
| [Tut2Q5Clock.py](Tut2Q5Clock.py) | Simulates rotating a three-digit lock, with each digit wrapping independently. Uses hard-coded sample values. |
| [SamplePuzzle.py](SamplePuzzle.py) | An interactive text-adventure prototype with commands, a locker puzzle, and inventory state. |
| [Puzzle1.py](Puzzle1.py) | An interactive Caesar-cipher puzzle with rotation instructions, input validation, and hints. |
| [RLtrial.py](RLtrial.py) | A Tkinter interface for replaying ten training episodes from a Q-learning maze project. Requires a companion module that is not included in this repository; see below. |

## Requirements

- Python 3.
- A terminal or Python IDE for running individual scripts.
- The standalone exercises use Python's standard library; they do not require packages installed with `pip`.
- `RLtrial.py` additionally requires Tkinter, a graphical desktop session, and the companion `maze_car` module.

## Run the examples

From the folder containing these files:

```bash
python3 "Recursion Algorithms.py"
python3 "Sorting Algorithms.py"
python3 Tuples.py
```

Quote filenames that contain spaces. If your Python installation uses `python` instead of `python3`, use that command instead.

To obtain the repository on another computer:

```bash
git clone https://github.com/LyuxuanChen/Python_Data_Algo.git
cd Python_Data_Algo
```

### Exercises that read input

For the checkerboard exercise:

```bash
python3 "CheckboardTiles Assignment1 Optimal.py"
```

Enter three integers, one per line: the number of tile rows, the number of tile columns, and the side length of each tile. For example:

```text
2
3
2
```

The current script also prints a final `0` from a separate modulo experiment after the checkerboard.

For the unique-name sequence exercise:

```bash
python3 L3Challenge5.py
```

Enter the number of names, followed by one name per line. For example:

```text
5
ALICE
BOB
ALICE
CAROL
DAVE
```

Output:

```text
2
4
```

The longest sequence without repetition starts at position 2 and contains four names.

### Interactive puzzles

```bash
python3 SamplePuzzle.py
python3 Puzzle1.py
```

Run these separately. `SamplePuzzle.py` displays commands such as `look`, `help`, and `quit`. `Puzzle1.py` prompts for a five-letter L/R rotation sequence and offers hints after incorrect attempts. Press `Ctrl+C` in the terminal to stop a running script.

### Maze training replay

`RLtrial.py` imports `ROOT`, `DIRS`, `generate`, and `train` from `maze_car`. That module is not currently present in this repository, so this script cannot run independently from the files here.

With the companion module available, the script reads training data from `ROOT / "outputs/training_timeline.json"`. If that file does not exist, it calls the companion training function to generate the data. Its interface provides replay, pause/resume, playback-speed, and retraining controls.

## Learning notes

- Binary-search examples require input sorted in ascending order and use inclusive `left` and `right` bounds. The initial right bound is `len(readings) - 1`.
- The recursive boundary search continues left or right after finding a match, keeping the matching index as a fallback.
- Recursive functions need stopping conditions, such as an empty search interval, a string of length at most one, or Fibonacci's two base cases.
- The slicing-based palindrome example creates substrings. The recursive binary-search examples pass index bounds and avoid copying the input list.
- Many examples run at the top level when a file is executed or imported. Run scripts directly when exploring their printed output.

These files record learning progress and experimentation. Some include extra output and earlier attempts, so check the active code and input format before adapting an example for an assessed exercise.

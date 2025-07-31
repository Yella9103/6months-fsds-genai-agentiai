# 🧩 Sudoku Game with Streamlit

A fully-featured Sudoku game built with Python and Streamlit, featuring puzzle generation, validation, hints, and a beautiful web interface.

## Features

- 🎯 **Multiple Difficulty Levels**: Easy, Medium, Hard, and Expert
- 🧠 **Smart Puzzle Generation**: Unique, solvable puzzles using backtracking algorithm
- 💡 **Hint System**: Get help when you're stuck
- ⏱️ **Timer**: Track your solving time
- 📊 **Statistics**: Monitor mistakes, hints used, and progress
- 🎨 **Beautiful UI**: Modern Streamlit interface with custom styling
- ✅ **Validation**: Real-time move validation and error detection
- 🔄 **Game Controls**: Reset, solve, and pause functionality
- 📈 **Performance Scoring**: Get rated based on time, mistakes, and hints

## Game Rules

1. **Objective**: Fill the 9x9 grid with numbers 1-9
2. **Rules**: 
   - Each row must contain numbers 1-9 without repetition
   - Each column must contain numbers 1-9 without repetition
   - Each 3x3 box must contain numbers 1-9 without repetition
   - Original numbers cannot be changed
3. **Scoring**: Performance based on time, mistakes, and hints used

## Installation

1. **Clone or download the project files**

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the game**:
   ```bash
   streamlit run app.py
   ```

4. **Open your browser** and navigate to the URL shown in the terminal (usually `http://localhost:8501`)

## Project Structure

```
sudoku-game/
├── app.py              # Main Streamlit application
├── sudoku_game.py      # Core game logic and classes
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## How to Play

1. **Start the Game**: Run `streamlit run app.py`
2. **Select Difficulty**: Choose from Easy, Medium, Hard, or Expert
3. **Play the Game**:
   - Use the cell selector to choose a cell
   - Use the number pad to enter numbers
   - Use hints if you're stuck
   - Monitor your progress and statistics
4. **Complete the Puzzle**: Fill all cells correctly to win

## Game Features

### Difficulty Levels
- **Easy**: 40 numbers removed (41 filled)
- **Medium**: 50 numbers removed (31 filled)
- **Hard**: 60 numbers removed (21 filled)
- **Expert**: 70 numbers removed (11 filled)

### Visual Elements
- **Green Numbers**: Original puzzle numbers (cannot be changed)
- **Black Numbers**: User-entered numbers
- **Gray Cells**: Empty cells to fill
- **Styled Grid**: Clear 3x3 box boundaries

### Controls
- **Cell Selector**: 9x9 grid to select cells
- **Number Pad**: 1-9 buttons for number input
- **Clear Button**: Remove number from selected cell
- **Hint Button**: Get help with next move
- **Reset Button**: Reset puzzle to original state
- **Solve Button**: Show complete solution
- **Pause Timer**: Stop/start the timer

### Statistics
- **Time**: Elapsed solving time (MM:SS format)
- **Mistakes**: Number of invalid moves made
- **Hints Used**: Number of hints requested
- **Progress**: Percentage of puzzle completed

## Technical Details

### Core Classes
- **SudokuGame**: Main game logic with puzzle generation, validation, and solving
- **SudokuController**: Manages game state, timer, and user interactions

### Algorithms
- **Puzzle Generation**: Starts with solved board, randomizes, then removes numbers
- **Backtracking Solver**: Finds solution for any valid puzzle
- **Move Validation**: Checks row, column, and box constraints
- **Hint System**: Provides next move from solution

### Technologies Used
- **Python**: Core programming language
- **Streamlit**: Web application framework
- **Pandas**: Data manipulation and display
- **NumPy**: Numerical operations

### Key Features
- **Session State Management**: Persistent game state across interactions
- **Real-time Validation**: Immediate feedback on moves
- **Responsive Design**: Works on different screen sizes
- **Custom Styling**: Beautiful CSS styling for better UX

## Game Mechanics

### Puzzle Generation
1. **Create Solved Board**: Start with a valid 9x9 Sudoku solution
2. **Randomize**: Apply random row/column swaps within 3x3 boxes
3. **Number Removal**: Remove cells based on difficulty level
4. **Validate**: Ensure puzzle has unique solution

### Move Validation
- **Row Check**: No duplicate numbers in same row
- **Column Check**: No duplicate numbers in same column
- **Box Check**: No duplicate numbers in same 3x3 box
- **Original Protection**: Cannot modify original numbers

### Hint System
- **Next Empty Cell**: Finds first empty cell
- **Solution Lookup**: Gets correct number from solution
- **Auto-Placement**: Automatically places the hint

### Performance Scoring
- **Time Score**: Base 100 points minus time penalty
- **Mistake Penalty**: -10 points per mistake
- **Hint Penalty**: -5 points per hint used
- **Final Score**: Maximum of 0 points

## Customization

You can easily customize the game by modifying:

- **Difficulty Levels**: Adjust `difficulty_levels` in `SudokuGame`
- **Scoring System**: Modify penalty values in `display_completion_message()`
- **Visual Styling**: Update CSS in the `st.markdown()` section
- **Board Size**: Change grid dimensions (currently 9x9)

## Troubleshooting

### Common Issues

1. **Port already in use**: 
   - Try running `streamlit run app.py --server.port 8502`

2. **Dependencies not found**:
   - Make sure to run `pip install -r requirements.txt`

3. **Game not responding**:
   - Check browser console for errors
   - Try refreshing the page

4. **Timer not updating**:
   - The timer updates every second
   - Check if timer is paused

### Performance Tips

- Close other browser tabs to improve performance
- Use a modern browser (Chrome, Firefox, Safari, Edge)
- Ensure stable internet connection for smooth gameplay

## Advanced Features

### Puzzle Generation Algorithm
The game uses a sophisticated algorithm to generate unique, solvable puzzles:

1. **Base Pattern**: Start with a valid Sudoku solution
2. **Randomization**: Apply random transformations while maintaining validity
3. **Number Removal**: Remove cells strategically to maintain uniqueness
4. **Validation**: Ensure puzzle has exactly one solution

### Solving Algorithm
The backtracking solver can solve any valid Sudoku puzzle:

1. **Find Empty Cell**: Locate next empty cell
2. **Try Numbers**: Test numbers 1-9 in the cell
3. **Validate Move**: Check if number is valid
4. **Recurse**: If valid, continue with next cell
5. **Backtrack**: If no valid number, backtrack to previous cell

### Hint System
The hint system provides intelligent assistance:

1. **Find Empty Cell**: Locate first empty cell
2. **Solution Lookup**: Get correct number from solution
3. **Auto-Placement**: Place the number automatically
4. **Statistics Update**: Track hint usage

## Contributing

Feel free to contribute improvements:
- Add new difficulty levels
- Implement different puzzle generation algorithms
- Add sound effects
- Create multiplayer functionality
- Add puzzle import/export features
- Implement different visual themes

## License

This project is open source and available under the MIT License.

---

**Enjoy solving Sudoku puzzles! 🧩🎯** 
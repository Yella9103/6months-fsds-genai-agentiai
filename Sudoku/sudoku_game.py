import random
import copy
import time
from typing import List, Tuple, Optional, Set
import streamlit as st

class SudokuGame:
    def __init__(self, difficulty: str = "medium"):
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        self.solution = [[0 for _ in range(9)] for _ in range(9)]
        self.original_board = [[0 for _ in range(9)] for _ in range(9)]
        self.difficulty = difficulty
        self.difficulty_levels = {
            "easy": 40,      # Remove 40 numbers
            "medium": 50,    # Remove 50 numbers
            "hard": 60,      # Remove 60 numbers
            "expert": 70     # Remove 70 numbers
        }
        self.generate_puzzle()
    
    def is_valid_move(self, row: int, col: int, num: int) -> bool:
        """Check if placing num at (row, col) is valid"""
        # Check row
        for x in range(9):
            if self.board[row][x] == num:
                return False
        
        # Check column
        for x in range(9):
            if self.board[x][col] == num:
                return False
        
        # Check 3x3 box
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.board[i + start_row][j + start_col] == num:
                    return False
        
        return True
    
    def find_empty(self) -> Optional[Tuple[int, int]]:
        """Find an empty cell in the board"""
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return (i, j)
        return None
    
    def solve_puzzle(self, board: List[List[int]]) -> bool:
        """Solve the Sudoku puzzle using backtracking"""
        empty = self.find_empty_in_board(board)
        if not empty:
            return True
        
        row, col = empty
        for num in range(1, 10):
            if self.is_valid_move_in_board(board, row, col, num):
                board[row][col] = num
                if self.solve_puzzle(board):
                    return True
                board[row][col] = 0
        
        return False
    
    def find_empty_in_board(self, board: List[List[int]]) -> Optional[Tuple[int, int]]:
        """Find an empty cell in a given board"""
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return (i, j)
        return None
    
    def is_valid_move_in_board(self, board: List[List[int]], row: int, col: int, num: int) -> bool:
        """Check if placing num at (row, col) is valid in a given board"""
        # Check row
        for x in range(9):
            if board[row][x] == num:
                return False
        
        # Check column
        for x in range(9):
            if board[x][col] == num:
                return False
        
        # Check 3x3 box
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if board[i + start_row][j + start_col] == num:
                    return False
        
        return True
    
    def generate_puzzle(self):
        """Generate a new Sudoku puzzle"""
        # Start with a solved board
        self.generate_solved_board()
        
        # Copy the solution
        self.solution = copy.deepcopy(self.board)
        
        # Remove numbers based on difficulty
        cells_to_remove = self.difficulty_levels.get(self.difficulty, 50)
        self.remove_numbers(cells_to_remove)
        
        # Store the original board (for checking user input)
        self.original_board = copy.deepcopy(self.board)
    
    def generate_solved_board(self):
        """Generate a solved Sudoku board"""
        # Start with a simple pattern
        self.board = [
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [4, 5, 6, 7, 8, 9, 1, 2, 3],
            [7, 8, 9, 1, 2, 3, 4, 5, 6],
            [2, 3, 1, 5, 6, 4, 8, 9, 7],
            [5, 6, 4, 8, 9, 7, 2, 3, 1],
            [8, 9, 7, 2, 3, 1, 5, 6, 4],
            [3, 1, 2, 6, 4, 5, 9, 7, 8],
            [6, 4, 5, 9, 7, 8, 3, 1, 2],
            [9, 7, 8, 3, 1, 2, 6, 4, 5]
        ]
        
        # Randomize the board by swapping rows/columns within boxes
        self.randomize_board()
    
    def randomize_board(self):
        """Randomize the solved board while maintaining Sudoku rules"""
        for _ in range(50):  # Perform 50 random transformations
            # Random row swaps within the same box
            box = random.randint(0, 2)
            row1 = box * 3 + random.randint(0, 2)
            row2 = box * 3 + random.randint(0, 2)
            if row1 != row2:
                self.board[row1], self.board[row2] = self.board[row2], self.board[row1]
            
            # Random column swaps within the same box
            box = random.randint(0, 2)
            col1 = box * 3 + random.randint(0, 2)
            col2 = box * 3 + random.randint(0, 2)
            if col1 != col2:
                for row in range(9):
                    self.board[row][col1], self.board[row][col2] = self.board[row][col2], self.board[row][col1]
    
    def remove_numbers(self, count: int):
        """Remove numbers from the solved board to create the puzzle"""
        positions = [(i, j) for i in range(9) for j in range(9)]
        random.shuffle(positions)
        
        for i, j in positions[:count]:
            self.board[i][j] = 0
    
    def is_complete(self) -> bool:
        """Check if the puzzle is complete and correct"""
        # Check if all cells are filled
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return False
        
        # Check if the solution is correct
        return self.is_valid_solution()
    
    def is_valid_solution(self) -> bool:
        """Check if the current board is a valid Sudoku solution"""
        # Check rows
        for row in range(9):
            if len(set(self.board[row])) != 9:
                return False
        
        # Check columns
        for col in range(9):
            column = [self.board[row][col] for row in range(9)]
            if len(set(column)) != 9:
                return False
        
        # Check 3x3 boxes
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                box = []
                for i in range(3):
                    for j in range(3):
                        box.append(self.board[box_row + i][box_col + j])
                if len(set(box)) != 9:
                    return False
        
        return True
    
    def get_hint(self) -> Optional[Tuple[int, int, int]]:
        """Get a hint for the next move"""
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return (i, j, self.solution[i][j])
        return None
    
    def get_cell_status(self, row: int, col: int) -> str:
        """Get the status of a cell (original, user-filled, or empty)"""
        if self.original_board[row][col] != 0:
            return "original"
        elif self.board[row][col] != 0:
            return "user"
        else:
            return "empty"
    
    def get_possible_numbers(self, row: int, col: int) -> Set[int]:
        """Get possible numbers for a cell"""
        if self.board[row][col] != 0:
            return set()
        
        possible = set(range(1, 10))
        for num in range(1, 10):
            if not self.is_valid_move(row, col, num):
                possible.discard(num)
        
        return possible
    
    def reset_puzzle(self):
        """Reset the puzzle to its original state"""
        self.board = copy.deepcopy(self.original_board)
    
    def solve_current_puzzle(self):
        """Solve the current puzzle"""
        self.board = copy.deepcopy(self.solution)
    
    def get_difficulty_info(self) -> dict:
        """Get information about the current difficulty level"""
        filled_cells = sum(1 for row in self.board for cell in row if cell != 0)
        total_cells = 81
        empty_cells = total_cells - filled_cells
        
        return {
            "difficulty": self.difficulty,
            "filled_cells": filled_cells,
            "empty_cells": empty_cells,
            "completion_percentage": round((filled_cells / total_cells) * 100, 1)
        }

class SudokuController:
    def __init__(self):
        self.game = SudokuGame()
        self.timer_start = None
        self.timer_running = False
        self.mistakes = 0
        self.hints_used = 0
    
    def new_game(self, difficulty: str = "medium"):
        """Start a new game with specified difficulty"""
        self.game = SudokuGame(difficulty)
        self.timer_start = None
        self.timer_running = False
        self.mistakes = 0
        self.hints_used = 0
    
    def start_timer(self):
        """Start the game timer"""
        if not self.timer_running:
            self.timer_start = time.time()
            self.timer_running = True
    
    def get_elapsed_time(self) -> int:
        """Get elapsed time in seconds"""
        if not self.timer_running or self.timer_start is None:
            return 0
        return int(time.time() - self.timer_start)
    
    def format_time(self, seconds: int) -> str:
        """Format time as MM:SS"""
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes:02d}:{seconds:02d}"
    
    def make_move(self, row: int, col: int, number: int) -> bool:
        """Make a move and return if it's correct"""
        if self.game.original_board[row][col] != 0:
            return False  # Can't modify original numbers
        
        if number == 0:
            self.game.board[row][col] = 0
            return True
        
        if self.game.is_valid_move(row, col, number):
            self.game.board[row][col] = number
            return True
        else:
            self.mistakes += 1
            return False
    
    def get_hint(self) -> Optional[Tuple[int, int, int]]:
        """Get a hint and increment hint counter"""
        hint = self.game.get_hint()
        if hint:
            self.hints_used += 1
        return hint
    
    def get_game_stats(self) -> dict:
        """Get current game statistics"""
        return {
            "elapsed_time": self.get_elapsed_time(),
            "formatted_time": self.format_time(self.get_elapsed_time()),
            "mistakes": self.mistakes,
            "hints_used": self.hints_used,
            "difficulty_info": self.game.get_difficulty_info(),
            "is_complete": self.game.is_complete()
        } 
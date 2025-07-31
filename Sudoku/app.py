import streamlit as st
import time
import pandas as pd
import numpy as np
from sudoku_game import SudokuController

# Page configuration
st.set_page_config(
    page_title="Sudoku Game",
    page_icon="🧩",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #2E8B57;
        margin-bottom: 2rem;
    }
    .game-container {
        border: 2px solid #2E8B57;
        border-radius: 10px;
        padding: 20px;
        background-color: #f0f8f0;
        margin: 10px 0;
    }
    .stats-container {
        display: flex;
        justify-content: space-around;
        margin: 20px 0;
    }
    .stButton > button {
        background-color: #2E8B57;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        font-weight: bold;
        margin: 5px;
    }
    .stButton > button:hover {
        background-color: #1a5f3a;
    }
    .sudoku-board {
        font-family: 'Courier New', monospace;
        font-size: 18px;
        font-weight: bold;
    }
    .original-cell {
        background-color: #e8f5e8;
        color: #2E8B57;
    }
    .user-cell {
        background-color: #fff;
        color: #333;
    }
    .empty-cell {
        background-color: #f9f9f9;
        color: #666;
    }
</style>
""", unsafe_allow_html=True)

def create_sudoku_board(game_controller):
    """Create an interactive Sudoku board"""
    board = game_controller.game.board
    original_board = game_controller.game.original_board
    
    # Create a styled dataframe for the Sudoku board
    df = pd.DataFrame(board)
    
    # Replace zeros with empty strings for display
    df_display = df.copy()
    df_display = df_display.replace(0, "")
    
    # Style the dataframe
    def style_cell(val, row_idx, col_idx):
        if original_board[row_idx][col_idx] != 0:
            return 'background-color: #e8f5e8; color: #2E8B57; font-weight: bold; text-align: center; font-size: 18px;'
        elif val != "":
            return 'background-color: #fff; color: #333; font-weight: bold; text-align: center; font-size: 18px;'
        else:
            return 'background-color: #f9f9f9; color: #666; text-align: center; font-size: 18px;'
    
    # Apply styling
    styled_df = df_display.style.apply(lambda row_data: [style_cell(row_data[i], row_data.name, i) for i in range(len(row_data))], axis=1)
    
    # Display the board
    st.dataframe(
        styled_df,
        hide_index=True,
        use_container_width=False,
        height=400
    )
    
    # Create a 9x9 grid of buttons for cell selection
    st.subheader("Click on cells to select:")
    
    for i in range(9):
        cols = st.columns(9)
        for j in range(9):
            with cols[j]:
                cell_value = board[i][j]
                cell_status = game_controller.game.get_cell_status(i, j)
                
                # Determine button text and style
                if cell_value == 0:
                    button_text = " "
                else:
                    button_text = str(cell_value)
                
                # Create button with different colors based on status
                button_style = ""
                if cell_status == "original":
                    button_style = "background-color: #e8f5e8; color: #2E8B57;"
                elif cell_status == "user":
                    button_style = "background-color: #fff; color: #333;"
                else:
                    button_style = "background-color: #f9f9f9; color: #666;"
                
                # Check if this cell is selected
                if 'selected_cell' in st.session_state:
                    selected_row, selected_col = st.session_state.selected_cell
                    if i == selected_row and j == selected_col:
                        button_style = "background-color: #ffeb3b; border: 2px solid #ffc107;"
                
                # Create button
                if st.button(
                    button_text,
                    key=f"board_cell_{i}_{j}",
                    help=f"Row {i+1}, Column {j+1}"
                ):
                    if cell_status != "original":  # Only allow selection of non-original cells
                        st.session_state.selected_cell = (i, j)
                        st.rerun()

def create_number_pad():
    """Create a number pad for input"""
    st.subheader("Number Input")
    
    # Create 3x3 grid of number buttons
    col1, col2, col3 = st.columns(3)
    
    with col1:
        for num in [1, 4, 7]:
            if st.button(str(num), key=f"num_{num}"):
                if 'selected_cell' in st.session_state:
                    row, col = st.session_state.selected_cell
                    game_controller = st.session_state.game_controller
                    game_controller.make_move(row, col, num)
                    del st.session_state.selected_cell
                    st.rerun()
    
    with col2:
        for num in [2, 5, 8]:
            if st.button(str(num), key=f"num_{num}"):
                if 'selected_cell' in st.session_state:
                    row, col = st.session_state.selected_cell
                    game_controller = st.session_state.game_controller
                    game_controller.make_move(row, col, num)
                    del st.session_state.selected_cell
                    st.rerun()
    
    with col3:
        for num in [3, 6, 9]:
            if st.button(str(num), key=f"num_{num}"):
                if 'selected_cell' in st.session_state:
                    row, col = st.session_state.selected_cell
                    game_controller = st.session_state.game_controller
                    game_controller.make_move(row, col, num)
                    del st.session_state.selected_cell
                    st.rerun()
    
    # Clear button
    if st.button("Clear", key="clear_cell"):
        if 'selected_cell' in st.session_state:
            row, col = st.session_state.selected_cell
            game_controller = st.session_state.game_controller
            game_controller.make_move(row, col, 0)
            del st.session_state.selected_cell
            st.rerun()

def display_game_stats(game_controller):
    """Display game statistics"""
    stats = game_controller.get_game_stats()
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Time", stats["formatted_time"])
    
    with col2:
        st.metric("Mistakes", stats["mistakes"])
    
    with col3:
        st.metric("Hints Used", stats["hints_used"])
    
    with col4:
        completion = stats["difficulty_info"]["completion_percentage"]
        st.metric("Progress", f"{completion}%")

def create_difficulty_selector():
    """Create difficulty selection"""
    st.subheader("Difficulty")
    difficulty = st.selectbox(
        "Select Difficulty",
        ["easy", "medium", "hard", "expert"],
        index=1,
        key="difficulty_selector"
    )
    
    if st.button("New Game"):
        game_controller = st.session_state.game_controller
        game_controller.new_game(difficulty)
        st.rerun()
    
    return difficulty

def create_game_controls(game_controller):
    """Create game control buttons"""
    st.subheader("Game Controls")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("💡 Hint"):
            hint = game_controller.get_hint()
            if hint:
                row, col, number = hint
                game_controller.make_move(row, col, number)
                st.success(f"Hint: Place {number} at row {row+1}, column {col+1}")
            else:
                st.warning("No hints available!")
            st.rerun()
        
        if st.button("🔄 Reset"):
            game_controller.game.reset_puzzle()
            st.rerun()
    
    with col2:
        if st.button("✅ Solve"):
            game_controller.game.solve_current_puzzle()
            st.rerun()
        
        if st.button("⏸️ Pause Timer"):
            game_controller.timer_running = not game_controller.timer_running
            st.rerun()

def display_completion_message(game_controller):
    """Display completion message when puzzle is solved"""
    if game_controller.game.is_complete():
        stats = game_controller.get_game_stats()
        
        st.success("🎉 Congratulations! You've solved the puzzle!")
        
        # Display completion stats
        st.markdown("### Completion Statistics")
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric("Time Taken", stats["formatted_time"])
            st.metric("Mistakes Made", stats["mistakes"])
        
        with col2:
            st.metric("Hints Used", stats["hints_used"])
            st.metric("Difficulty", stats["difficulty_info"]["difficulty"].title())
        
        # Performance rating
        time_score = max(0, 100 - stats["elapsed_time"] // 60)  # Time penalty
        mistake_penalty = stats["mistakes"] * 10
        hint_penalty = stats["hints_used"] * 5
        total_score = max(0, time_score - mistake_penalty - hint_penalty)
        
        st.metric("Performance Score", f"{total_score}/100")



def main():
    # Initialize session state
    if 'game_controller' not in st.session_state:
        st.session_state.game_controller = SudokuController()
    
    # Header
    st.markdown('<h1 class="main-header">🧩 Sudoku Game</h1>', unsafe_allow_html=True)
    
    # Sidebar for controls
    with st.sidebar:
        st.header("Game Controls")
        
        # Difficulty selector
        create_difficulty_selector()
        
        # Game controls
        create_game_controls(st.session_state.game_controller)
        
        # Instructions
        st.subheader("How to Play")
        st.markdown("""
        1. **Click directly on the Sudoku board** to select a cell
        2. **Enter a number** using the number pad
        3. **Use hints** if you're stuck
        4. **Complete the puzzle** by filling all cells correctly
        
        **Rules:**
        - Each row, column, and 3x3 box must contain numbers 1-9
        - No number can repeat in the same row, column, or box
        - Original numbers (green) cannot be changed
        """)
    
    # Main game area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Game board
        st.markdown('<div class="game-container">', unsafe_allow_html=True)
        st.subheader("Sudoku Board")
        create_sudoku_board(st.session_state.game_controller)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        # Game stats
        st.markdown('<div class="game-container">', unsafe_allow_html=True)
        st.subheader("Game Statistics")
        display_game_stats(st.session_state.game_controller)
        
        # Number input
        create_number_pad()
        
        # Selected cell info
        if 'selected_cell' in st.session_state:
            row, col = st.session_state.selected_cell
            st.info(f"Selected: Row {row+1}, Column {col+1}")
            
            # Show possible numbers for the selected cell
            possible = st.session_state.game_controller.game.get_possible_numbers(row, col)
            if possible:
                st.write(f"Possible numbers: {', '.join(map(str, sorted(possible)))}")
        
        st.markdown('</div>', unsafe_allow_html=True)
    

    
    # Start timer if not already running
    if not st.session_state.game_controller.timer_running:
        st.session_state.game_controller.start_timer()
    
    # Display completion message
    display_completion_message(st.session_state.game_controller)
    
    # Auto-refresh for timer
    if st.session_state.game_controller.timer_running:
        time.sleep(1)
        st.rerun()

if __name__ == "__main__":
    main() 
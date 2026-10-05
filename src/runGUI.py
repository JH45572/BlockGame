import tkinter as tk
import numpy as np

class BlockPuzzleGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Block Puzzle! Emulator")
        
        # Grid parameters
        self.rows = 8
        self.cols = 8
        self.cell_size = 50  # Pixels per grid square
        
        # Emulated board state (0 = empty, 1 = occupied)
        # In your project, you'll pass or update your actual Board object here
        self.board_state = np.zeros((self.rows, self.cols), dtype=int)
        
        # Mock some pieces on the board for visualization purposes
        self.board_state[3, 3:6] = 1
        self.board_state[4:6, 4] = 1

        # Setup Canvas
        canvas_width = self.cols * self.cell_size
        canvas_height = self.rows * self.cell_size
        self.canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="#1e1e24")
        self.canvas.pack(padx=20, pady=20)
        
        # Bind interactions
        self.canvas.bind("<Button-1>", self.handle_click)
        
        # Initial draw
        self.draw_board()

    def draw_board(self):
        """Clears and re-renders the 8x8 grid based on the underlying matrix."""
        self.canvas.delete("all")
        
        for r in range(self.rows):
            for c in range(self.cols):
                # Calculate screen coordinates for the cell
                x1 = c * self.cell_size
                y1 = r * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                
                # Color code based on cell state
                if self.board_state[r, c] == 1:
                    fill_color = "#4a90e2"  # Placed block color
                    outline_color = "#ffffff"
                else:
                    fill_color = "#2c2c35"  # Empty slot color
                    outline_color = "#3f3f4a"
                
                self.canvas.create_rectangle(
                    x1, y1, x2, y2, 
                    fill=fill_color, 
                    outline=outline_color, 
                    width=1
                )

    def handle_click(self, event):
        """Converts raw screen pixel coordinates back into integer [row, column] metrics."""
        col = event.x // self.cell_size
        row = event.y // self.cell_size
        
        # Direct structural check to keep coordinates bounded within 0-7
        if 0 <= row < self.rows and 0 <= col < self.cols:
            print(f"Clicked Matrix Position: [Row {row}, Column {col}]")
            
            # Simple toggle action to demonstrate real-time array updates
            self.board_state[row, col] = 1 if self.board_state[row, col] == 0 else 0
            self.draw_board()

if __name__ == "__main__":
    root = tk.Tk()
    app = BlockPuzzleGUI(root)
    root.mainloop()

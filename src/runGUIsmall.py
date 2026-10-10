import tkinter as tk
import numpy as np
import src.board as bo
import src.block as bl
from config import BOARD_SIZE
small_blocks = [0, 6, 7, 11, 12, 13, 14, 15]

class BlockPuzzleGUI:
    def __init__(self, root, headless):
        self.root = root
        self.is_headless = headless #should be boolean TODO: if clickable == false, don't handle clicks
        self.root.title("Block Puzzle")
        
        # Grid parameters
        self.rows = BOARD_SIZE
        self.cols = BOARD_SIZE
        self.cell_size = 120  # Pixels per grid square
        self.tray_height = 100
        self.preview_cell_size = 15
        
        self.board = bo.Board(np.zeros((self.rows, self.cols), dtype=int))
        self.blocks = [bl.Block(small_blocks[np.random.randint(len(small_blocks)-1)]) for _ in range(3)] 
        self.selected_block = None
        self.score = 0
        self.game_over = False
        

        # Setup Canvas
        canvas_width = self.cols * self.cell_size
        canvas_height = self.rows * self.cell_size + self.tray_height
        self.canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="#F15CEC")
        self.canvas.pack(padx=20, pady=20)
        self.status_text = tk.StringVar(value="Score: 0 | Select a block below.")
        status_bar = tk.Frame(root)
        status_bar.pack(fill=tk.X, padx=20, pady=(0, 12))
        tk.Label(status_bar, textvariable=self.status_text, anchor="w").pack(
            side=tk.LEFT, fill=tk.X, expand=True
        )
        tk.Button(status_bar, text="Reset", command=self.reset_game).pack(side=tk.RIGHT)
        
        # Bind interactions
        self.canvas.bind("<Button-1>", self.handle_click)
        
        # Initial draw
        self.draw_board()

    def draw_board(self):
        """Clears and re-renders the board and block tray."""
        self.canvas.delete("all")
        
        for r in range(self.rows):
            for c in range(self.cols):
                # Calculate screen coordinates for the cell
                x1 = c * self.cell_size
                y1 = r * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                
                # Color code based on cell state
                if self.board.board[r, c] == 1:
                    fill_color = "#6b20b5"  # Placed block color
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

        self.draw_block_tray()

    def draw_block_tray(self):
        board_height = self.rows * self.cell_size
        canvas_width = self.cols * self.cell_size
        self.canvas.create_rectangle(
            0,
            board_height,
            canvas_width,
            board_height + self.tray_height,
            fill="#3575b5",
            outline="",
        )
        self.canvas.create_line(
            0,
            board_height,
            canvas_width,
            board_height,
            fill="#ffffff",
            width=2,
        )

        blocks = self.blocks
        slot_width = canvas_width / len(blocks)
        label_height = 25
        for index, block in enumerate(blocks):
            slot_left = slot_width * index
            if self.selected_block == index:
                self.canvas.create_rectangle(
                    slot_left + 4,
                    board_height + 4,
                    slot_left + slot_width - 4,
                    board_height + self.tray_height - 4,
                    outline="#ffd54a",
                    width=3,
                )

            center_x = slot_width * (index + 0.5)
            self.canvas.create_text(
                center_x,
                board_height + 16,
                text=f"BLOCK {index + 1}" if block is not None else "USED",
                fill="#ffffff",
                font=("TkDefaultFont", 10, "bold"),
            )

            if block is None:
                continue

            shape_height, shape_width = block.arr.shape
            shape_x = center_x - shape_width * self.preview_cell_size / 2
            shape_y = board_height + label_height + (
                self.tray_height - label_height - shape_height * self.preview_cell_size
            ) / 2
            for row in range(shape_height):
                for col in range(shape_width):
                    if block.arr[row, col]:
                        x1 = shape_x + col * self.preview_cell_size
                        y1 = shape_y + row * self.preview_cell_size
                        self.canvas.create_rectangle(
                            x1,
                            y1,
                            x1 + self.preview_cell_size,
                            y1 + self.preview_cell_size,
                            fill="#6b20b5",
                            outline="#ffffff",
                            width=1,
                        )

    def handle_click(self, event):
        """Selects a tray block or places it at a board cell."""
        if self.game_over:
            return

        board_height = self.rows * self.cell_size
        canvas_width = self.cols * self.cell_size
        if board_height <= event.y < board_height + self.tray_height:
            if 0 <= event.x < canvas_width:
                block_index = int(event.x // (canvas_width / len(self.blocks)))
                self.select_block(block_index)
            return

        col = event.x // self.cell_size
        row = event.y // self.cell_size

        if 0 <= row < self.rows and 0 <= col < self.cols:
            if self.selected_block is None:
                self.set_status("Select a block below first.")
                return

            block = self.blocks[self.selected_block]
            if not self.board.add_block(block, (row, col)):
                self.set_status("That placement is invalid. Choose another cell.")
                return

            self.blocks[self.selected_block] = None
            self.selected_block = None
            self.score += self.board.update_board()
            self.check_block_pool()
            self.game_over = self.check_game_over()
            if self.game_over:
                self.set_status("Game over.")
            else:
                self.set_status("Block placed. Select another block.")
            self.draw_board()

    def select_block(self, block_index):
        if self.blocks[block_index] is None:
            self.selected_block = None
            self.set_status(f"Block {block_index + 1} has already been used.")
        elif self.selected_block == block_index:
            self.selected_block = None
            self.set_status("Block selection cleared.")
        else:
            self.selected_block = block_index
            self.set_status(f"Block {block_index + 1} selected. Click a board cell to place it.")
        self.draw_board()

    def check_block_pool(self):
        if all(block is None for block in self.blocks):
            self.blocks = [bl.Block(small_blocks[np.random.randint(len(small_blocks)-1)]) for _ in range(3)] 
    def check_game_over(self):
        return not any(
            block is not None and self.board.check_block_placeability(block)
            for block in self.blocks
        )

    def reset_game(self):
        self.board = bo.Board(np.zeros((self.rows, self.cols), dtype=int))
        self.blocks = [bl.Block(small_blocks[np.random.randint(len(small_blocks)-1)]) for _ in range(3)]
        self.selected_block = None
        self.score = 0
        self.game_over = False
        self.set_status("Select a block below.")
        self.draw_board()

    def set_status(self, message):
        self.status_text.set(f"Score: {self.score} | {message}")

def runGUISmallMode():
    root = tk.Tk()
    app = BlockPuzzleGUI(root, True)
    root.mainloop()

if __name__ == "__main__":
    runGUISmallMode()

import tkinter as tk
import random
import time

class SudokuApp:
    def __init__(self, master):
        self.master = master
        self.difficulty = "easy"
        self.grid = [[0 for _ in range(9)] for _ in range(9)]
        self.initial_grid = [[0 for _ in range(9)] for _ in range(9)]
        self.create_widgets()
        self."Sudoku" \
             "generate_puzzle()
        self.update_board()
        self.start_time = None
        self.elapsed_time = 0
        self.timer_label = tk.Label(master, text="00:00", font=("Helvetica", 16))
        self.timer_label.grid(row=9, column=0, columnspan=3, padx=5, pady=5)
        self.timer_running = False
        self.master.bind("<Button-1>", self.on_click)
        self.master.bind("<Key>", self.on_key_press)

    def create_widgets(self):
        self.canvas = tk.Canvas(self.master, width=450, height=450)
        self.canvas.grid(row=0, column=0, rowspan=9, padx=5, pady=5)
        for i in range(10):
            width = 3 if i % 3 == 0 else 1
            self.canvas.create_line(i * 50, 0, i * 50, 450, width=width)
            self.canvas.create_line(0, i * 50, 450, i * 50, width=width)
        self.buttons_frame = tk.Frame(self.master)
        self.buttons_frame.grid(row=0, column=1, sticky="N", padx=5, pady=5)
        self.new_game_button = tk.Button(self.buttons_frame, text="New Game", command=self.new_game)
        self.new_game_button.pack(fill="x", padx=5, pady=5)
        self.difficulty_label = tk.Label(self.buttons_frame, text="Difficulty:", font=("Helvetica", 12))
        self.difficulty_label.pack(side="top", padx=5, pady=5)
        self.easy_button = tk.Button(self.buttons_frame, text="Easy", command=lambda: self.set_difficulty("easy"))
        self.easy_button.pack(fill="x", padx=5, pady=2)
        self.medium_button = tk.Button(self.buttons_frame, text="Medium", command=lambda: self.set_difficulty("medium"))
        self.medium_button.pack(fill="x", padx=5, pady=2)
        self.hard_button = tk.Button(self.buttons_frame, text="Hard", command=lambda: self.set_difficulty("hard"))
        self.hard_button.pack(fill="x", padx=5, pady=2)
        self.solve_button = tk.Button(self.buttons_frame, text="Show Solution", command=self.show_solution)
        self.solve_button.pack(fill="x", padx=5, pady=5)
        self.message_label = tk.Label(self.buttons_frame, text="", font=("Helvetica", 12))
        self.message_label.pack(fill="x", padx=5, pady=5)

    def set_difficulty(self, difficulty):
        self.difficulty = difficulty
        self.new_game()

    def new_game(self):
        self.generate_puzzle()
        self.update_board()
        self.message_label.configure(text="")
        if self.timer_running:
            self.reset_timer()
        self.start_time = time.time()

    def show_solution(self):
        self.grid = self.solve_helper(copy.deepcopy(self.grid))
        self.update_board()

    def update_board(self):
        self.canvas.delete("numbers")
        for i in range(9):
            for j in range(9):
                x = j * 50 +
                y = i * 50
                number = self.grid[i][j]
                if number != 0:
                    self.canvas.create_text(x + 25, y + 25, text=str(number), tags="numbers",
                                            font=("Helvetica", 20, "bold"))
            for i in range(9):
                for j in range(9):
                    x = j * 50 + 20
                    y = i * 50 + 20
                    number = self.initial_grid[i][j]
                    if number != 0:
                        self.canvas.create_text(x, y, text=str(number), tags="numbers", font=("Helvetica", 16))

            def generate_puzzle(self):
                self.grid = [[0 for _ in range(9)] for _ in range(9)]
                self.initial_grid = [[0 for _ in range(9)] for _ in range(9)]
                self.generate_solution()
                cells_to_remove = {"easy": 30, "medium": 40, "hard": 50}[self.difficulty]
                cells_removed = 0
                while cells_removed < cells_to_remove:
                    row = random.randint(0, 8)
                    col = random.randint(0, 8)
                    if self.grid[row][col] != 0:
                        self.grid[row][col] = 0
                        cells_removed += 1
                self.initial_grid = copy.deepcopy(self.grid)

            def generate_solution(self):
                self.solve_helper(self.grid)

            def solve_helper(self, board):
                for i in range(9):
                    for j in range(9):
                        if board[i][j] == 0:
                            for k in range(1, 10):
                                if self.is_valid(board, i, j, k):
                                    board[i][j] = k
                                    if self.solve_helper(board):
                                        return board
                                    board[i][j] = 0
                            return False
                return board

            def is_valid(self, board, row, col, num):
                for i in range(9):
                    if board[row][i] == num:
                        return False
                    if board[i][col] == num:
                        return False
                    if board[row // 3 * 3 + i // 3][col // 3 * 3 + i % 3] == num:
                        return False
                return True

            def on_click(self, event):
                if not self.timer_running:
                    self.start_timer()
                x = event.x // 50
                y = event.y // 50
                self.canvas.delete("highlight")
                self.canvas.create_rectangle(x * 50, y * 50, x * 50 + 50, y * 50 + 50, fill="#ADD8E6", tags="highlight")

            def on_key_press(self, event):
                if not self.timer_running:
                    self.start_timer()
                if event.char.isdigit():
                    x, y = self.get_highlighted_cell()
                    if self.initial_grid[y][x] == 0:
                        self.grid[y][x] = int(event.char)
                        self.update_board()
                        if self.is_solved():
                            self.game_over()

            def start_timer(self):
                self.timer_running = True
                self.start_time = time.time()
                self.tick()

            def tick(self):
                if self.timer_running:
                    self.elapsed_time = int(time.time() - self.start_time)
                    minutes = self.elapsed_time // 60
                    seconds = self.elapsed_time % 60
                    self.timer_label.configure(text=f"{minutes:02d}:{seconds:02d}")
                    self.master.after(1000, self.tick)

            def reset_timer(self):
                self.timer_running = False
                self.elapsed_time = 0
                self.timer_label.configure(text="00:00")

            def get_highlighted_cell(self):
                items = self.canvas.find_withtag("highlight")
                x = self.canvas.coords(items[0])[0] // 50
                y = self.canvas.coords(items[0])[1] // 50
                return x, y

            def is_solved(self):
                for row in self.grid:
                    if 0 in row:
                        return False
                for i in range(9):
                    if not self.is_valid(self.grid, i, i, self.grid[i][i]):
                        return False
                return True

            def game_over(self):
                self.timer_running = False
                message = f"Congratulations! You solved the puzzle in {self.elapsed_time // 60:02d}:{self.elapsed_time % 60:02d}!"
                messagebox.showinfo("Game Over", message)

            def solve_puzzle(self):
                self.grid = copy.deepcopy(self.solution)
                self.initial_grid = copy.deepcopy(self.solution)
                self.update_board()

            def new_game(self):
                self.generate_puzzle()
                self.update_board()
                self.reset_timer()

            def set_difficulty(self, difficulty):
                self.difficulty = difficulty
                self.new_game()

            def create_menu(self):
                menubar = tk.Menu(self.master)
                difficulty_menu = tk.Menu(menubar, tearoff=0)
                difficulty_menu.add_command(label="Easy", command=lambda: self.set_difficulty("easy"))
                difficulty_menu.add_command(label="Medium", command=lambda: self.set_difficulty("medium"))
                difficulty_menu.add_command(label="Hard", command=lambda: self.set_difficulty("hard"))
                menubar.add_cascade(label="Difficulty", menu=difficulty_menu)
                self.master.config(menu=menubar)

            if __name__ == '__main__':
                root = tk.Tk()
                SudokuGame(root)
                root.mainloop()
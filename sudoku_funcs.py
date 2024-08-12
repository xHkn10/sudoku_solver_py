import tkinter.messagebox
import time
import customtkinter as ctk
from pythonProject.sudoku import SudokuSolver

entry_list = [[None for _ in range(9)] for _ in range(9)]
t0 = 0


class SudokuFuncs:

    @staticmethod
    def clear():
        for y in range(9):
            for x in range(9):
                entry_list[y][x].delete(0, "end")

    @staticmethod
    def solve_sudoku():
        sudoku_board = [[0 for _ in range(9)] for _ in range(9)]
        for y in range(9):
            for x in range(9):
                entry_val = entry_list[y][x].get().strip()
                if entry_val.isdigit():
                    sudoku_board[y][x] = int(entry_val)
                else:
                    sudoku_board[y][x] = 0
        if not SudokuSolver.valid(sudoku_board):
            tkinter.messagebox.showerror("Invalid sudoku", "Please enter a valid sudoku")
            SudokuFuncs.clear()
            return
        try:
            global t0
            t0 = time.time()
            SudokuSolver.solver(sudoku_board)
        except SudokuSolver.TerminateRecursion:
            SudokuFuncs.clear()
            for y in range(9):
                for x in range(9):
                    entry_list[y][x].insert(0, sudoku_board[y][x])
        except SudokuSolver.UnsolvableSudoku:
            SudokuFuncs.clear()
            tkinter.messagebox.showerror("Unsolvable sudoku", "No solutions exist to the current sudoku.")
        finally:
            if not SudokuSolver.full(sudoku_board):
                tkinter.messagebox.showerror("Unsolvable sudoku", "No solutions exist to the current sudoku.")

    @staticmethod
    def open_solver(main_frame: ctk.CTkFrame,
                    solver_frame: ctk.CTkFrame,
                    solver_canvas: ctk.CTkCanvas,
                    solve_button: ctk.CTkButton,
                    clear_button: ctk.CTkButton):

        global entry_list

        main_frame.pack_forget()
        solver_frame.pack(pady=50, anchor="s")
        solver_canvas.grid()

        for i in range(9):
            solver_canvas.grid_rowconfigure(i, weight=0, minsize=40)
            solver_canvas.grid_columnconfigure(i, weight=0, minsize=40)
        for y in range(9):
            for x in range(9):
                entry = ctk.CTkEntry(master=solver_canvas, width=30, height=30)
                entry.bind("<KeyPress>", command=lambda event, y=y, x=x: SudokuFuncs.navigate(y, x, event))
                entry_list[y][x] = entry
                entry.grid(row=y, column=x, padx=0, pady=0)

        solve_button.pack()
        clear_button.pack()

    @staticmethod
    def navigate(y, x, event):
        if y != 0 and event.keysym == "Up":
            entry_list[y - 1][x].focus_set()

        elif y != 8 and event.keysym == "Down":
            entry_list[y + 1][x].focus_set()

        elif x != 0 and event.keysym == "Left":
            entry_list[y][x - 1].focus_set()

        elif x != 8 and event.keysym == "Right":
            entry_list[y][x + 1].focus_set()

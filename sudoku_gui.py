import customtkinter as ctk
from pythonProject import sudoku_funcs


class SudokuGUI(ctk.CTk):
    root = None
    main_frame = None
    main_screen_buttons_frame = None
    solver_frame = None
    solver_canvas = None
    SDK_label = None
    open_sudoku_solver_button = None
    solve_button = None
    clear_button = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.root = self
        self.title("Sudoku")
        self.geometry("500x500")

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self.main_frame = ctk.CTkFrame(master=self, corner_radius=32)
        self.main_frame.pack(pady=10, padx=10, fill="both", expand=True)

        self.SDK_label = ctk.CTkLabel(master=self.main_frame, text="SUDOKU", font=("Ink Free", 56, "bold"))
        self.SDK_label.pack(pady=50)

        self.main_screen_buttons_frame = ctk.CTkFrame(master=self.main_frame, width=50, height=100,
                                                      fg_color="#262928", corner_radius=32)
        self.main_screen_buttons_frame.pack(pady=40)

        self.solver_frame = ctk.CTkFrame(master=self)

        self.solver_canvas = ctk.CTkCanvas(master=self.solver_frame, bg="gray")
        self.solver_canvas.create_line(0, 120, 400, 120, fill="black", width=5)
        self.solver_canvas.create_line(0, 240, 400, 240, fill="black", width=5)
        self.solver_canvas.create_line(120, 0, 120, 400, fill="black", width=5)
        self.solver_canvas.create_line(240, 0, 240, 400, fill="black", width=5)

        self.open_sudoku_solver_button = ctk.CTkButton(master=self.main_screen_buttons_frame,
                                                       text="SUDOKU SOLVER",
                                                       font=("Ink Free", 27, "bold"),
                                                       command=lambda: sudoku_funcs.SudokuFuncs.open_solver(
                                                           self.main_frame,
                                                           self.solver_frame,
                                                           self.solver_canvas,
                                                           self.solve_button,
                                                           self.clear_button),
                                                       width=100, height=50, corner_radius=32)
        self.open_sudoku_solver_button.pack(pady=30)

        self.solve_button = ctk.CTkButton(master=self, text="Solve!", font=("Ink Free", 27),
                                          command=sudoku_funcs.SudokuFuncs.solve_sudoku,
                                          width=70, height=35, corner_radius=32)

        self.clear_button = ctk.CTkButton(master=self, text="Clear", font=("Ink Free", 27),
                                          command=sudoku_funcs.SudokuFuncs.clear,
                                          width=70, height=35, corner_radius=32)

        self.mainloop()


def main() -> None:
    SudokuGUI()


if __name__ == '__main__':
    main()

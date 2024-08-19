# sudoku_solver_py
Sudoku solver in Python, with a CustomTkinter GUI.

The Sudoku solver algorithm uses backtracking to explore possible combinations through brute force and stops when it either finds a solution or determines that no solution is possible. When all cells are filled, this indicates that a solution has been found, and we raise a TerminateRecursion exception to stop the recursion. If we backtrack to the initial stage or if 1 second passes, it means no solution exists for the given Sudoku puzzle. We shuffle the range(1,10) iterator to explore other possible solutions because, without shuffling, we always get the same answer.

pip install customtkinter if you don't have and run the main function located in Sudoku_GUI

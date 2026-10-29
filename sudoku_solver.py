def print_grid(grid):
    for row in grid:
        print(" ".join(map(str, row)))


def is_valid(grid, row, col, num):
    # Check row
    for j in range(9):
        if grid[row][j] == num:
            return False

    # Check column
    for i in range(9):
        if grid[i][col] == num:
            return False

    # Check 3x3 subgrid
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if grid[i][j] == num:
                return False

    return True


def solve_sudoku(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(grid, row, col, num):
                        grid[row][col] = num

                        if solve_sudoku(grid):
                            return True

                        # Backtrack
                        grid[row][col] = 0

                return False

    return True


def valid_initial_grid(grid):
    for row in range(9):
        for col in range(9):
            num = grid[row][col]

            if num < 0 or num > 9:
                return False

            if num != 0:
                grid[row][col] = 0
                valid = is_valid(grid, row, col, num)
                grid[row][col] = num

                if not valid:
                    return False

    return True


print("Enter Sudoku row by row (use 0 for empty cells).")
grid = []

try:
    for i in range(9):
        row = list(map(int, input(f"Row {i + 1}: ").split()))

        if len(row) != 9:
            raise ValueError("Enter exactly 9 numbers per row.")

        grid.append(row)

    if not valid_initial_grid(grid):
        print("Invalid Sudoku grid.")
    else:
        print("\nOriginal Sudoku:")
        print_grid(grid)

        if solve_sudoku(grid):
            print("\nSolved Sudoku:")
            print_grid(grid)
        else:
            print("No solution exists.")

except ValueError as error:
    print("Invalid input:", error)
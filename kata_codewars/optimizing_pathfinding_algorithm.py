def get_number_of_reachable_fields(grid, rows, columns, start_row, start_column):
    # Your magic here...
    for g in grid:
        print(g) 
    
    #create grid
    gameboard = [[0 for x in range(rows)] for y in range(columns)]
    # Draw board - Blocked
    for r in range(rows):
        for c in range(columns):
            gameboard[r][c] = '-'
            if r == start_row and c == start_column:
                gameboard[r][c] = "PL"
            elif grid[r][c] == 0:
                gameboard[r][c] = "B"

    for g in gameboard:
        print(g) 
    return gameboard
    #try to move left or right

grid = [[1,1,1],
        [0,0,1],
        [0,1,0]]
get_number_of_reachable_fields(grid, 3, 3, 0, 0)


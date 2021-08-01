# solving Sudoku puzzle ver.01-210802
# assume there exists only one solution

import copy

## variables
SIZE = 9
grid = []
history = []

## classes & functions
def loadData() : # 0 means empty
    testgrid = \
    [ 
        [0, 0, 0, 7, 5, 0, 0, 3, 0],
        [1, 0, 6, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 3, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 6, 0, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 4, 0, 0, 9, 0, 0, 0, 0],
        [3, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
    ]
    return testgrid

def findNext(grid) : # grid가 실수로 변경되지 않길 원해서 global로 선언 x
    global SIZE
    for i in range(SIZE) :
        for j in range(SIZE) :
            if grid[i][j] == 0 :
                return i, j

def possibleNumbers(row, column, grid) : # grid가 실수로 변경되지 않길 원해서 global로 선언 x
    # search numbers of the same row, column, and subgrid
    global SIZE
    pos_nums = [num for num in range(1, SIZE + 1)] # SIZE == the num of possible nums
    for j in range(SIZE) : # search numbers of the same row
        if grid[row][j] in pos_nums :
            pos_nums.remove(grid[row][j])
    for i in range(SIZE) : # search numbers of the same column
        if grid[i][column] in pos_nums :
            pos_nums.remove(grid[i][column])
    for i in range(SIZE**(1/2)) :     # search numbers of the same subgrid.
        for j in range(SIZE**(1/2)) : # size of subgrids == SIZE**(1/2)
            num_subgrid = grid[(row//3)*3 + i][(row//3)*3 + j]
            if num_subgrid in pos_nums : # (row//3)*3 == first index of the subgrid
                pos_nums.remove(num_subgrid)
    return pos_nums

def isComplete() :
    for i in range(SIZE) :
        for j in range(SIZE) :
            if grid[i][j] == 0 :
                return False
    return True


def findSolution() :
    global grid, history, solution
        
    if isComplete():
        solution = copy.deepcopy(grid)
        return # now, global variable 'grid' is the unique solution

    i, j = findNext() # find next (first) empty position
    
    if possibleNumbers(i, j, grid) :
        for num in possibleNumbers(i, j, grid) :
            grid[i][j] = num
            history.append((i, j, num))
            findSolution()
            cellData = history.pop() # cellData has (i, j, num) form. (position data i, j) & (a number filled in the cell)
            grid[cellData[0], cellData[1]] = 0
            return
    elif not possibleNumbers(i, j, grid):
        


## main

def main() :
    grid = loadData()
    
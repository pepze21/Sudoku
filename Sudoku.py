# solving Sudoku puzzle ver.04-210805
# assume there exists only one solution

import copy

## variables
SIZE = 9
SIZE_OF_SUBGRIDS = 3 # == SIZE**(1/2)
grid = [] # [[None for _ in range(SIZE)] for _ in range(SIZE)] 을 선언?
history = []
solutions = []

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
    global SIZE, SIZE_OF_SUBGRIDS
    pos_nums = [num for num in range(1, SIZE + 1)] # SIZE == the num of possible nums
    for j in range(SIZE) : # search numbers in the same row
        if grid[row][j] in pos_nums :
            pos_nums.remove(grid[row][j])
    for i in range(SIZE) : # search numbers in the same column
        if grid[i][column] in pos_nums :
            pos_nums.remove(grid[i][column])
    for i in range(SIZE_OF_SUBGRIDS) :     # search numbers in the same subgrid
        for j in range(SIZE_OF_SUBGRIDS) :
            num_subgrid = grid[(row//SIZE_OF_SUBGRIDS)*SIZE_OF_SUBGRIDS + i]\
                              [(row//SIZE_OF_SUBGRIDS)*SIZE_OF_SUBGRIDS + j]
            if num_subgrid in pos_nums : # (row//3)*3 == first index of the subgrid
                pos_nums.remove(num_subgrid)
    print("pos_nums :", pos_nums)
    return pos_nums

def isComplete(grid) : # grid가 실수로 변경되지 않길 원해서 global로 선언 x
    global SIZE
    for i in range(SIZE) :
        for j in range(SIZE) :
            if grid[i][j] == 0 :
                return False
    return True


def findSolution() : # we'll find only one solution.(b/o uniqueness of solutions)
    global grid, history, solutions

    while True :
        if isComplete(grid):
            solutions.append(copy.deepcopy(grid))
            print("I got a solution")
            break # now, global variable 'grid' is the unique solution
    
        i, j = findNext(grid) # find next (first) empty position
        pos_num = copy.deepcopy(possibleNumbers(i, j, grid))
        if not pos_num :
            break 

        for num in pos_num :
            grid[i][j] = num
            history.append((i, j, num))
            print(grid)
            findSolution()
            cellData = history.pop() # cellData has (i, j, num) form. (position data i, j) & (a number filled in the cell)
            grid[cellData[0]][cellData[1]] = 0
        

    
def main() :
    global grid, solution
    grid = loadData()
    findSolution()
    for solution in solutions :
        print("solution :", solution)


## main

if __name__ == "__main__" :
    main()
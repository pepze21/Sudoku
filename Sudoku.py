# solving Sudoku puzzle ver.08-210809, 코드를 깔끔하게 정리
# assume there exists only one solution  - but there could be many solutions in the testgrid !!!!

import copy

## global variables
SIZE = 9
SIZE_OF_SUBGRIDS = 3
grid = []
history = []
solutions = []

## functions
def loadData(): # 0 means empty
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

def findNext(grid):
    global SIZE
    for i in range(SIZE):
        for j in range(SIZE):
            if grid[i][j] == 0:
                return i, j

def possibleNumbers(row, column, grid):
    # search numbers of the same row, column, and subgrid
    global SIZE, SIZE_OF_SUBGRIDS
    pos_nums = [num for num in range(1, SIZE + 1)]
    for j in range(SIZE): # search in the same row
        if grid[row][j] in pos_nums:
            pos_nums.remove(grid[row][j])
    for i in range(SIZE): # search in the same column
        if grid[i][column] in pos_nums:
            pos_nums.remove(grid[i][column])
    for i in range(SIZE_OF_SUBGRIDS): # search in the same subgrid
        for j in range(SIZE_OF_SUBGRIDS):
            num_subgrid = \
            grid[(row//SIZE_OF_SUBGRIDS)*SIZE_OF_SUBGRIDS + i]\
                [(column//SIZE_OF_SUBGRIDS)*SIZE_OF_SUBGRIDS + j]
            if num_subgrid in pos_nums:
                pos_nums.remove(num_subgrid)
    return pos_nums

def isComplete(grid):
    global SIZE
    for i in range(SIZE):
        for j in range(SIZE):
            if grid[i][j] == 0:
                return False
    return True


def findSolution(): # we'll find only one solution.
    global grid, history, solutions

    if isComplete(grid):
        solutions.append(copy.deepcopy(grid))
        print("I got a solution")
        return

    i, j = findNext(grid)
   
    for num in possibleNumbers(i, j, grid):
        grid[i][j] = num
        history.append((i, j, num))
        findSolution()
        cellData = history.pop()
        grid[cellData[0]][cellData[1]] = 0
        
def isReallyComplete(solution):
    sum = 0

    for i in range(SIZE): # row test
        sum = 0
        for j in range(SIZE):
            sum += solution[i][j]
        if sum != 45:
            print("%dth row is not complete" %i)
            return False

    for j in range(SIZE): # column test
        sum = 0
        for i in range(SIZE):
            sum += solution[i][j]
        if sum != 45:
            print("%dth column is not complete" %j)
            return False

    for k in range(SIZE_OF_SUBGRIDS): # subgrid test.
        for l in range(SIZE_OF_SUBGRIDS):
            sum = 0
            for i in range(SIZE_OF_SUBGRIDS):
                for j in range(SIZE_OF_SUBGRIDS):
                    sum += solution[SIZE_OF_SUBGRIDS*k + i]\
                                   [SIZE_OF_SUBGRIDS*l + j]
            if sum != 45 :
                print("(%d, %d)th subgrid is not complete" %(i, j))
                return False

    sum = 0 # total sum test
    for i in range(SIZE):
        for j in range(SIZE):
            sum += solution[i][j]
    if sum != 405:
        print("total sum of the grid is not 405")
        return False
    
    print("this solution has passed 'row', 'column', 'subgrid', 'total sum' tests.")
    print("thus it is really complete")
    return True

def main():
    global grid, solutions
    grid = loadData()
    findSolution()
    for solution in solutions:
        print("solution :")
        for i in range(len(solution)):
            print(solution[i])
        isReallyComplete(solution)

## main

if __name__ == "__main__" :
    main()
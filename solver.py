board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]
'''
1. pick empty
2. try a number
3. find one that works
4. repeat
5. backtrack
'''

def solve(bo):
    """
    Solves a sudoku board using backtracking
    :param bo: 2d list of ints
    :return: solution
    """
    find = find_empty(bo)
    if find:
        row, col = find
    else:
        return True

    for i in range(1,10):
        if valid(bo, (row, col), i):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def valid(bo, pos, num):
    # check row
    for i in range(len(bo)):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
    # check col
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[1] != i:
            return False
    
    # check box, [0,0], [0, 1 ], [0, 2], [1, 0 ]
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(3*box_y, 3*box_y + 3):
        for j in range(3*box_x, 3*box_x + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False
    return True

def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("---------------------------")
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end = "")
            if j == 8:
                print(str(bo[i][j]))
            else:
                print(str(bo[i][j]) + " ", end="")

'''
return position of the board
'''
def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[i])):
            if bo[i][j] == 0:  
                return (i, j) # row, col
    return None
    
print("before: \n")
print_board(board)
print("************************************")
print("after: \n")
solve(board)
print_board(board)
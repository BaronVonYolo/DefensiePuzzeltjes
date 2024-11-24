import numpy as np
import sys
import time

# 90 degree rotation matrices
X_ROTATION_PLUS = np.matrix('1 0 0; 0 0 1; 0 -1 0')
Y_ROTATION_PLUS = np.matrix('0 0 -1; 0 1 0; 1 0 0')

X_ROTATION_MIN = np.matrix('1 0 0; 0 0 -1; 0 1 0')
Y_ROTATION_MIN = np.matrix('0 0 1; 0 1 0; -1 0 0')

# Path needs to end in one of these
END_POS = [(2, 1), (0, 1), (0, 5), (2, 5), (3, 4), (3, 2)]

WIDTH = 8
HEIGHT = 8

# Global count to keep track of total number of recursive calls
count = 0

class Die:

    def __init__(self):
        self.orientation = np.matrix('1 0 0; 0 1 0; 0 0 1')
        self.nums = [[5, 2], [3, 4], [1, 6]]

    def get_number(self):
        for i in range(0, 3):
            if self.orientation[2, i] != 0:
                return self.nums[i][max(0, self.orientation[2, i])]
        return None

    def rotate_right(self):
        self.orientation = np.matmul(X_ROTATION_PLUS, self.orientation)

    def rotate_left(self):
        self.orientation = np.matmul(X_ROTATION_MIN, self.orientation)

    def rotate_up(self):
        self.orientation = np.matmul(Y_ROTATION_PLUS, self.orientation)

    def rotate_down(self):
        self.orientation = np.matmul(Y_ROTATION_MIN, self.orientation)


# Our partial solution is only valid if we can reack all unvisited squares in one path
def check_connectivity(board):
    visited = board != 0

    # Pick the first unvisited square we find
    x, y = 0, 0

    while visited[x, y] and y < board.shape[1]:
        y += 1
        if y == board.shape[1]:
            y = 0
            x += 1

            # If there are no unvisited squares: connected by default
            if x == board.shape[0]:
                return True

    # Graph connectivity can be tested by counting nodes with depth first search
    reachedCount = dfs_count(board, x, y, visited)

    # Connected if count of unreached is equal to amount of unvisited nodes
    return reachedCount == np.sum(board == 0)

def dfs_count(board, x, y, visited):
    
    # This node has been counted already
    if visited[x, y]:
        return 0
    
    visited[x, y] = True
    
    # Count this square as a free square
    freeSquareCount = 1
    
    # Check paths of all neighbours (Check visited here to prevent another function call overhead)
    if x < board.shape[1] - 1 and not visited[x+1, y]:
        freeSquareCount += dfs_count(board, x+1, y, visited)   
    if y < board.shape[0] - 1 and not visited[x, y+1]:
        freeSquareCount += dfs_count(board, x, y+1, visited)
    if x > 0 and not visited[x-1, y]:
        freeSquareCount += dfs_count(board, x-1, y, visited)
    if y > 0 and not visited[x, y-1]:
        freeSquareCount += dfs_count(board, x, y-1, visited) 

    return freeSquareCount

# Function to check if an x, y coordinate is one of the allowed end points
def is_end_point(x, y):
    for end_x, end_y in END_POS:
        if end_x == x and end_y == y:
            return True
        
    return False

# The can only be one dead end in a partial solution and that is the end point as we need to reach every part in a single path
def check_dead_ends(board, x, y):

    dead_ends = 0
    dead_end_at_current_pos = 0

    for i in range(0, board.shape[0]):
        for j in range(0, board.shape[1]):
            
            # If it is not visited, check if it is a dead end
            if board[i, j] == 0:

                open_neighbours = 0
                if i > 0 and board[i-1, j] == 0:
                    open_neighbours += 1
                if j > 0 and board[i, j-1] == 0:
                    open_neighbours += 1
                if i < board.shape[0]-1 and board[i+1, j] == 0:
                    open_neighbours += 1
                if j < board.shape[1]-1 and board[i, j+1] == 0:
                    open_neighbours += 1

                # A dead end only has one or less open neighbours
                if open_neighbours <= 1:
                    # One dead end is allowed at the current position 
                    if dead_ends < 1 and is_end_point(i, j):
                        dead_ends += 1
                    # One dead end is allowed at current dice position
                    elif dead_end_at_current_pos < 1 and ((abs(x-i) == 1) ^ (abs(y-j) == 1)):
                        dead_end_at_current_pos += 1
                    else:
                        return False
                        
    return True


def find_value(depth, x, y, board, moves, die, debug = False):

    value = die.get_number()

    # Check horse jump constraint
    if x > 0 and y > 1 and board[x-1, y-2] == value:
        return None
    if y > 0 and x > 1 and board[x-2, y-1] == value:
        return None
    if x < 7 and y > 1 and board[x+1, y-2] == value:
        return None
    if y < 7 and x > 1 and board[x-2, y+1] == value:
        return None
    if x < 6 and y > 0 and board[x+2, y-1] == value:
        return None
    if y < 6 and x > 0 and board[x-1, y+2] == value:
        return None
    if x < 6 and y < 7 and board[x+2, y+1] == value:
        return None
    if y < 6 and x < 7 and board[x+1, y+2] == value:
        return None
        
    # Add dice value to board
    board[x, y] = value

    global count
    count += 1

    if not check_connectivity(board):
        if debug:
            print('---No Connection---')
            print(count)
            print(depth)
            print(board)
        board[x, y] = 0
        return None
    
    if not check_dead_ends(board, x, y):
        if debug:
            print(f'---Dead end {x} {y} ---')
            print(count)
            print(depth)
            print(board)
        board[x, y] = 0
        return None

    if count % 10000 == 0:
        print('---Update---')
        print(count)
        print(depth)
        print(board)

    # if we are done
    if depth == 64:

        if is_end_point(x, y):
            return np.sum(board)
    
        else: 
            board[x, y] = 0
            return None
    

    # Try to continue path from all neigbours
    if x < 7 and board[x+1, y] == 0:
        die.rotate_down()
        val = find_value(depth+1, x+1, y, board, moves, die, debug=debug)
        # Found solution
        if val != None:
            moves.append('down')
            return val

        # Else undo roll
        die.rotate_up()
        
    if x > 0 and board[x-1, y] == 0:
        die.rotate_up()
        val = find_value(depth+1, x-1, y, board, moves, die, debug=debug)
        
        if val != None:
            moves.append('up')
            return val

        die.rotate_down()
    
    if y > 0 and board[x, y-1] == 0:
        die.rotate_left()
        val = find_value(depth+1, x, y-1, board, moves, die, debug=debug)
        
        if val != None:
            moves.append('left')
            return val
        
        die.rotate_right()

    if y < 7 and board[x, y+1] == 0:
        die.rotate_right()
        val = find_value(depth+1, x, y+1, board, moves, die, debug=debug)
        
        if val != None:
            moves.append('right')
            return val

        die.rotate_left()
    
    # nothing returned --> nothing found
    board[x, y] = 0
    return None

if __name__ == '__main__':

    arg = sys.argv[1] if len(sys.argv) > 1 else ''

    die = Die()
    board = np.zeros(shape=[8, 8])

    move_list = []

    t1 = time.time_ns()

    print(find_value(1, 1, 3, board, move_list, die, debug=arg == 'debug'))
    
    t2 = time.time_ns()
    
    print(f'Oplossing gevonden in {(t2-t1) / 1000000000:.2f}s')

    # Moves get added in reverse order
    print(move_list[-1::-1])
    print(board)
        

# 0 is a valid space
# 9 is a wall, you cannot move past it
# 1 is the exit, your goal
# can only move left, right, up and down

# 2 test mazes for you to verify your code
'''
maze = [[9,9,9,9,9,1,9],\
        [9,9,0,9,9,0,9],\
        [9,0,0,9,9,0,9],\
        [9,0,9,0,0,0,9],\
        [9,0,0,0,9,0,9],\
        [9,9,9,9,0,0,9],\
        [9,9,9,9,9,9,9]]
'''
maze = [[9,9,1,9,9,9,9],\
        [9,9,0,9,9,0,9],\
        [9,0,0,9,9,0,9],\
        [9,0,9,0,0,0,9],\
        [9,0,0,0,9,0,9],\
        [9,9,9,9,0,0,9],\
        [9,9,9,9,9,9,9]]

NUMROWS = 7     # update these 4 constants for maze of a different size
NUMCOLUMNS = 7  
STARTX = 3      # starting column
STARTY = 3      # starting row

WALL = 9        # constants to represent the meaning of the values
EXIT = 1        
SPACE = 0        

# Your code should display something like: Exit found at 0,2

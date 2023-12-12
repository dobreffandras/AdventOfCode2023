import re

puzzle_input = open("./puzzle_input.txt", "r").read()

def parse(input):
    return [[c for c in line] for line in input.splitlines()]
    
def find_starting_position(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'S':
                return (i,j)
                
def figure_out_coming_directions_from_start(grid, S):
    i,j = S
    connection_to_north = 0 < i and (grid[i-1][j] == '|' or grid[i-1][j] == '7' or grid[i-1][j] == 'F')
    connection_to_east = j < (len(grid[i])-1) and (grid[i][j+1] == '-' or grid[i][j+1] == '7' or grid[i][j+1] == 'J')
    connection_to_south = i < (len(grid)-1) and (grid[i+1][j] == '|' or grid[i+1][j] == 'L' or grid[i+1][j] == 'J')
    connection_to_west = 0 < j and (grid[i][j-1] == '-' or grid[i][j-1] == 'L' or grid[i][j-1] == 'F')
            
    directions = []
    if connection_to_north:
        directions.append('S')
    if connection_to_east:
        directions.append('W')
    if connection_to_south:
        directions.append('N')
    if connection_to_west:
        directions.append('E')

    return directions
            
                
def find_next_pipe(grid, pos, coming_direction):
    i, j = pos
    tile = grid[i][j]
    
    match (tile, coming_direction):
        case ('|', 'N'):
            return ((i+1, j), 'N') 
        case ('|', 'S'):
            return ((i-1, j), 'S')
        case ('-', 'E'):
            return ((i, j-1), 'E')
        case ('-', 'W'):
            return ((i, j+1), 'W')
        case ('L', 'N'):
            return ((i, j+1), 'W')
        case ('L', 'E'):
            return ((i-1, j), 'S')
        case ('J', 'N'):
            return ((i, j-1), 'E')
        case ('J', 'W'):
            return ((i-1, j), 'S')
        case ('7', 'S'):
            return ((i, j-1), 'E')
        case ('7', 'W'):
            return ((i+1, j), 'N')
        case ('F', 'E'):
            return ((i+1, j), 'N')
        case ('F', 'S'):
            return ((i, j+1), 'W')
    
def from_start_with_direction(S, coming_direction):
    i, j = S
    match coming_direction:
        case 'N':
            return (i+1, j)
        case 'E':
            return (i, j-1)
        case 'S':
            return (i-1, j)
        case 'W':
            return (i, j+1)

if __name__ == "__main__":
    grid = parse(puzzle_input)
    S = find_starting_position(grid)
    D = figure_out_coming_directions_from_start(grid, S)
    step = 1
    coming_direction1 = D[0]
    coming_direction2 = D[1]
    position1 = from_start_with_direction(S, coming_direction1)
    position2 = from_start_with_direction(S, coming_direction2)
    
    while position1 != position2:
        position1, coming_direction1 = find_next_pipe(grid, position1, coming_direction1)
        position2, coming_direction2 = find_next_pipe(grid, position2, coming_direction2)
        step +=1
    print(step)
        
    
    
                
                
    
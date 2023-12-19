import re
def read(file):
    with open(file) as f:
        rawdata = f.readlines()
    return rawdata

# map made based on 90degree pipes. e.g. L is a pipe connecting north and east. So if were travelling south
# our new direction is east, and if we were travelling west originally, our direction is north. 
MAP = {
	'L': {
		'S': 'E',
		'W': 'N'
	},
	'F': {
		'N': 'E',
		'W': 'S'
	},
	'J': {
		'E': 'N',
		'S': 'W'
	},
	'7': {
		'E': 'S',
		'N': 'W'
	},
	'-': {
		'E': 'E',
		'W': 'W'
	},
	'|': {
		'N' : 'N',
		'S' : 'S'
	}
}
DIRECTION_2_COORDS = {  #y , x
	'N': [-1, 0],
	'S': [1, 0],
	'E': [0, 1],
	'W': [0, -1]
}

VIABLE_DIRECTIONS = { #if i was going north, viable directions are | F and 7
	'N': ['|', 'F', '7'],
	'S': ['|', 'J', 'L'],
	'E': ['-', 'J', '7'],
	'W': ['-', 'L', 'F']
}

OPPOSITE_DIRECTIONS =  {
	'N':'S',
	'S':'N',
	'E': 'W',
	'W': 'E'
}

def find_start(grid):
	for y in range(0, len(grid)):
		if 'S' in grid[y]:
			return grid[y].index('S'), y

def move(grid,x,y,direction):
	current_pipe = grid[y][x]
	new_dir = MAP[current_pipe][direction]
	new_coord = DIRECTION_2_COORDS[new_dir]
	new_y = y + new_coord[0]
	new_x = x + new_coord[1]
	return new_x, new_y, new_dir
	
def find_starting_path(grid,x,y):
	for dir, coord_dir in DIRECTION_2_COORDS.items():
		new_coord = [y + coord_dir[0], x+coord_dir[1]]
		pipe_at_new_coord = grid[new_coord[0]][new_coord[1]]
		if pipe_at_new_coord in VIABLE_DIRECTIONS[dir]:
			return dir, new_coord[0], new_coord[1]

def main(file):
	grid = read(file)
	xstart, ystart = find_start(grid)
	print(xstart, ystart)
	dir, y,x = find_starting_path(grid,xstart, ystart)
	print(x,y,dir)
	counter = 1
	while grid[y][x] != 'S':
		x,y,dir = move(grid, x,y,dir)
		
		print(x, y, dir)
		counter +=1
	print(counter//2)
	print(grid)



main('./10/data.txt')

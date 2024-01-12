import re
from part1 import VIABLE_DIRECTIONS, DIRECTION_2_COORDS, MAP, find_start, find_starting_path, move, read
#604 too high
#335 too low

	
def add_coord(loop_coords, x,y):
	if f'{y}' in loop_coords:
		loop_coords[f'{y}'].append(x)
	else:
		loop_coords[f'{y}'] = [x]
	return loop_coords

def fill_in_pipes(loop_coords, grid):
	for y,xs in loop_coords.items():
		for x in xs:
			grid[int(y)] = grid[int(y)][:x] + 'O' + grid[int(y)][x+1:] 
	return grid


def reformat(grid):
	for i in range(len(grid)):
		grid[i] = grid[i] + '\n'
	return grid

def visual(new_grid):
	with open('10/visualiser.txt', 'w') as f:
		grid = reformat(new_grid)
		f.writelines(grid)
	return new_grid

def check_boundary(x,y,w,h):
	
	boundary_rules = DIRECTION_2_COORDS.copy()
	if x == 0:
		del boundary_rules['W']
	elif x == w-1:
		del boundary_rules['E']
	if y ==0:
		del boundary_rules['N']
	elif y == h-1:
		del boundary_rules['S']
	
	return boundary_rules


	



def main(file):
	grid = read(file)
	
	loop_coords = {}
	xstart, ystart = find_start(grid)
	loop_coords = add_coord(loop_coords, xstart, ystart)
	dir, y,x = find_starting_path(grid,xstart, ystart)
	loop_coords = add_coord(loop_coords, x, y)
	travelling = True
	while travelling:
		x,y,dir = move(grid, x,y,dir)
		if grid[y][x] != 'S':
			loop_coords = add_coord(loop_coords, x, y)
		else:
			travelling = False
	summation = 0
	for y, xs in loop_coords.items():
		xs.sort()
		y = int(y)
		p = 1
		for i in range(1,len(xs)):
			first = grid[y][xs[i-p]]
			second = grid[y][xs][i]
			line = 


		
		



	
	
	

	



main('./10/data.txt')

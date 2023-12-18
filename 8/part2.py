import re
import math
def read(file):
    with open(file) as f:
        rawdata = f.readlines()
    return rawdata


def move(index, paths):
	next_position = re.findall('[A-Z]{3}', paths)[index + 1]
	return next_position

def main(file):
	rawdata = read(file)
	instructions, maps = rawdata[0].strip(), [line.strip() for line in rawdata[2:]]
	i = 0
	k = 1
	instruction_index = {
		'L': 0,
		'R': 1
	}
	all_current = re.findall(r'[A-Z]{2}A = \([A-Z]+, [A-Z]+\)', '\n'.join(maps))
	current = list(map(lambda pos: pos[:3], all_current))
	current_loop_length = {}
	while len(current_loop_length.items()) < 6:
		if i == len(instructions):
			i = 0
		direction = instructions[i]
		dir_index = instruction_index[direction]
		current = list(map(lambda currents: move(dir_index, currents), all_current))
		for n,c in enumerate(current):
			if c[-1] == 'Z':
				i_s = f'{n}'
				if i_s not in current_loop_length:
					current_loop_length[i_s] = k
				print(current_loop_length)
		all_current = [re.search(f'{current_pos} = \([A-Z]+, [A-Z]+\)', '\n'.join(maps)).group() for current_pos in current]
		k +=1
		i+=1
	print(math.lcm(*current_loop_length.values()))
	
main('./8/data.txt')

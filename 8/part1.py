import re
def read(file):
    with open(file) as f:
        rawdata = f.readlines()
    return rawdata

def main(file):
	rawdata = read(file)
	instructions, maps = rawdata[0].strip(), [line.strip() for line in rawdata[2:]]
	starting, ending = 'AAA', 'ZZZ'
	current = starting
	i = 0
	k = 0
	instruction_index = {
		'L': 0,
		'R': 1
	}
	while current != ending:
		if i == len(instructions):
			i = 0
		direction = instruction_index[instructions[i]]
		location = re.findall(f'{current} = \([A-Z]+, [A-Z]+\)', '\n'.join(rawdata))[0]
		available_locations = re.findall('[A-Z]+',location.split(' = ')[1])
		current = available_locations[direction]
		i+=1
		k+=1
		
	print(k)



main('./8/data.txt')

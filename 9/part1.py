import re
def read(file):
    with open(file) as f:
        rawdata = f.readlines()
    return rawdata


def main(file):
	rawdata = read(file)
	summation = 0
	for i in range(len(rawdata)):
		diff0 = False
		data_points = list(map(int, re.findall('-?\d+', rawdata[i])))
		current_diff = [data_points]
		while diff0 == False:
			new_set = []
			for p in range(1,len(data_points)):
				new_set.append(data_points[p]-data_points[p-1])
			if all([n==0 for n in new_set]):
				diff0 = True
			else:
				data_points = new_set
			current_diff.append(new_set)
		set_sum = sum(list(map(lambda sums: sums[-1], current_diff)))
		summation +=set_sum
	print(summation)


main('./9/data.txt')

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
		first_values = [data_points[0]]
		while diff0 == False:
			new_set = []
			for p in range(1,len(data_points)):
				new_set.append(data_points[p]-data_points[p-1])
			first_values.append(new_set[0])

			if all([n==0 for n in new_set]):
				diff0 = True
			else:
				data_points = new_set		
		extrapolated = 0
		for s in range(len(first_values)-2,-1,-1):
			extrapolated = first_values[s] - extrapolated
		summation += extrapolated
	print(summation)
main('./9/data.txt')

import re
def read(file):
    rawdata = []
    with open(file) as f:
        rawdata = f.readlines()

                
    return rawdata

def main(file):
    rawdata = read(file)
    seeds = [int(seed) for seed in re.findall('\d+',rawdata[0].split(':')[1])]
    print(seeds)
    maps = [[] for _ in range(7)]
    k = 0
    for i,line in enumerate(rawdata[2:]):
        if line == '\n' or i == len(rawdata) -3:
          for i in range(len(seeds)):
            for map in maps[k]:
                if seeds[i] >= map[1] and seeds[i] < map[1] + map[2]:
                    seeds[i] += (map[0] - map[1])
                    break
          k+=1
          continue
        numbers =[int(n) for n in re.findall('\d+', line)]
        if len(numbers):
            maps[k].append(numbers)
    print(min(seeds))

main('./5/data.txt')

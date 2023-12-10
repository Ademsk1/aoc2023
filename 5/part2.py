import re
def read(file):
    rawdata = []
    with open(file) as f:
        rawdata = f.readlines()     
    return rawdata

def get_seed_range(seed):
   return [
      seed[0], 
      seed[0]+seed[1]
   ]

def get_map_range(map_):
   return [
      map_[1],
      map_[1] + map_[2],
      map_[0] - map_[1]
   ]

def check_in_range(sstart,sstop, dstart,dstop):
  if (sstart >= dstart and sstart < dstop):
    if (sstop <= dstop):
      return 'Fully contained'
    else:
      return 'Partially contained on the left'
  elif (sstart < dstart and sstop >=dstart):
     if (sstop > dstop):
        return 'Partially contained in the middle'
     else:
        return 'Partially contained on the right'
  else:
     return False

def get_divisions(sstart,sstop,dstart,dstop, in_range):
  if in_range == 'Partially contained on the right':
    left_side = [sstart, dstart-sstart]
    right_side = [dstart, sstop-dstart]
    return [left_side,right_side]
  elif in_range == 'Partially contained on the left':
    left_side = [sstart, dstop-sstart]
    right_side = [dstop, sstop-dstop]
    return [left_side, right_side]
  else:
    left_side = [sstart, dstart-sstart]
    right_side = [dstop, sstop - dstop]
    middle = [dstart, dstop-dstart]
    return [left_side, middle, right_side]


def divider(seed, maps):
  sstart, sstop = get_seed_range(seed)
  for map_ in maps:
    dstart, dstop,_ = get_map_range(map_)
    in_range = check_in_range(sstart,sstop, dstart, dstop)
    if in_range == False:
      continue
    elif in_range == 'Fully contained':
      return [seed]
    else:
      return get_divisions(sstart,sstop,dstart,dstop, in_range)
  return [seed]

def map_changes(seed, maps):
  sstart, sstop = get_seed_range(seed)
  for map_ in maps:
    dstart, dstop,diff = get_map_range(map_)
    in_range = check_in_range(sstart,sstop, dstart, dstop)
    if in_range == False:
      continue
    elif in_range == 'Fully contained':
      return [seed[0]+diff, seed[1]]
  return seed
    
def mapper(seeds, maps):
  new_seeds = []
  mapped_seeds = []
  seeds.sort(key=lambda s:s[0])
  for i in range(len(seeds)):
    seed = seeds[i]
    divided_seeds = divider(seed, maps)
    new_seeds.append(divided_seeds)
  for new_seed_set in new_seeds:
     for seed in new_seed_set:
      mapped_seed = map_changes(seed, maps)
      mapped_seeds.append(mapped_seed)
  return mapped_seeds


def main(file):
    rawdata = read(file)
    rawseeds = re.findall('\d+ \d+',rawdata[0].split(':')[1])
    seeds = [list(map(int,re.findall('\d+',rawseed))) for rawseed in rawseeds]
    maps = [[] for _ in range(7)]
    k = 0
    for i,line in enumerate(rawdata[2:]):
      if line == '\n' or i == len(rawdata) -3:
        j = 0
        maps[k].sort(key=lambda m:m[1])
        seeds = mapper(seeds, maps[k])
        k+=1
        continue
      numbers =[int(n) for n in re.findall('\d+', line)]
      if len(numbers):
          maps[k].append(numbers)
    print(seeds)
main('./5/data.txt')

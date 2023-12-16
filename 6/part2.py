import re
import math
from itertools import accumulate
def read(file):
    with open(file) as f:
        rawdata = f.readlines()
    return rawdata

def reformat_data(rawdata):
    times = int(''.join(re.findall('\d+',rawdata[0])))
    distances = int(''.join(re.findall('\d+',rawdata[1])))
    data = [(times,distances)]
    return data


def main(file):
    rawdata = read(file)
    data = reformat_data(rawdata)
    multiplier = 1
    for race in data:
        durations_to_press = 0
        duration, distance_to_beat = race
        speed  = math.ceil(duration/2)
        time_left = duration - speed
        while speed * time_left  > distance_to_beat:
            durations_to_press +=1
            time_left -=1
            speed+=1
        if duration % 2:
          durations_to_press *=2
        else:
          durations_to_press = durations_to_press *2 -1
        multiplier *= durations_to_press
    print(multiplier)
main('./6/data.txt')

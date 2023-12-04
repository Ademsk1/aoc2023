import re
import time


def read(file):
    rawdata = []
    with open(file) as f:
        rawdata = f.readlines()
    return rawdata


def boundary(i, height, j, width, ib, jb):
    t = max([0, i-ib])
    b = min([height-1, i+ib])
    l = max([0, j-jb])
    r = min([width-1, j+jb])
    return [t, b, l, r]


def wider_view_analysis(wider_views):
    """
   its necessary to get a wider view than the 3x3 in order to not miss any digits. Here we get a 5x3. Then we check that only two numbers are within the cog.  d
    """
    wider_above, wider_here, wider_below = wider_views
    multiplier = 1
    counter = 0
    for row in [wider_above, wider_here, wider_below]:
        next_digits = re.search('\d+', row)
        jend = 0
        jstart = 0
        
        while next_digits:
            jstart = jend + next_digits.start()
            jend += next_digits.end()
            if jstart < 5 and jend > 2:
                multiplier *= int(next_digits.group())
                counter +=1
            next_digits = re.search('\d+', row[jend:])
    if counter == 2:
      return multiplier
    else:
        return 0


def main(file):
    rawdata = read(file)
    width = len(rawdata[0])
    height = len(rawdata)
    tstart = time.time()
    gear_ratio_sum = 0
    for i, entry in enumerate(rawdata):
        for j, value in enumerate(entry):
            if value != '*':
                continue
            t, b, wl, wr = boundary(i, height, j, width, 1, 3)
            wider_view = [
                rawdata[y][wl:wr+1] for y in [t, i, b]]
            gear_ratio_sum += wider_view_analysis(wider_view)
    print(gear_ratio_sum)
    print(time.time()-tstart)


main('./3/data.txt')

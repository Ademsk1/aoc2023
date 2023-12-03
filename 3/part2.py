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
    After checking that the gear has two numbers adjacent to it, its 
    necessary to get a wider view than the 3x3 in order to not miss any digits.
    """
    wider_above, wider_here, wider_below = wider_views
    multiplier = 1
    for row in [wider_above, wider_here, wider_below]:
        next_digits = re.search('\d+', row)
        jend = 0
        jstart = 0
        while next_digits:
            jstart = jend + next_digits.start()
            jend += next_digits.end()
            if jstart < 5 and jend > 2:
                multiplier *= int(next_digits.group())
            next_digits = re.search('\d+', row[jend:])
    return multiplier


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
            t, b, l, r = boundary(i, height, j, width, 1, 1)
            above = rawdata[t][l:r+1]
            here = rawdata[i][l:r+1]
            below = rawdata[b][l:r+1]
            total = 0
            for row in [above, here, below]:
                numbers = re.findall('\d+', row)
                total += len(numbers)
            if total != 2:
                continue
            _, _, wl, wr = boundary(i, height, j, width, 1, 3)
            wider_view = [
                rawdata[y][wl:wr+1] for y in [t, i, b]]
            gear_ratio_sum += wider_view_analysis(wider_view)
    print(gear_ratio_sum)
    print(time.time()-tstart)


main('./3/data.txt')

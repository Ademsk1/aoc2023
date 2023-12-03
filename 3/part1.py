import re


def read(file):
    rawdata = []
    with open(file) as f:
        rawdata = f.readlines()
    return rawdata


def get_surrounding_indexes(t, b, l, r):
    p = []
    for i in range(t, b+1):
        for j in range(l, r+1):
            p.append([i, j])

    return p


def boundary(i, height):
    t = max([0, i-1])
    b = min([height-1, i+1])
    return [t, b]


def main(file):
    rawdata = read(file)
    height = len(rawdata)
    s = 0
    for i, entry in enumerate(rawdata):
        j = re.search('\d+', entry)
        jend = 0
        jstart = 0
        while j:
            jstart = jend + j.start()
            jend += j.end()
            t, b = boundary(i, height)
            idxes = get_surrounding_indexes(t, b, jstart-1, jend)
            match = [re.match('[^(\.|\d|\\n)]', rawdata[idx][jdx]) != None
                     for idx, jdx in idxes]
            if any(match):
                s += int(j.group())
            j = re.search('\d+', entry[jend:])
    print(s)


if __name__ == '__main__':
    main('./3/data.txt')

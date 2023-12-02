import re


def read(file):
    rawdata = []
    with open(file) as f:
        rawdata = f.readlines()
    return rawdata


def main(file):
    rawdata = read(file)
    s = 0
    colours = ['red', 'green', 'blue']
    for entry in rawdata:
        multiplier = 1
        for colour in colours:
            max_colour = max([int(c)
                             for c in re.findall(f'\d+(?= {colour})', entry)])
            multiplier *= max_colour
        s += multiplier
    print(s)


main('data.txt')

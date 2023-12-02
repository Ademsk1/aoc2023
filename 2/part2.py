import re


def read(file):
    rawdata = []
    with open(file) as f:
        rawdata = f.readlines()
    return rawdata


def multiplier(entry):
    multiplier = 1
    colours = ['red', 'green', 'blue']
    for colour in colours:
        max_colour = max([int(c)
                          for c in re.findall(f'\d+(?= {colour})', entry)])
        multiplier *= max_colour
    s += multiplier


def main(file):
    rawdata = read(file)
    s = 0
    for entry in rawdata:
        s += multiplier(entry)
    print(s)


main('data.txt')

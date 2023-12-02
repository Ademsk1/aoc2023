import re


def read(file):
    rawdata = []
    with open(file) as f:
        rawdata = f.readlines()
    return rawdata


def valid(game):
    colours = ['red', 'green', 'blue']
    maximums = [12, 13, 14]
    for colour, maximum in zip(colours, maximums):
        invalid = [int(match) > maximum for match in re.findall(
            f'\d+(?= {colour})', game)]
        if any(invalid):
            return False
    return True


def main(file):
    rawdata = read(file)

    s = 0
    for entry in rawdata:
        id, game = entry.split(':')
        if valid(game):
            s += int(id.split(' ')[1])

    print(s)


main('./data.txt')

import re


def read(file):
    rawdata = []
    with open(file) as f:
        rawdata = f.readlines()
    return rawdata


def get_set_sum(game):
    colours = ['red', 'green', 'blue']
    maximums = [12, 13, 14]
    for colour, maximum in zip(colours, maximums):
        matches = re.findall(f'\d+ {colour}', game)
        gt = any([int(re.findall('\d+', result)[0])
                 > maximum for result in matches])
        if gt:
            return False
    return True


def main(file):
    rawdata = read(file)

    s = 0
    for entry in rawdata:
        id, game = entry.split(':')
        if get_set_sum(game):
            s += int(id.split(' ')[1])

    print(s)


main('./data.txt')

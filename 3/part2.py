def read(file):
    rawdata = []
    with open(file) as f:
        rawdata = f.readlines()
    return rawdata


def main(file):
    rawdata = read(file)

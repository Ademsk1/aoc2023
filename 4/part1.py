import re
def read(file):
    rawdata = []
    with open(file) as f:
        rawdata = f.readlines()
    return rawdata



def convert_to_int(numbers):
    return [int(n) for n in re.findall('\d+', numbers)]

def main(file):
    rawdata = read(file)
    total_score = 0
    for game in rawdata:
        score = 0
        _,_, raw_winning_n,_, raw_n = re.split('(:|\|)', game)
        numbers = re.findall('\d+', raw_n)
        for number in numbers:
            score += len(re.findall(f' {number} ', raw_winning_n))

        if score:
            score = 2**(score-1)
        else:
            score = 0
        total_score +=score


        

main('./4/data.txt')

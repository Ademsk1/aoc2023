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
    copies = [1 for _ in range(len(rawdata))]
    for i,game in enumerate(rawdata):
        score = 0
        _,_, raw_winning_n,_, raw_n = re.split('(:|\|)', game)
        numbers = re.findall('\d+', raw_n)
        for number in numbers:
            score += len(re.findall(f' {number} ', raw_winning_n))
        for j in range(score):
            copies[i+j+1] += copies[i]
    print(sum(copies))
        
    


        

main('./4/data.txt')

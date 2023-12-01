from part1 import read
import re

map_to_num = {
    'zero':'0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

def map(digit):
  if digit.isdigit():
    return digit
  return map_to_num[digit]
 



def main(file):
  calibration_document = read(file)
  sm = 0
  for line in calibration_document:
    digits = re.findall(r'(?=(\d|zero|one|two|three|four|five|six|seven|eight|nine))',line)
    try:
      joined_digits = int(map(digits[0]) + map(digits[-1]))
    except:
      joined_digits=0
    sm +=joined_digits
  print(sm)
    


if __name__=='__main__':
  main('./data1.txt')

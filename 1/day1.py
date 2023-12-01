import numpy as np
import re

def read(file):
  rawdata = []
  with open(file) as f:
    rawdata = f.readlines()
  return rawdata

def main(file):
  calibration_document = read(file)
  sm = 0
  for line in calibration_document:
    digits = re.findall('\d',line)
    try:
      joined_digits = int(digits[0] + digits[-1])
    except:
      joined_digits=0
    sm +=joined_digits
  print(sm)
    


main('./data.txt')

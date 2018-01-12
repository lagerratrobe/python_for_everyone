'''
Exercise 2: Write another program that prompts for a list of numbers as 
above and at the end prints out both the maximum and minimum of the 
numbers instead of the average.
'''

from __future__ import division

def num_check(value):
  '''Checks to see if value can be cast as a float.
  Returns: value as a float, if possible
           False, if not'''
  return_value = None
  try:
    return_value = float(value)
  except ValueError:
    if str.upper(value) == 'DONE':
      return_value = 'DONE'
    else:
      return_value = 'Invalid input'
  return return_value 

def calc_values(numbers):
  '''Generate some summary statictics from numbers and print them'''
  numbers.sort()
  total = sum(numbers)
  count = len(numbers)
  min_n = numbers[0]
  max_n = numbers[-1]
  print("Total = {}, Count = {}, Min = {}, Max = {}".format(total, count, min_n, max_n))

def main():
  numbers = []
  while True:
    value = raw_input('Enter a number:')
    checked_value = num_check(value)
    if checked_value == 'DONE':
      break
    elif checked_value == 'Invalid input':
      print(checked_value)
    else:
      numbers.append(checked_value)
  calc_values(numbers)
    

if __name__ == '__main__':
  main()

'''
Exercise 5.1: Write a program which repeatedly reads numbers until the user enters "done". 
Once "done" is entered, print out:

-	the total, 
-	count, 
-	average 
of the numbers. 
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
  total = sum(numbers)
  count = len(numbers)
  avg = round(total/count,2)
  print("Total = {}, Count = {}, Avg = {}".format(total, count, avg))

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

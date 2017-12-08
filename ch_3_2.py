'''Exercise 3.2 Rewrite your pay program using try and except so that your program
handles non-numeric input gracefully by printing a message and exiting the
program. The following shows two executions of the program'''

import sys

# Ex. 2
hours = None
pay_rate = None

try:
    hours = int(input("Enter number of hours worked: "))
except:
    print("Use a numeric value")
    sys.exit(1)

try:
    int(input("Enter rate of pay: "))
except:
    print("Use a numeric value")
    sys.exit(1)

# Did they work more than 40?
if hours >= 40:
  normal_hours = 40
  overtime_hours = hours - 40
  normal_pay = (pay_rate * 40)
  overtime_pay = (pay_rate * 1.5) * overtime_hours
  print("Pay =", normal_pay + overtime_pay)
else:
  pay = (hours * pay_rate)
  print ("Pay =", pay)

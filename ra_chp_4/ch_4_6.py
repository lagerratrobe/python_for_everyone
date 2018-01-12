'''Exercise 6: Rewrite your pay computation with time-and-a-half for overtime
and create a function called computepay which takes two parameters (hours and rate). '''

import sys

hours = None
pay_rate = None

def computepay(hours, pay_rate):
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

try:
    hours = int(input("Enter number of hours worked: "))
except:
    print("Use a numeric value")
    sys.exit(1)
try:
    pay_rate = int(input("Enter rate of pay: "))
except:
    print("Use a numeric value")
    sys.exit(1)

computepay(hours, pay_rate)

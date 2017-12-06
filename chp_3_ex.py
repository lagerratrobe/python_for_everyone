from __future__ import division

# Ex. 1
hours = int(raw_input("Enter number of hours worked: "))
pay_rate = int(raw_input("Enter rate of pay: "))

# Did they work more than 40? 
if hours >= 40:
  normal_hours = 40
  overtime_hours = hours - 40
  normal_pay = (pay_rate * 40)
  overtime_pay = (pay_rate * 1.5) * overtime_hours
  print "Pay =", normal_pay + overtime_pay
else:
  pay = (hours * pay_rate)
  print "Pay =", pay



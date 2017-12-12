from __future__ import absolute_import, division, print_function, unicode_literals
import sys

hours_work = input('Enter Hours: ')
hours_rate = input('Enter Rate: ')
hours_thresh = input('When do overhours start? (e.g. 40): ')
pay_factor = input('What is the overhours factor (e.g. 1.5x): ')
try:
   foo = int(hours_work)
   foo = int(hours_rate)
   foo = int(hours_thresh)
   foo = int(pay_factor)


except:
   sys.exit("Error, please enter a numeric input. \nProgram stopping")

if hours_work >= hours_thresh:

    hours_extra = float(hours_work) - float(hours_thresh)
    pay_extra = hours_extra * (float(pay_factor) * float(hours_rate))
    pay_normal = float(hours_thresh) * float(hours_rate)
    pay_total = pay_normal + pay_extra
    print('Total hours worked: ', hours_work)
    print('Earnings of normal hours worked: ', hours_thresh, 'hours @ ', hours_rate ,' total pay:', pay_normal, '\n')
    print('Earnings of extra hours worked: ', hours_extra, 'hours @', (float(hours_rate) * float(pay_factor)), ' total pay;', pay_extra, '\n')
    print('total money in da pocket: ', pay_total)
else:
    hours_work = float(hours_work) * float(hours_rate)
    print('Amount of money made: ', hours_work)
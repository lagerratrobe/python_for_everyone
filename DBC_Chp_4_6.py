from __future__ import absolute_import, division, print_function, unicode_literals
import sys

def computepay(hours_input, factor_pay):
    total = int(hours_input) * float(factor_pay) * float(hours_rate)
    return total


hours_work = input('Enter hours worked: ')
hours_rate = input('Enter hourly rate $: ')
hours_thresh = input('When do over hours start? (e.g. 40): ')
pay_factor = input('What is the overhours factor (e.g. 1.5x): ')

try:
   foo = float(hours_work)
   foo = float(hours_rate)
   foo = float(hours_thresh)
   foo = float(pay_factor)


except:
   sys.exit("Error, please enter a numeric input. \nProgram stopping")

if hours_work >= hours_thresh:

    hours_extra = float(hours_work) - float(hours_thresh)
    pay_normal = float(hours_thresh) * float(hours_rate)
    pay_extra = computepay(hours_extra, pay_factor)
    pay_total = pay_normal + pay_extra
    hour_rate_extra = float(hours_rate) * float(pay_factor)

    print('Total hours worked: ', hours_work,'\n')
    print('Normal payout:', hours_thresh, 'hours *', hours_rate ,'$/hour=', pay_normal, '\n')
    print('Extra payout:', hours_extra, 'hours *', hour_rate_extra, '$/overhours=', pay_extra, '\n')
    print('Total money in da pocket:', pay_total)
else:
    hours_work = float(hours_work) * float(hours_rate)
    print('Amount of money made:', hours_work)
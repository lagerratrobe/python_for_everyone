from __future__ import division

#Note: Python 2 uses "raw_input()", not "input()"
# Ex. 2
name = raw_input("What is your name? ")
print "Your name is ", name, "\n"

# Ex. 3
hours = raw_input("How many hours? ")
pay_rate = raw_input("How many dollars per hour? ")
pay = ( int(hours) * float(pay_rate) )
print "Your pay is: $",pay

# Ex. 4
width = 17
height = 12.0

print "\n8 =", width//2
print "8.5 =", width/2.0
print "4.0 = ", height/3
print "11 = ", 1 + 2 * 5

# Ex. 5
# C = (F - 32)/1.8
# C * 1.8 = F - 32
# (C * 1.8) + 32 = F
# Prompt for Celsius temp and convert to Farenheit
celsius = raw_input("\nEnter celsius temp: ")
farenheit =  (float(celsius) * 1.8) + 32
print "Farenheit temp = ", farenheit


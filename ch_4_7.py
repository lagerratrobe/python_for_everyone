'''Exercise 7: Rewrite the grade program from the previous chapter using a
function called computegrade that takes a score as its parameter and
returns a grade as a string.'''

import sys

def computegrade(score):
    grade = None
    if score > 1.0:
        print("Value too large. Enter value between 0.0 and 1.0")
        sys.exit(1)
    elif score >= .9:
        grade = "A"
    elif score >= .8:
        grade = "B"
    elif score >= .7:
        grade = "C"
    elif score >= .6:
        grade = "D"
    else:
        grade = "F"
    return grade

try:
    score = float(input("Enter score:"))
except:
    print("Enter a numeric value between 0.0 and 1.0")
    sys.exit(1)

print("Grade = {}".format(computegrade(score)))

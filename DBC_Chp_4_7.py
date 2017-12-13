from __future__ import absolute_import, division, print_function, unicode_literals
import sys

grade = []

def computegrade(grade_letter):
    if 1.0 <= grade_letter:
        sys.exit("Bad score (score outside range.)")
    elif 0.9 <= grade_letter:
        grade = "A"
    elif 0.8 <= grade_letter:
        grade = "B"
    elif 0.7 <= grade_letter:
        grade = "C"
    elif 0.6 <= grade_letter:
        grade = "D"
    elif 0.6 > grade_letter:
        grade = "F - aka 'The Maarten-award'"

    return grade

message_welcome="""
Score   Grade
>= 0.9     A
>= 0.8     B
>= 0.7     C
>= 0.6     D
< 0.6    F
~~~
"""

print(message_welcome)
grade_input = input('Enter score: ')

try:
   grade_input = float(grade_input)
except:
    sys.exit("Bad score (input is non numeric.)")

print(print_grade(computegrade(grade_input)))
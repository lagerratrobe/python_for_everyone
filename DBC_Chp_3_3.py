from __future__ import absolute_import, division, print_function, unicode_literals
import sys
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

grade_input = input('Enter score:')
grade = []

try:
   grade_input = float(grade_input)
except:
    sys.exit("Bad score (input is non numeric.)")

if 1.0 <= grade_input:
    sys.exit("Bad score (score outside range.)")
elif 0.9 <= grade_input:
    grade = "A"
elif 0.8 <= grade_input:
    grade = "B"
elif 0.7 <= grade_input:
    grade = "C"
elif 0.6 <= grade_input:
    grade = "D"
elif 0.6 > grade_input:
    grade = "F - aka 'The Maarten-award'"

print("Your score is:", grade)
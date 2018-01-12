'''Write a program to prompt for a score between 0.0 and 1.0. If the
score is out of range, print an error message. If the score is between 0.0 and 1.0,
print a grade using the following table:

Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
Enter score: 0.95 -     A
Enter score: perfect -  Bad score
Enter score: 10.0 -     Bad score
Enter score: 0.75 -     C
'''
import sys

score = input("Enter score:")
grade = None
try:
    score = float(score)
except:
    print("Enter a numeric value between 0.0 and 1.0")
    sys.exit(1)

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

print("Grade = {}".format(grade))

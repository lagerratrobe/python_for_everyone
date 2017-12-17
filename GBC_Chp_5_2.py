from __future__ import absolute_import, division, print_function, unicode_literals
largest = 0
smallest = 0


while True:
    user_input = input("Please provide a number (or type done): ")

    if user_input == "done":
        break

    try:
        user_input = int(user_input)
    except:
        print("Bad data (please enter a number or type 'done')")
        continue

    if int(user_input) > int(largest):
        largest = user_input
    elif int(user_input) < int(smallest):
        smallest = user_input

print ("Largest number:", largest)
print ("Smallest number:", smallest)
user_input = 0
number_input = 0
i = 0

def calc_avr(total, diff_number):
    if total <= 0:
       print("Error: Input total is zero, cannot calculate average")
       return None

    return int(total)/int(diff_number)


while True:

    user_input = input ("Enter a number (or 'done' to exit':")

    if user_input == "done":
        break

    try:
       user_input = int(user_input)
    except:
        print("Bad data (please enter a number or type 'done')")
        continue

    number_input = int(number_input) + int(user_input)
    i = i + 1

print("Total:", number_input)
print("Count:", i)
print("Average:", calc_avr(number_input, i))
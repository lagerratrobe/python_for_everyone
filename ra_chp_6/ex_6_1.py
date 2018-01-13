'''Exercise 1: Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a separate line, except backwards.'''

word = "foo"

word_length = len(word)
transmogrifier = word_length + 1

while word_length > 0:
  index = word_length - transmogrifier
  print(word[index])
  word_length -= 1

# Honestly though, this is retarded.  Do this instead:
for char in word[::-1]:
  print char

#make characters small
#make remove characters after space 
#remove non alphanumerics

import string


# Open the file in read mode
with open('tagalog_wordlist.txt', 'r') as file:
  # Read all the lines in the file into a list
  lines = file.readlines()

# Open the file in write mode
with open('cebuano_wordlist.txt', 'w') as file:
  # Iterate over the lines in the list
  for line in lines:
    # Make all letters lowercase
    line = line.lower()
    # Remove everything after the first space
    line = line.split(' ', 1)[0]
    # Remove all non-alphanumeric characters
    line = ''.join(c for c in line if c.isalnum())
    # Split the line into words
    words = line.split()
    # Join the words back into a single string
    line = ' '.join(words)
    # Write the modified line to the file
    file.write(line + '\n')


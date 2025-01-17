
# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Matthew Seepersaud
# Date: 2025/ 01/ 15
# Purpose: Use string methods and f-string formating.
# Usage: ./lab1d.py

#TO-DO 1:
#	Create a variable called "name" and assign it the value of your name.
# Use the string method .upper() to convert the name to upper case.
# Create another variable called “age”, the value of “age” should be your age
# The script, when executed, should print out "How are you yourname? Happy xxth birthday!" To print this output use .format() method. 

name = "Matthew"
uppercase_text = name.upper()
print (uppercase_text)
#TO-DO 2:
# Create a variable called "words".
# The value of words should be "The quick brown fox jumps over the lazy dog".
# Use indexing to return the first and 17th charecters of "words" to the user.
words = "The quick brown fox jumps over the lazy dog"
characters = words [0] + words [16]
print (characters)
#TO-DO 3:
# Use negative indexing to return the words "jumps" and "quick" from "words" to the user.
jumps = words [-23:-18]
print(jumps)
quick = words [-39:-34]
print(quick)
#TO-DO 4:
# Use slicing to retun everything between index 2-15 to the user.
# Print "uick brown foxs ju" from "words".
user = words [2:15]
print (user)
uick = words [5:22]
print (uick)
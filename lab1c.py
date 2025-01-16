
# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Matthew Seeprsaud
# Date: 2025/ 01/ 15 
# Purpose: Use string methods and f-string formating.
# Usage: ./lab1c.py

#TO-DO 1:
# import math module.
# Create a variable called 'radius' and take its value form user.
# Convert the variable to integer using int()
# use the contant pi form math module and compute the area of the circle using the variable 'radius'

import math                                             # Imported math module for pi
radius = int (input("Enter the radius: "))                   # Have the user input a int for the radius
circumfrence = 2 * math.pi * radius 
print (circumfrence)                                        # Print the result
# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "Lion"            # Runtime Error: Not defined correctly
animal_type = "cub"
number_of_teeth = 16

full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth" # LogicalError: variables are wrong way round AND SyntaxError need to add "f" at the front to parse the variables into the string.

print(full_spec)         # SyntaxError: Missing parentheses in call to 'print'.


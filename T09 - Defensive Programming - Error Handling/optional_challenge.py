Print("Welcome to my Program")      # Syntax Error 1: Print with capital P is not a defined python function

name = "python"
counter = 0

# Runtime error: there will be an index error after all the letters p y t h o n are printed
while true:                          # Syntax Error 2: need `True` not `true`, lower case true is not a defined boolean in python
    print(name[counter])
    counter += 1

# Logical Error: cant concatenate a str with an int
print("The word python has " + counter + " letters in it")
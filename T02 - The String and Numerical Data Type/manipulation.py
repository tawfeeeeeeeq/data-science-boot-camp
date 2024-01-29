# Ask the user to enter a sentence and Save in a variable called str_manip.
# str_manip = "Hello how is everyone" # Test sting
str_manip = input("Please enter a sentence : ")

# Calculate and display the length of str_manip.
print(len(str_manip))

# Find the last letter in str_manip sentence. 
last_letter = str_manip[-1]
print(last_letter)

# Replace every occurrence of this letter in str_manip with ‘@’.
print(str_manip.replace(last_letter,"@"))

# Print the last 3 characters in str_manip backwards.
print(str_manip[:-4:-1])

# Create a five-letter word that is made up of the first three characters and the last two characters in str_manip.
str_five = str_manip[:3] + str_manip[-2:]
print(str_five)
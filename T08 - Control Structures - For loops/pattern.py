'''
This program outputs a star pattern that increases then decreases
This program uses an if-else statement in combination with a single for loop
'''

# This is the maximum form of the output pattern
pattern = "*****"
# To print the pattern that increases then decreases we will loop for double the length of our pattern
loopsize = len(pattern)*2

# Begin looping
for i in range(1,loopsize):
    # When the pattern is in the increasing phase
    if i < len(pattern):
        print(pattern[0:i])
    # When the pattern is in the decreasing phase
    else:
        print(pattern[0:loopsize-i])


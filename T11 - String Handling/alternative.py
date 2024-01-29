'''
This program reads in a string and 
  (1) makes each alternate character into upper and then lower case.
  (2) with the same string - making each alternate word lower and upper case.
'''

# Get sentence from user
sentence = input("Enter a sentence : ")


alt_char = ""
# Loop thru each character and alternate the case
for i in range(len(sentence)):
    # Odd indexes will be lower case
    if i%2 == 1:
        alt_char += sentence[i].lower()
    # Even indexes will be upper case
    else:
        alt_char += sentence[i].upper()
print(alt_char)


words = sentence.split(" ")
# Loop thru each word and alternate the case
for i in range(len(words)):
    # Odd indexes will be lower case
    if i%2 == 1:
        words[i] = words[i].lower()
    # Even indexes will be upper case
    else:
        words[i] = words[i].upper()
# Make one string from the list of strings `words`
alt_word = " ".join(words)
print(alt_word)
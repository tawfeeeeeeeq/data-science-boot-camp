# Import the spaCy library to allow as to do some natural language processing
import spacy
nlp = spacy.load('en_core_web_sm')

# Create a list of `Garden Path Sentences` for us to examine
gardenpathSentences = ["The old man the boat.", 
                       "The complex houses married and single soldiers and their families.", 
                       "The horse raced past the barn fell.", 
                       "We painted the wall with cracks.",
                       "Mary gave the child the dog bit a Band-Aid",
                       "That Jill is never here hurts.",
                       "The cotton clothing is made of grows in Mississippi."]

# Iterate through all the Garden Path Sentences
for sentence in gardenpathSentences:
    # Tokenise the text and then print the tokenised list
    doc = nlp(sentence)
    print([token.text for token in doc])

    # Perform named entity recognition.
    for ent in doc.ents:
        # Print responses
        print(ent.text, ent.label, ent.label_)
        # Get the explanation of an entity and print it
        print(ent.label_, ": ", spacy.explain(ent.label_))

    # Print a line to seperate the resulsts for each garden path sentence
    print("---------------------------------")


"""
Below are 2 entities the my program has looked up.

Entity 1: PERSON
- `PERSON` was explained to be "People, including fictional"
- Yes, this entity made sense as it described the name Mary.

Entity 2: GPE
- `GPE` was explained to be "Countries, cities, states"
- Yes, this entity made sense as it described Mississsippi.
"""

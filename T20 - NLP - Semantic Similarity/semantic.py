import spacy  # importing spacy
nlp = spacy.load('en_core_web_md')
#nlp = spacy.load('en_core_web_sm') 

print("SIMILARITY WITH SPACY")
print("----------------------------------------")
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.text, word2.text, word1.similarity(word2))
print(word3.text, word2.text, word3.similarity(word2))
print(word3.text, word1.text, word3.similarity(word1))
print(" * Cats are not known to eat bananas so it has the smallest value.")

print("\nMy own example")
word4 = nlp("zoo")
print(word4.text, word1.text, word4.similarity(word1))
print(word4.text, word2.text, word4.similarity(word2))
print(word4.text, word3.text, word4.similarity(word3))
print(" * Cat and Monkey both have higher values because they are animals.")
print(" * Monkey has the highest value, as its the one you are likely to find in a zoo.")
print(" ** When using `en_core_web_sm` the values are way higher ")
print("----------------------------------------","\n")

print("WORKING WITH VECTORS")
print("----------------------------------------")
tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
print("----------------------------------------","\n")

print("WORKING WITH SENTENCES")
print("----------------------------------------")
sentence_to_compare = "Why is my cat on the car"
print("-------", sentence_to_compare, "-------")
sentences = ["where did my dog go",
             "Hello, there is my car",
             "I\'ve lost my car in my car",
             "I\'d like my boat back",
             "I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(similarity," - ",sentence)
print("----------------------------------------","\n")
import spacy
nlp = spacy.load('en_core_web_md')
nlp2 = spacy.load('en_core_web_sm')
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

print('-------------------------------------------------------------') # divider for ease of reading terminal output

tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
'''
I found it interesting how cat-banana had a stronger similarity than cat-apple; what is it about bananas that are closer to cats?!
'''
print("my own list:")
tokens = nlp('chicken cow turkey burger wing')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
'''
I tried playing around with animal names and meat products, and the fact that chicken/turkey are both the name of the animal and the meat product. 
Interestingly, 'cow-burger' has a very low level of similarity when compared to 'chicken-burger' and 'turkey-burger'.
I was also suprised at how low-similarity 'chicken-wing' was, considering that chickens have wings AND that 'wings' are a chicken product! 
'''
print("my own list with the simpler sm language model:")
tokens = nlp2('chicken cow turkey burger wing')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))


print('-------------------------------------------------------------')

sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
      similarity = nlp(sentence).similarity(model_sentence)
      print(sentence + " - ",  similarity)
print('-------------------------------------------------------------')
'''
Having run the example.py program with the simpler en_core_web_sm model, I noticed the program was consistently lower levels of similarity
Usually this was 50-80%, with a few outliers. For the complete matches they both returned 1.0, and a higher similarity in the 'md' model generally correlated with a higher similarity in the 'sm' model.
'''
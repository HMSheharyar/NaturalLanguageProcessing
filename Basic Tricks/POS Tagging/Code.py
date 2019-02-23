<=============================================== Parts of Speech (POS) Tagging ===============================================>

import nltk
tokens = nltk.word_tokenize("I am trying to tag the words with POS tagging of NLTK.")
print("Parts of Speech: ", nltk.pos_tag(tokens))

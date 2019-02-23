<=============================================== Antonyms (WordNet) ===============================================>

from nltk.corpus import wordnet
antonyms = []
for syn in wordnet.synsets("big"):
    for l in syn.lemmas():
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())
print(antonyms)

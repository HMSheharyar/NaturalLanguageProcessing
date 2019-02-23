<=============================================== Synonyms (WordNet) ===============================================>

from nltk.corpus import wordnet 
synonyms = []
for syn in wordnet.synsets('conflict'):
    for lemma in syn.lemmas():
        synonyms.append(lemma.name())
print(synonyms)

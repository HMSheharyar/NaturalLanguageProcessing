<=============================================== Stemming ===============================================>

from nltk.stem import PorterStemmer
stemmer = PorterStemmer() 
print(stemmer.stem('playing'))

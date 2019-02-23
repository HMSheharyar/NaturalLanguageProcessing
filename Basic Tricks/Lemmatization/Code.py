<=============================================== Lemmatization ===============================================>

from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize('processes'))

//The default POS is nouns. Switch it to verb for better results.
print(lemmatizer.lemmatize('running', pos="v"))

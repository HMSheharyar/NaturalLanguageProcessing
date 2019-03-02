<============================================= Sentiment Analysis (Supervised) =============================================>


#<--------Libraries Import-------->
from nltk.corpus import movie_reviews
from nltk.corpus import stopwords
from nltk import NaiveBayesClassifier
from nltk import classify 
from nltk.tokenize import word_tokenize
from nltk import ngrams
from random import shuffle 
import string

 
#<--------Data Preprocessing-------->

stopwords_list = stopwords.words('english')
important_words_for_bigrams = ['above', 'below', 'off', 'over', 'under', 'more', 'most', 'such', 'no', 'nor', 'not', 'only', 'so', 'than', 'too', 'very', 'just', 'but']
stopwords_list_for_bigrams = set(stopwords_list) - set(important_words_for_bigrams)

#Removing Stopwords and Punctuation
def clean_words(words, stopwords_list):
    words_clean = []
    for word in words:
        word = word.lower()
        if word not in stopwords_list and word not in string.punctuation:
            words_clean.append(word)    
    return words_clean 
 
    

#<--------Feature Extraction-------->  

#Feature Extractor for Uni-grams
def bag_of_words(words):    
    words_dictionary = dict([word, True] for word in words)    
    return words_dictionary
 
#Feature Extractor for Bi-grams
def bag_of_ngrams(words, n=2):
    words_ng = []
    for item in iter(ngrams(words, n)):
        words_ng.append(item)
    words_dictionary = dict([word, True] for word in words_ng)    
    return words_dictionary

#Feature Extractor for both Uni-grams and Bi-grams
def bag_of_all_words(words, n=2):
    if type(words) is str: 
        words = word_tokenize(words)
    words_clean = clean_words(words, stopwords_list)
    words_clean_for_bigrams = clean_words(words, stopwords_list_for_bigrams)
 
    unigram_features = bag_of_words(words_clean)
    bigram_features = bag_of_ngrams(words_clean_for_bigrams)
 
    all_features = unigram_features.copy()
    all_features.update(bigram_features)
 
    return all_features



#<--------Training Classifier-------->  
    
pos_reviews = []
for fileid in movie_reviews.fileids('pos'):
    words = movie_reviews.words(fileid)
    pos_reviews.append(words)
 
neg_reviews = []
for fileid in movie_reviews.fileids('neg'):
    words = movie_reviews.words(fileid)
    neg_reviews.append(words)
    
#Positive reviews feature set
pos_reviews_set = []
for words in pos_reviews:
    pos_reviews_set.append((bag_of_all_words(words), 'pos'))
 
#Negative reviews feature set
neg_reviews_set = []
for words in neg_reviews:
    neg_reviews_set.append((bag_of_all_words(words), 'neg'))

#Shuffling the feature sets
shuffle(pos_reviews_set)
shuffle(neg_reviews_set)
 
#Train/Test Splits 
train_set = pos_reviews_set[200:] + neg_reviews_set[200:]
test_set = pos_reviews_set[:200] + neg_reviews_set[:200]

#Training the Naive Bayes Classifier
classifier = NaiveBayesClassifier.train(train_set)
 
#Checking the accuracy of the trained model
accuracy = classify.accuracy(classifier, test_set)
print(accuracy)



#<--------Testing the model with new reviews-------->  

new_review = "I was a disaster movie. Very bad ending."
new_review_set = bag_of_all_words(new_review)
print (classifier.classify(new_review_set))

new_review = "The movie was outstanding. Perfectly ended."
new_review_set = bag_of_all_words(new_review)
print (classifier.classify(new_review_set))

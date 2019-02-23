<=============================================== Word Frequency ===============================================>

import urllib.request
from bs4 import BeautifulSoup
import nltk 
response = urllib.request.urlopen('https://www.businessinsider.com') 
html = response.read() 
soup = BeautifulSoup(html,"html5lib") 
text = soup.get_text(strip=True) 
tokens = [t for t in text.split()] 
freq = nltk.FreqDist(tokens) 
for key,val in freq.items(): 
    print (str(key) + ':' + str(val))

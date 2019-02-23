<=============================================== Stop Words Removal ===============================================>

import urllib.request
from bs4 import BeautifulSoup  
import nltk 
from nltk.corpus import stopwords 
response = urllib.request.urlopen('https://www.businessinsider.com') 
html = response.read() 
soup = BeautifulSoup(html,"html5lib") 
text = soup.get_text(strip=True) 
tokens = [t for t in text.split()] 
clean_tokens = tokens[:] 
sr = stopwords.words('english') 
for token in tokens: 
    if token in stopwords.words('english'):
        clean_tokens.remove(token) 

<-------------------------------------------- Tokenize (Pure Python) -------------------------------------------->

import urllib.request 
from bs4 import BeautifulSoup 
response = urllib.request.urlopen('https://www.businessinsider.com') 
html = response.read() 
soup = BeautifulSoup(html,"html5lib") 
text = soup.get_text(strip=True) 
tokens = [t for t in text.split()] 
print (tokens)

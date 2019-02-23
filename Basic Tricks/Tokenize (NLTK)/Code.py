<=============================================== Tokenize (NLTK) ===============================================>

from bs4 import BeautifulSoup
import nltk 
from nltk.tokenize import sent_tokenize 
from urllib.request import Request, urlopen
req = Request('https://tribune.com.pk', headers={'User-Agent': 'Mozilla/5.0'})
html = urlopen(req).read()
soup = BeautifulSoup(html,"html5lib") 
text = soup.get_text(strip=True) 
print(sent_tokenize(text))
